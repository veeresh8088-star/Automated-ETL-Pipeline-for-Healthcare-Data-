import schedule
import time
from etl import run_etl

def job():
    print("Running ETL pipeline...")
    run_etl()

schedule.every(1).minutes.do(job)

print("Scheduler started...")
while True:
    schedule.run_pending()
    time.sleep(1)
