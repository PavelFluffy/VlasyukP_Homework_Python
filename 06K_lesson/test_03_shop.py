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

    login_form = {
        "user-name": "standard_user",
        "password": "secret_sauce"
    }
    for field_login, value in login_form.items():
        field_auto = wait.until(EC.presence_of_element_located((
            By.ID, field_login)))
        field_auto.send_keys(value)

    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.presence_of_all_elements_located((
        By.CLASS_NAME, "inventory_item_description")))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.ID, "shopping_cart_container").click()

    wait.until(EC.presence_of_element_located((
        By.ID, "checkout"))).click()

    delivery_form = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "postalCode": "140140",
    }
    for field_name, value in delivery_form.items():
        field = wait.until(EC.presence_of_element_located((
            By.NAME, field_name)))
        field.send_keys(value)

    driver.find_element(By.ID, "continue").click()

    price_total = wait.until(EC.presence_of_element_located((
        By.CLASS_NAME, "summary_total_label")))
    assert price_total.text == "Total: $58.29"
