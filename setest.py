from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
action = ActionChains(driver)
driver.get("http://127.0.0.1:8000/")
import time

driver.find_element_by_name('username').send_keys("revanth")
driver.find_element_by_name('password').send_keys("revanth")
driver.find_element_by_id('logsu').click()
time.sleep(10)
driver.find_element_by_link_text("Sign out").click()