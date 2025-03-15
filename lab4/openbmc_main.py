from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
import time

#--------------------------------
# defines
driver=None


#--------------------------------
# functions
def startWork(_adress):
	global driver

	if driver!=None:
		driver.quit()

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
	time.sleep(5)

def getTitle():
	global driver

	if driver==None:
		return

	return driver.title


#-------------------------------
# defines 2
chromedriver_path="/usr/bin/chromedriver"

options=webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-blink-features=AutomationControlled')
service=ChromeService(executable_path=chromedriver_path)