import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Transactions:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_url(self):
        self.driver.get("https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732")

    def verify_section_heading(self):
        values = self.driver.find_element(By.XPATH, '//h3[@class="font-h3"]')
        return values.text

    def verify_each_transaction(self):
        hash_values = []
        hash_values.append(self.get_hash_value())

        for _ in range(24):  # Navigate through 24 pages
            wait = WebDriverWait(self.driver, 10)
            next_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[span[text()='Next']]"))
            )
            next_button.click()
            hash_values.append(self.get_hash_value())

        return hash_values

    def get_hash_value(self):
        wait = WebDriverWait(self.driver, 30)
        hash_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@class="text-gray"]'))
        )
        return hash_element.text
