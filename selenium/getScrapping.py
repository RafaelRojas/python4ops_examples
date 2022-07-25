#!/usr/bin/env python3

from selenium import webdriver
import chromedriver_binary  
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://docs.python.org/3/tutorial/index.html#the-python-tutorial")
print(driver.find_element(by=By.XPATH, value="//div[@class= 'body']").text)
driver.close()


