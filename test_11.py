import datetime
import time
import logging
from faker import Faker
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

driver.find_element(By.XPATH, "//*[@id='post-36']/div/div[2]/div/div[3]/div[4]/div/a").click()

try:
    pdf_url = "https://practice-automation.com/download/download-file/"
    pdf_normal_text_link = driver.find_element(By.XPATH, "//*[@id='post-1042']/div/div[1]/div/div/div/div[2]/h3/a")
    pdf_normal_text_link_value = pdf_normal_text_link.get_attribute("href")
    assert pdf_normal_text_link_value == pdf_url, "Error with text first link!"

    response_pdf = requests.get(pdf_url)
    if response_pdf.status_code == 200:
        print("A PDF file available for download")
    else:
        print("A PDF file not available for download")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='post-1042']/div/div[1]/div/div/div/div[3]/a")))

    docx_url = "https://practice-automation.com/download/file-download-form/"
    docx_normal_text_link = driver.find_element(By.XPATH, "//*[@id='post-1042']/div/div[3]/div/div/div/div[2]/h3/a")
    docx_normal_text_link_value = docx_normal_text_link.get_attribute("href")
    assert docx_normal_text_link_value == docx_url, "Error with text first link!"

    response_docx = requests.get(docx_url)
    if response_docx.status_code == 200:
        print("A DOCX file available for download")
    else:
        print("A DOCX file not available for download")

    docx_download_button = driver.find_element(By.XPATH, "//*[@id='post-1042']/div/div[3]/div/div/div/div[3]/a")
    docx_download_button.click()
    
    driver.switch_to.frame('wpdm-lock-frame')
    time.sleep(2)
    fake = Faker()
    random_word = fake.word()
    input_password = driver.find_element(By.CSS_SELECTOR, "[id^='password_']")
    input_password.send_keys(random_word)
    input_password.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element(By.XPATH,"//*[@id='msg_921']/div").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[id^='password_']"))
    )
    input_password.send_keys("automateNow")
    input_password.send_keys(Keys.ENTER)

except Exception as e:
    logging.error("An exception occurred: %s" % str(e))
    logging.exception("Full traceback:")

else:
    logging.info("The script executed successfully")

