from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import sys
import os

def _init_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--window-size=1920, 1080')
    chrome_options.add_argument('--start-maximized')
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")
    return webdriver.Chrome(options = chrome_options)


def get_amazon_search_url(query):
    return f"https://www.amazon.in/s?k={query.replace(' ', '+')}"

def scrape_amazon_results(search_term):
    driver = _init_driver(headless=True)
    print('Driver intiated')
    url = get_amazon_search_url(search_term)
    print('Got Amazon Search Url')
    driver.get(url)
    print('Visting Url')
    time.sleep(2)

    products = []

    results = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
    print("Found results")

    for item in results:
        try:
            title = item.find_element(By.XPATH, './/a/h2/span').text
        except:
            title = None

        try:
            price = item.find_element(By.XPATH, './/span[@class = "a-price-whole"]').text
        except:
            price = None

        try:
            rating_string = item.find_element(By.XPATH, './/a[contains(@aria-label,     "out of 5 stars")]').get_attribute('aria-label')
            rating = rating_string.split(',')[0]
        except:
            rating = None
        
        try:
            reviews = item.find_element(By.XPATH, './/span[@class = "a-size-base s-underline-text"]').text
        except:
            review = None

        product = {
            'Title':title,
            'Price':price,
            'Rating':rating,
            'Reviews':reviews
        }

        products.append(product)

    driver.quit()
    print('Found products')
    return products

def save_to_csv(data, filename="output/products.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("❌ Please provide a search term.")
        print("👉 Example: python scraper.py 'laptops'")
        sys.exit(1)

    search_term = sys.argv[1]
    print(f"🔍 Searching Amazon for {search_term}")
    scraped_data = scrape_amazon_results(search_term)
    save_to_csv(scraped_data)
    
    