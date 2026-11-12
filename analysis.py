import pandas as pd
from database import fetch_data

def clean_data():
    df = fetch_data()

    df["transactionDate"] = pd.to_datetime(df["TransactionDate"],format = "%d/%m/%y", errors = "coerce")

    df = df.drop_duplicates()

    df["CustGender"] = df["CustGender"].fillna("unknown")

    df["CustAccountBalance"] = df["CustAccountBalance"].fillna(df["CustAccountBalance"].median())

    df = df[df["TransactionAmount (INR)"] > 0]

    return df

def daily_transaction_analysis(df):
    def transaction_type_analysis(df):
        result = df.groupby("TransactionType")["TransactionAmount (INR)"].sum().reset_index()
        return result
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"],format = "%m/%d/%y")
    daily = df.groupby("TransactionDate")["TransactionAmount (INR)"].sum().reset_index().sort_values("TransactionDate")
    return daily

def customer_balance_analysis(df):
    result = df.groupby("CustLocation")["CustAccountBalance"].mean().reset_index()
    result = result.sort_values("CustAccountBalance", ascending = False)
    return result

if __name__ == "__main__":
    data = clean_data()

    data["CustomerDOB"] = pd.to_datetime(
        data["CustomerDOB"], errors="coerce"
    )

    today = pd.Timestamp.today()
    data["CustomerAge"] = (today.year - data["CustomerDOB"].dt.year)

    print("Rows after cleaning: ",len(data))
    print("Missing Values: ")
    print(data.isnull().sum())

    daily = daily_transaction_analysis(data)
    print("\ndaily Transaction Analysis: ")
    print(daily)

    balance = customer_balance_analysis(data)
    print("\nAverage Account Balance by Location: ")
    print(balance)










