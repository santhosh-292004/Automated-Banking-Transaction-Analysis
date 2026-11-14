Automated Banking Transaction Analysis & Visualization Dashboard

Project Overview

This project analyzes banking transaction data stored in a MySQL database using Python, Pandas, and Matplotlib. It cleans transaction records, performs data analysis, and generates visual reports to understand transaction patterns and customer account balances.

Tech Stack

- Python – Core programming
- MySQL – Database storage
- Pandas – Data cleaning and analysis
- Matplotlib – Data visualization and reporting
- mysql.connector – MySQL database connectivity
- python-dotenv – Loads database configuration from environment variables
- Schedule – Scheduled task execution
  
Database Details

- Database Name: banking_analysis
- Table Name: bank_transactions
  
Dataset Columns

- TransactionID
- CustomerID
- CustomerDOB
- CustGender
- CustLocation
- CustAccountBalance
- TransactionDate
- TransactionTime
- TransactionAmount (INR)
  
Key Features

- Extracts banking transaction data from MySQL.
- Handles missing values and removes duplicate records.
- Converts transaction dates for date-based analysis.
- Analyzes transaction amount distributions.
- Identifies potential transaction amount outliers.
- Compares gender-wise transaction counts and amounts.
- Visualizes daily transaction trends.
- Displays the top 10 customers by transaction amount.
- Analyzes customer account balance distribution.
- Saves generated charts as PNG images in the reports folder.
- Supports scheduled chart generation using Python's schedule library.
  
Visual Reports

The project generates the following visualizations:

1. Transaction Amount Distribution
2. Transaction Amount Outlier Detection
3. Gender-wise Transaction Count
4. Gender-wise Total Transaction Amount
5. Daily Banking Transaction Trend
6. Top 10 Customers by Transaction Amount
7. Customer Account Balance Distribution
8. Transaction Amount by Gender
   
Project Structure

banking_transaction_project/
│
├── main.py
├── database.py
├── analysis.py
├── charts.py
├── scheduler.py
├── requirements.txt
├── README.md
└── reports/
    └── (generated chart images)
    
Installation and Setup

1. Install Python and MySQL
   
- Install Python and ensure it is available from your terminal.
- Install MySQL and make sure the MySQL server is running.
  
2. Install Dependencies
   
Open a terminal in the project directory and run:
pip install -r requirements.txt

3. Configure the MySQL Database
   
- Create or use the banking_analysis database.
- Ensure the bank_transactions table contains the dataset and the required columns listed above.
  
4. Configure Environment Variables
   
The database connection details are read from a .env file. Create a file named .env in the project root (the same folder as database.py) and add your own MySQL details:

DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=banking_analysis

Replace the example values with your actual MySQL configuration.

Security note: Do not upload your .env file to GitHub. It contains private database credentials. The .gitignore file should include .env.

5. Run the Project
   
Run the main Python script from the project directory:
python main.py
Run the scheduler separately if scheduled execution is configured:
python scheduler.py
The scheduler must remain running for scheduled jobs to execute.

Output

Generated visualization images are saved in the reports folder. These reports help users understand banking transaction patterns and customer-related metrics.

Future Enhancements

- Add an interactive dashboard.
- Include more detailed transaction analysis.
- Improve anomaly detection using statistical techniques.
- Add automated report export options.
  
Conclusion

This project demonstrates the practical use of Python, MySQL, Pandas, and Matplotlib for banking transaction analysis and visualization. It provides hands-on experience in database connectivity, data cleaning, data analysis, visualization, and report automation.
