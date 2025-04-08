from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import tempfile

chromedriver_path="/bin/chromedriver"
user_data_dir=tempfile.mkdtemp()

options=webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument(f"--user-data-dir={user_data_dir}")
service=ChromeService(executable_path=chromedriver_path)

driver=webdriver.Chrome(service=service,options=options)
driver.get("https://127.0.0.1:2443")
print(driver.title)
driver.quit()