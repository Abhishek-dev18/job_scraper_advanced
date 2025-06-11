import pandas as pd
from playwright.sync_api import sync_playwright
from proxy_utils import get_proxy

def scrape_ziprecruiter():
    proxy = get_proxy()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, proxy={"server": proxy} if proxy else None)
        page = browser.new_page()
        page.goto("https://www.ziprecruiter.com/candidate/search?search=software+engineer&location=India", timeout=60000)

        page.wait_for_selector(".job_content", timeout=10000)
        job_cards = page.query_selector_all(".job_content")

        results = []
        for card in job_cards[:10]:
            title = card.query_selector(".job_title").inner_text()
            company = card.query_selector(".company_name").inner_text()
            location = card.query_selector(".location").inner_text()
            link = card.query_selector("a").get_attribute("href")
            results.append({
                "title": title, "company": company, "location": location,
                "url": link, "source": "ziprecruiter"
            })

        browser.close()
        return pd.DataFrame(results)
