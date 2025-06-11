import pandas as pd
from naukri_scraper import scrape_naukri
from glassdoor_scraper import scrape_glassdoor
from ziprecruiter_scraper import scrape_ziprecruiter
from google_sheets import upload_to_google_sheets
from datetime import datetime

def main():
    all_jobs = []

    for scraper_func in [scrape_naukri, scrape_glassdoor, scrape_ziprecruiter]:
        try:
            jobs = scraper_func()
            all_jobs.append(jobs)
        except Exception as e:
            print(f"[ERROR] Failed to scrape with {scraper_func.__name__}: {e}")

    if all_jobs:
        df = pd.concat(all_jobs, ignore_index=True)
        df['date_fetched'] = datetime.now().strftime('%Y-%m-%d')
        upload_to_google_sheets(df)
    else:
        print("No data scraped.")

if __name__ == "__main__":
    main()
