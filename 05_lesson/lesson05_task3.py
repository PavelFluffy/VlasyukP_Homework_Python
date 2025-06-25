from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")
str = driver.find_element(By.CSS_SELECTOR, "input[type*='number']")
str.send_keys("Sky")
str.clear()
str.send_keys("Pro")
driver.quit()
