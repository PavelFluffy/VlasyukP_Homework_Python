from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))

imgs = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

print(imgs[2].get_attribute("src"))

driver.quit()
