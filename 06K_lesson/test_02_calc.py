import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    return WebDriverWait(driver, 50)


def test_calc(driver, wait):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    calc_wait = driver.find_element(By.CSS_SELECTOR, "#delay")
    calc_wait.clear()
    calc_wait.send_keys(45)

    driver.find_element(
        By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']"
        ).click()
    driver.find_element(
        By.XPATH,
        "//span[@class='operator btn btn-outline-success' and text()='+']"
        ).click()
    driver.find_element(
        By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']"
        ).click()
    driver.find_element(
        By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']"
        ).click()

    start_time = time.time()

    wait.until(EC.text_to_be_present_in_element((
        By.CLASS_NAME, "screen"), "15"))

    end_time = time.time()
    waiting_time = end_time - start_time
    assert 44 < waiting_time < 46

    result = driver.find_element(By.CLASS_NAME, "screen")
    assert result.text == "15"
