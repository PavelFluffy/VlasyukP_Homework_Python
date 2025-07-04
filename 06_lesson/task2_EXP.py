from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

input_box = driver.find_element(By.CLASS_NAME, "form-control")
blue_botton = driver.find_element(By.CLASS_NAME, "btn-primary")

input_box.send_keys("SkyPro")
blue_botton.click()
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element
                                ((By.CLASS_NAME, "btn-primary"), "SkyPro"))

print(blue_botton.text)
driver.quit
