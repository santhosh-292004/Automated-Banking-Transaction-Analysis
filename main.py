import mysql.connector
import pandas as pd

from analysis import (
    clean_data,
    daily_transaction_analysis,
    customer_balance_analysis
)
from charts import create_charts


def main():
    print("Banking Transaction Analysis Started...")

    # 1. Fetch and clean data
    data = clean_data()

    print("\nRows after cleaning:", len(data))
    print("\nMissing Values:")
    print(data.isnull().sum())

    # 2. Daily transaction analysis
    daily = daily_transaction_analysis(data)

    print("\nDaily Transaction Analysis:")
    print(daily)

    # 3. Customer balance analysis
    balance = customer_balance_analysis(data)

    print("\nAverage Account Balance by Location:")
    print(balance)

    # 4. Create all charts
    create_charts()

    print("\nBanking Transaction Analysis Completed!")


if __name__ == "__main__":
    main()
