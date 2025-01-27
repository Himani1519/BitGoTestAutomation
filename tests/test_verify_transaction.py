import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.verify_transaction_page import Transactions

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(
        'C:\\Users\\Admin\\Desktop\\BitGo\\driver\\chromedriver.exe'),
        options=options)
    yield driver
    driver.quit()

def test_verify_transaction_heading(driver):
    transactions = Transactions(driver)
    transactions.open_url()
    heading_text = transactions.verify_section_heading()
    assert heading_text == '25 of 2875 Transactions'


def test_verify_each_hash(driver):
    transactions = Transactions(driver)
    transactions.open_url()
    all_hash_values = transactions.verify_each_transaction()
    print(all_hash_values)