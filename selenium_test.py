from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
import time

chromedriver_path="/bin/chromedriver"

options=webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-blink-features=AutomationControlled')
service=ChromeService(executable_path=chromedriver_path)

driver=webdriver.Chrome(service=service,options=options)
driver.get("https://127.0.0.1:2443")
print(driver.title)
driver.quit()