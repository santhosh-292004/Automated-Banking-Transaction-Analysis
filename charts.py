import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import pandas as pd
import os
from datetime import datetime
from analysis import clean_data, daily_transaction_analysis

def create_charts():
    os.makedirs("reports", exist_ok = True)

    data = clean_data()
    daily = daily_transaction_analysis(data)

    today = datetime.now().strftime("%Y%m%d")

    plt.figure(figsize = (10,5))

    daily["TransactionDate"] = pd.to_datetime(daily["TransactionDate"])
    daily = daily.sort_values("TransactionDate")

    plt.plot(
        daily["TransactionDate"],
        daily["TransactionAmount (INR)"],
        marker = "o",
        color = "blue"
    )
    plt.title("Daily Banking Transaction Trend")
    plt.xlabel("Transaction Date")
    plt.ylabel("Transaction Amount (INR)")
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.DayLocator(interval = 10))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%y-%m-%d"))
    plt.xticks(rotation = 45, ha = "right")
    plt.tight_layout()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"reports/daily_transaction_{today}.png")
    plt.close()

    plt.figure(figsize = (10,5))
    plt.hist(data["TransactionAmount (INR)"], bins = 100,color = "blue", edgecolor = "black")
    plt.xlim(0, 15000)
    plt.ylim(0, 50)
    plt.title("Transaction Amount Distribution")
    plt.xlabel("Transaction Amount (INR)")
    plt.ylabel("Number of Transactions")
    plt.tight_layout()
    plt.savefig("reports/transactions_distribution.png")
    plt.close()

    plt.figure(figsize = (10,5))
    plt.boxplot(data["TransactionAmount (INR)"].dropna())
    plt.title("Banking Transaction Amount - Outlier Detection")
    plt.ylabel("Transaction Amount (INR)")
    plt.grid(axis = "y", linestyle = "dashed", alpha = 0.5)
    plt.tight_layout()
    plt.savefig("reports/transaction_boxplot.png", dpi = 300)
    plt.close()

    gender_data = data[data["CustGender"].isin(["M", "F"])]
    gender_counts = gender_data["CustGender"].value_counts()
    plt.figure(figsize = (8,5))
    plt.bar(gender_counts.index, gender_counts.values)
    plt.title("Gender-wise Transaction Count")
    plt.xlabel("Customer Gender")
    plt.ylabel("Number of Transactions")
    plt.tight_layout()
    plt.savefig("reports/gender_transaction_count.png", dpi = 300)
    plt.close()

    gender_data = data[data["CustGender"].isin(["M", "F"])]
    gender_amount = gender_data.groupby("CustGender")["TransactionAmount (INR)"].sum()
    plt.figure(figsize = (8,5))
    plt.bar(gender_amount.index, gender_amount.values, color = "red", edgecolor = "black")
    plt.title("Gender-wise Total Transaction Amount")
    plt.xlabel("Customer Gender")
    plt.ylabel("Total Transaction Amount (INR)")
    plt.tight_layout()
    plt.savefig("reports/gender_transaction_amount.png", dpi = 300)
    plt.close()

    customer_amount = data.groupby("CustomerID")["TransactionAmount (INR)"].sum()
    top_customers = customer_amount.sort_values(ascending = False).head(10)
    plt.figure(figsize = (10,5))
    top_customers.plot(kind = "bar", color = "teal", edgecolor = "black")
    plt.title("Top 10 Customer Transaction Amount")
    plt.xlabel("Customer ID")
    plt.ylabel("Total Transaction Amount (INR)")
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.savefig("reports/top_10_customers.png", dpi = 300)
    plt.close()

    plt.figure(figsize = (10,5))
    plt.hist(data["CustAccountBalance"].dropna(),bins = 20, color = "skyblue", edgecolor = "black")
    plt.ylim(0, 50)
    plt.title("CustAccount Account Balance Distribution")
    plt.xlabel("Account Balance (INR)")
    plt.ylabel("Number of Customers")
    ax = plt.gca()
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"₹{x / 100000:.1f}L"))
    plt.tight_layout()
    plt.savefig("reports/account_balance_distribution.png", dpi = 300)
    plt.close()

    gender_data = data[data["CustGender"].isin(["M", "F"])]
    gender_data = data.groupby("CustGender")["TransactionAmount (INR)"].sum()
    plt.figure(figsize = (8,8))
    plt.pie(
        gender_data,
        labels = gender_data.index.map({"M": "Male", "F": "Female"}),
        autopct = "%1.1f%%",
        startangle = 90
    )
    plt.title("Transaction Amount by Gender")
    plt.tight_layout()
    plt.savefig("reports/transaction_amount_by_gender.png")
    plt.close()

if __name__ == "__main__":
    create_charts()

