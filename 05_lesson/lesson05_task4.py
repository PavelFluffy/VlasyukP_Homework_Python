from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
text = driver.find_element(By.ID, "flash")
print(text.text)
driver.quit()
