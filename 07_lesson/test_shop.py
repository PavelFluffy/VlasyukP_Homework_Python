import pytest
from selenium import webdriver
from page_shop import LoginPage
from page_shop import ProductAdd
from page_shop import Checkout
from page_shop import DeliveryForm


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_shop(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    ProductAdd(driver).add()
    ProductAdd(driver).go_cart()
    Checkout(driver).gocheck()
    DeliveryForm(driver).inputform("Ivan", "Ivanov", "123456")
    DeliveryForm(driver).contin()
    DeliveryForm(driver).pricetotal()

    assert DeliveryForm(driver).pricetotal() == "Total: $58.29"
