from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://uitestingplayground.com/textinput")

input_box = driver.find_element(By.CLASS_NAME, "form-control")
blue_botton = driver.find_element(By.CLASS_NAME, "btn-primary")

input_box.send_keys("SkyPro")
blue_botton.click()

print(blue_botton.text)
driver.quit
