from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import keyboard
# exec_path_chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
exec_path_driver = "C:/Users/MoonOrchid/Desktop/test3/cookieclickerautomatic/chromedriver.exe"

options = webdriver.ChromeOptions() 

options.add_argument('--user-data-dir=C:/Users/MoonOrchid/AppData/Local/Google/Chrome/User Data')

options.add_argument('--profile-directory=Profile 1')
driver = webdriver.Chrome(executable_path = exec_path_driver, options = options) #Chrome_Options is deprecated. So we use options instead.

driver.get("https://orteil.dashnet.org/cookieclicker/")
# while
# driver.find_element_by_id("bigCookie").click()
bb=driver.find_element_by_id("shimmers")

def function():

	# if keyboard.is_pressed("up arrow"):  # if key 'q' is pressed 
	running=True
	aa=driver.find_element_by_id("bigCookie")
	while(True):
		if keyboard.is_pressed("²"):
			running=True
			time.sleep(0.2)
		while(running):
			try:
				bb.find_element_by_css_selector('[alt="Golden cookie"]').click()
			except:
				pass
			try:
				bb.find_element_by_css_selector('[alt="Wrath cookie"]').click()
			except:
				pass
			try:
				bb.find_element_by_css_selector('[alt="Reindeer"]').click()
			except:
				pass
			try:
				aa.click()
			except:
				pass
			if keyboard.is_pressed("²"):
				running=False
				time.sleep(0.2)

t1 = Thread(target=function)
t1.start()