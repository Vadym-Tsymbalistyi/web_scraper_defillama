import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

BASE_URL = 'https://defillama.com/chains'

def scrape_page(driver):
    data = []
    try:
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[style*='translateY']"))
        )
        data = _scroll_page(driver)
    except Exception as e:
        logging.error(f"Error while scraping page: {e}")
    return data

def _scroll_page(driver):
    scroll_step = 500
    current_position = 100
    last_height = driver.execute_script("return document.body.scrollHeight")
    logging.info("Starting to scroll the page...")

    collected_data = []

    while current_position < last_height:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(0.01)
        current_position += scroll_step
        last_height = driver.execute_script("return document.body.scrollHeight")

        elements = driver.find_elements(By.CSS_SELECTOR, "div[style*='translateY']")
        collected_data.extend(_get_elements(elements))

    return collected_data

def _get_elements(elements):
    extracted = []
    for element in elements:
        try:
            cells = element.find_elements(By.CSS_SELECTOR, "div[data-chainpage='true']")
            raw_data = [cell.text.strip() for cell in cells]

            number, name = raw_data[0].split("\n") if '' not in raw_data[0].split("\n") else (None, None)
            protocols = raw_data[1] if len(raw_data) > 1 else None
            tvl = raw_data[4] if len(raw_data) > 4 else None

            extracted.append({
                'Name': name,
                'Protocols': protocols,
                'TVL': tvl
            })
            logging.info(f"Updated data: 'Name': {name}, 'Protocols': {protocols}, 'TVL': {tvl}.")
        except Exception as e:
            logging.error(f"Error processing element: {e}")
    return extracted
