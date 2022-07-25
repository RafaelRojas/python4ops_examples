#!/usr/bin/env python3


# Importing necessary modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# WebDriver Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
  
# Target URL
driver.get("https://docs.python.org/3/tutorial/index.html#the-python-tutorial")
  
# print(driver.title)
  
# Printing the whole body text
print(driver.find_element(by=By.XPATH, value="//div[@class= 'body']").text)
  
# Closing the driver
driver.close()