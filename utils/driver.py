import random
import logging
from selenium import webdriver

def create_driver(proxies):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--enable-automation')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")

    if proxies:
        proxy = random.choice(proxies)
        options.add_argument(f'--proxy-server={proxy}')
        logging.info(f"Using proxy: {proxy}")

    logging.info("Initializing Chrome WebDriver...")
    try:
        return webdriver.Chrome(options=options)
    except Exception as e:
        logging.error(f"Error initializing Chrome WebDriver: {e}")
        return None
