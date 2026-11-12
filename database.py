import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


def fetch_data():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    query = "SELECT * FROM bank_transactions"
    df = pd.read_sql(query, conn)

    conn.close()

    return df