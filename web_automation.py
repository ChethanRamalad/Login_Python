import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

element = driver.find_element(By.ID, "username")
element.send_keys("student")

element = driver.find_element(By.ID, "password")
element.send_keys("Password123")

element = driver.find_element(By.XPATH, "submit")
element.click() 

time.sleep(10)
