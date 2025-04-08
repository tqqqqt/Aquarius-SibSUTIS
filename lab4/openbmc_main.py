from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import tempfile

#--------------------------------
# defines
driver=None


#--------------------------------
# functions
def startWork(_adress):
	global driver

	if driver!=None:
		driver.quit()

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
	driver.get(_adress)

def endWork():
	if driver==None:
		return

	driver.quit()

def loginServer(_user_name, _user_pass):
	if driver==None:
		return

	user_name_field=driver.find_element(By.ID,"username")
	user_name_field.send_keys(_user_name)

	password_field=driver.find_element(By.ID,"password")
	password_field.send_keys(_user_pass)

	enter_button=driver.find_element(By.CSS_SELECTOR,'[data-test-id="login-button-submit"]')
	enter_button.click()

	# need wait to update page
	time.sleep(10)

def getTitle():
	global driver

	if driver==None:
		return

	return driver.title