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


driver.find_element(By.XPATH, "//*[@id='post-36']/div/div[2]/div/div[2]/div[1]/div/a").click()

stylesheets = driver.find_elements(By.CSS_SELECTOR,"link[rel='stylesheet']")[::2]
for stylesheet in stylesheets:
    driver.execute_script("arguments[0].remove()", stylesheet)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='to-top']").click()
time.sleep(2)



driver.find_element(By.XPATH, "//*[@id='name']").send_keys(" Irakli")


checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.click()


color1 = driver.find_element(By.XPATH, "//*[@for='color1']").text
assert color1 == "Red", "Not Red"

color2 = driver.find_element(By.XPATH, "//*[@for='color2']").text
assert color2 == "Blue", "Not Blue"

color3 = driver.find_element(By.XPATH, "//*[@for='color3']").text
assert color3 == "Yellow", "Not Yellow"

color4 = driver.find_element(By.XPATH, "//*[@for='color4']").text
assert color4 == "Green", "Not Green"


driver.find_element(By.XPATH, "//*[@id='color5']").click()
#color5 = driver.find_element(By.XPATH, "//*[@for='color5']").text
#assert color5 == "Pink", "Not Pink"


driver.find_element(By.XPATH, "//*[@id='siblings']").click()

driver.find_element(By.XPATH, "//*[@id='siblings']/option[4]").click()


driver.find_element(By.XPATH, "//*[@id='email']").send_keys("irakli1@gmail.com")


driver.find_element(By.XPATH, "//*[@id='message']").send_keys(" hahah213")

element = driver.find_element(By.XPATH, "//*[@id='submit-btn']")
driver.execute_script("arguments[0].click();", element)


time.sleep(3)

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
text = alert.text
assert text == "Message received!", "Message not received!"
alert.accept()







