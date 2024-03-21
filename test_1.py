import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import json





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
styles = driver.find_elements(By.CSS_SELECTOR, "style")
for style in styles:
    driver.execute_script("arguments[0].parentNode.removeChild(arguments[0])", style)

driver.find_element(By.XPATH, "//*[@id='post-36']/div/div[2]/div/div[1]/div[1]/div/a").click()

driver.find_element(By.XPATH, "//*[@id='start']").click()


counter_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='delay']"))  
)

counter_value = counter_element.text

expected_value = "Liftoff!"
WebDriverWait(driver, 10).until(
    lambda driver: counter_value == expected_value
)

print(counter_value)


