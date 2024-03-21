import datetime
import time
import logging
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import json

logging.basicConfig(filename='selenium_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

options = Options()
options.add_argument("--no-sandbox")
#options.add_argument("headless") # without browser
options.add_argument("--disable-gpu")
options.add_argument('--disable-extensions')
options.add_argument("--disable-webgl")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-features=NetworkService")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
)

options.add_argument(r"--user-data-dir=C:\Users\irakl.IRAKLI-USER1324\AppData\Local\Google\Chrome\User Data")

options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome( options=options)

driver.get("https://practice-automation.com/")

response = requests.get("http://example.com")

if response.status_code == 200:
    print("No problemo!")
else:
    print(f"Problemo: {response.status_code}")

stylesheets = driver.find_elements(By.CSS_SELECTOR,"link[rel='stylesheet']")[::2]
for stylesheet in stylesheets:
    driver.execute_script("arguments[0].remove()", stylesheet)

driver.execute_script("window.scrollBy(0, 250);")

driver.find_element(By.XPATH, "//*[@id='post-36']/div/div[2]/div/div[1]/div[3]/div/a").click()

try:
    items = ["Oranges", "Laptop", "Marbles"]
    
    prices = ["$3.99", "$1200.00", "$1.25"]

    for i, item in enumerate(items, start=2):
        actual_item = driver.find_element(By.XPATH, f"//*[@id='post-1076']/div/figure/table/tbody/tr[{i}]/td[1]").text
        assert actual_item == item, f"Wrong value in table. Expected: {item}, Actual: {actual_item}"

    for i, price in enumerate(prices, start=2):
        actual_price = driver.find_element(By.XPATH, f"//*[@id='post-1076']/div/figure/table/tbody/tr[{i}]/td[2]").text
        assert actual_price == price, f"Wrong value in table. Expected: {price}, Actual: {actual_price}"


    sort_tables = driver.find_element(By.XPATH, "//*[@id='tablepress-1_length']/label/select")

    select = Select(sort_tables)
    select.select_by_index(1) 
    time.sleep(4)
    last_column= driver.find_element(By.XPATH, "//*[@id='tablepress-1']/tbody/tr[25]/td[1]").text
    assert last_column == "25", "Error with last column"

    driver.find_element(By.XPATH, "//*[@id='tablepress-1_filter']/label/input").send_keys("Bangladesh")
    assert driver.find_element(By.XPATH, "//*[@id='tablepress-1']/tbody/tr/td[2]").text == "Bangladesh", "It's not Bangladesh"

except Exception as e:
    logging.error("An exception occurred: %s" % str(e))

else:
    logging.info("The script executed successfully")

