import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

element = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/div[1]/input")
element.send_keys("student")

element = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/div[2]/input")
element.send_keys("Password123")

element = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/button")
element.click() 

time.sleep(10)
