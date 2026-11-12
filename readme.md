\# Automated Banking Transaction Analysis \& Visualization Dashboard



\## Project Overview



This project analyzes banking transaction data stored in a MySQL database using Python, Pandas, and Matplotlib. It cleans transaction records, performs data analysis, and generates visual reports to understand transaction patterns and customer account balances.



\## Tech Stack



\- \*\*Python\*\* – Core programming

\- \*\*MySQL\*\* – Database storage

\- \*\*Pandas\*\* – Data cleaning and analysis

\- \*\*Matplotlib\*\* – Data visualization and reporting

\- \*\*mysql.connector\*\* – MySQL database connectivity

\- \*\*Schedule\*\* – Scheduled task execution



\## Database Details



\- \*\*Database Name:\*\* `banking\_analysis`

\- \*\*Table Name:\*\* `bank\_transactions`



\### Dataset Columns



\- `TransactionID`

\- `CustomerID`

\- `CustomerDOB`

\- `CustGender`

\- `CustLocation`

\- `CustAccountBalance`

\- `TransactionDate`

\- `TransactionTime`

\- `TransactionAmount (INR)`



\## Key Features



\- Extracts banking transaction data from MySQL.

\- Handles missing values and removes duplicate records.

\- Converts transaction dates for date-based analysis.

\- Analyzes transaction amount distributions.

\- Identifies potential transaction amount outliers.

\- Compares gender-wise transaction counts and amounts.

\- Visualizes daily transaction trends.

\- Displays the top 10 customers by transaction amount.

\- Analyzes customer account balance distribution.

\- Saves generated charts as PNG images in the `reports` folder.

\- Supports scheduled chart generation using Python's `schedule` library.



\## Visual Reports



The project generates the following visualizations:



1\. Transaction Amount Distribution

2\. Transaction Amount Outlier Detection

3\. Gender-wise Transaction Count

4\. Gender-wise Total Transaction Amount

5\. Daily Banking Transaction Trend

6\. Top 10 Customers by Transaction Amount

7\. Customer Account Balance Distribution

8\. Transaction Amount by Gender



\## Project Structure



```text

banking\_transaction\_project/

│

├── main.py

├── database.py

├── analysis.py

├── charts.py

├── scheduler.py

├── requirements.txt

├── README.md

└── reports/

```



\## Installation and Setup



\### 1. Install Python



Install Python and ensure it is available from your terminal.



\### 2. Install Dependencies



Open the terminal in the project directory and run:



```bash

pip install -r requirements.txt

```



\### 3. Configure MySQL



\- Ensure MySQL is installed and running.

\- Create or use the `banking\_analysis` database.

\- Ensure the `bank\_transactions` table contains the required dataset.

\- Update the database connection settings in `database.py` with your own MySQL credentials.



\### 4. Run the Project



Run the main Python script from the project directory:



```bash

python main.py

```



Run the scheduler separately if scheduled execution is configured:



```bash

python scheduler.py

```



The scheduler must remain running for scheduled jobs to execute.



\## Output



Generated visualization images are saved in the `reports` folder. These reports help users understand banking transaction patterns and customer-related metrics.



\## Future Enhancements



\- Add an interactive dashboard.

\- Include more detailed transaction analysis.

\- Improve anomaly detection using statistical techniques.

\- Add automated report export options.



\## Conclusion



This project demonstrates the practical use of Python, MySQL, Pandas, and Matplotlib for banking transaction analysis and visualization. It provides hands-on experience in database connectivity, data cleaning, data analysis, visualization, and report automation.

