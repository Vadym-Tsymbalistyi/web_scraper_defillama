import time
import random
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

# TODO: move to app config
BASE_URL = 'https://defillama.com/chains'


class Scraper:
    def __init__(self, proxies):
        self.__logger = logging.getLogger("Scraper")
        self.__webdriver = self.__create_webdriver(proxies)

    def __create_webdriver(self, proxies):
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
            self.__logger.info(f"Using proxy: {proxy}")

        self.__logger.info("Initializing Chrome WebDriver...")
        try:
            return webdriver.Chrome(options=options)
        except Exception as e:
            self.__logger.error(f"Error initializing Chrome WebDriver: {e}")
            raise

    def scrape_page(self):
        try:
            self.__webdriver.get(BASE_URL)
            WebDriverWait(self.__webdriver, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[style*='translateY']"))
            )
            return self.scroll_page_and_extract_data()

        except Exception as e:
            self.__logger.error(f"Error while scraping page: {e}")
            raise

    def scroll_page_and_extract_data(self):
        scroll_step = 500
        current_position = 100
        last_height = self.__webdriver.execute_script("return document.body.scrollHeight")
        self.__logger.info("Starting to scroll the page...")

        collected_data = []

        while current_position < last_height:
            self.__logger.debug(f"current_position: {current_position}")

            self.__webdriver.execute_script(f"window.scrollTo(0, {current_position});")
            time.sleep(0.01)
            current_position += scroll_step
            last_height = self.__webdriver.execute_script("return document.body.scrollHeight")

            elements = self.__webdriver.find_elements(By.CSS_SELECTOR, "div[style*='translateY']")
            collected_data.extend(self.extract_data(elements))

        return collected_data

    def extract_data(self, elements):
        extracted = []
        for element in elements:
            try:
                cells = element.find_elements(By.CSS_SELECTOR, "div[data-chainpage='true']")
                raw_data = [cell.text.strip() for cell in cells]
                self.__logger.debug(f"raw data extracted: {raw_data}")

                number, name = raw_data[0].split("\n") if '' not in raw_data[0].split("\n") else (None, None)
                protocols = raw_data[1] if len(raw_data) > 1 else None
                tvl = raw_data[4] if len(raw_data) > 4 else None

                extracted.append({
                    'Name': name,
                    'Protocols': protocols,
                    'TVL': tvl
                })
                self.__logger.debug(f"Updated data: 'Name': {name}, 'Protocols': {protocols}, 'TVL': {tvl}.")
            except StaleElementReferenceException:
                self.__logger.debug("Page data was updated during the scraping. Skipping it ...")

            except Exception as e:
                self.__logger.error(f"Error processing element: {e}")
                raise

        return extracted

    def stop(self):
        if self.__webdriver:
            self.__webdriver.quit()
