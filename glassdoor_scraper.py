import pandas as pd
from playwright.sync_api import sync_playwright
from proxy_utils import get_proxy

def scrape_glassdoor():
    proxy = get_proxy()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, proxy={"server": proxy} if proxy else None)
        page = browser.new_page()
        page.goto("https://www.glassdoor.co.in/Job/software-engineer-jobs-SRCH_KO0,17.htm", timeout=60000)

        page.wait_for_selector(".react-job-listing", timeout=10000)
        job_cards = page.query_selector_all(".react-job-listing")

        results = []
        for card in job_cards[:10]:
            title = card.query_selector(".jobTitle").inner_text()
            company = card.query_selector(".jobEmpolyerName").inner_text()
            location = card.query_selector(".jobLocation").inner_text()
            link = "https://www.glassdoor.co.in" + card.get_attribute("data-job-id")
            results.append({
                "title": title, "company": company, "location": location,
                "url": link, "source": "glassdoor"
            })

        browser.close()
        return pd.DataFrame(results)
