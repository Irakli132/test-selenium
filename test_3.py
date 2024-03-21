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
    driver.execute_script("arguments[0].remove()", style)



driver.find_element(By.XPATH, "//*[@id='post-36']/div/div[2]/div/div[3]/div[1]/div/a").click()


element = driver.find_element(By.XPATH, "//*[@id='alert']")
driver.execute_script("arguments[0].click();", element)

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
text = alert.text
assert text == "Hi there, pal!", "Not Hi"
alert.accept()


element = driver.find_element(By.XPATH, "//*[@id='confirm']")
driver.execute_script("arguments[0].click();", element)

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
text = alert.text
assert text == "OK or Cancel, which will it be?", "No one"
alert.dismiss()

label_dissmiss = driver.find_element(By.XPATH, "//*[@id='confirmResult']").text
assert label_dissmiss == "Cancel it is!", "Not Cancel!"


driver.execute_script("arguments[0].click();", element)
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
text = alert.text
assert text == "OK or Cancel, which will it be?", "No one"
alert.accept()

label_accept = driver.find_element(By.XPATH, "//*[@id='confirmResult']").text
assert label_accept == "OK it is!", "Not OK"


driver.find_element(By.XPATH, "//*[@id='prompt']").click()

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
text = alert.text
assert text == "Hi there, what's your name?", "Wrong sentence!"
alert = driver.switch_to.alert
alert.send_keys("")
alert.accept()

text = driver.find_element(By.XPATH, "//*[@id='promptResult']").text
assert text == "Fine, be that way...", "Not Fine"

driver.find_element(By.XPATH, "//*[@id='prompt']").click()

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
text = alert.text
assert text == "Hi there, what's your name?", "Wrong sentence!"
alert = driver.switch_to.alert
name_of_user = "ika1@*&%"
alert.send_keys(name_of_user)
alert.accept()
text_of_user = driver.find_element(By.XPATH, "//*[@id='promptResult']").text
print(text_of_user)
assert text_of_user == f"Nice to meet you, {name_of_user}!", "Who are you?"

