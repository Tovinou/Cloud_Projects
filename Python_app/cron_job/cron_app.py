import time
from datetime import datetime
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    start = time.time()
    page.goto("https://example.com")
    load_time = time.time() - start
    with open("/data/results.log", "a") as f:
        f.write(f"{datetime.now()} - Load time: {load_time:.2f}s\n")
    browser.close()
