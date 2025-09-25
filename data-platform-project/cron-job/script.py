# Cron-jobb med Playwright

from playwright.sync_api import sync_playwright
import time
import json
from datetime import datetime

def measure_load_time(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        start_time = time.time()
        page.goto(url)
        load_time = time.time() - start_time
        
        browser.close()
        
        return load_time

def main():
    url = "https://example.com"
    load_time = measure_load_time(url)
    
    result = {
        "timestamp": datetime.now().isoformat(),
        "url": url,
        "load_time_seconds": load_time
    }
    
    # Save result to file
    with open("/data/load_times.json", "a") as f:
        f.write(json.dumps(result) + "\n")
    
    print(f"Load time for {url}: {load_time:.2f} seconds")

if __name__ == "__main__":
    main()