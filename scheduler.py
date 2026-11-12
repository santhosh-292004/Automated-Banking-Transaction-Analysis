import schedule
import time
from charts import create_charts

def job():
    print("Banking Analysis Started...")
    create_charts()
    print("Banking Analysis Completed...")

schedule.every().day.at("06:00").do(job)

print("Scheduler Started...Waiting for 6 AM")

while True:
    schedule.run_pending()
    time.sleep(60)