import pandas as pd
from playwright.sync_api import sync_playwright
from proxy_utils import get_proxy

def scrape_naukri():
    proxy = get_proxy()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, proxy={"server": proxy} if proxy else None)
        page = browser.new_page()
        page.goto("https://www.naukri.com/software-engineer-jobs", timeout=60000)

        job_cards = page.query_selector_all("article.jobTuple")

        results = []
        for card in job_cards[:10]:
            title = card.query_selector("a.title").inner_text()
            company = card.query_selector("a.subTitle").inner_text()
            location = card.query_selector("li.location").inner_text()
            link = card.query_selector("a.title").get_attribute("href")
            results.append({
                "title": title, "company": company, "location": location,
                "url": link, "source": "naukri"
            })

        browser.close()
        return pd.DataFrame(results)
