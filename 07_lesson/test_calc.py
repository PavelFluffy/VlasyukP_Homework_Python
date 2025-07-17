import pytest
from selenium import webdriver
from page_calc import PageCalc


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
    yield driver
    driver.quit()


def test_calc(driver):
    page = PageCalc(driver)
    page.calcwait("45")
    page.calcinput("7")
    page.calcinput("+")
    page.calcinput("8")
    page.calcinput("=")
    result = page.getresult()
    assert result == "15"
