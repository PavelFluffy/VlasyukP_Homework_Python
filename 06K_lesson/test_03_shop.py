import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    return WebDriverWait(driver, 10)


def test_shop(driver, wait):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.ID, "shopping_cart_container").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.NAME, "firstName").send_keys("Иван")
    driver.find_element(By.NAME, "lastName").send_keys("Иванов")
    driver.find_element(By.NAME, "postalCode").send_keys("140140")
    driver.find_element(By.ID, "continue").click()

    price_total = wait.until(EC.presence_of_element_located((
        By.CLASS_NAME, "summary_total_label")))
    print(price_total.text)
    assert price_total.text == "Total: $58.29"
