from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_buttom = (By.ID, "login-button")

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_buttom).click()


class ProductAdd:
    def __init__(self, driver):
        self.driver = driver
        self.backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_button = (By.ID, "shopping_cart_container")

    def add(self):
        self.driver.find_element(*self.backpack).click()
        self.driver.find_element(*self.tshirt).click()
        self.driver.find_element(*self.onesie).click()

    def go_cart(self):
        self.driver.find_element(*self.cart_button).click()


class Checkout:
    def __init__(self, driver):
        self.driver = driver
        self.checkout = (By.ID, "checkout")

    def gocheck(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.checkout)).click()


class DeliveryForm:
    def __init__(self, driver):
        self.driver = driver
        self.first = (By.ID, "first-name")
        self.last = (By.ID, "last-name")
        self.zip = (By.ID, "postal-code")
        self.conbutton = (By.ID, "continue")
        self.total = (By.CLASS_NAME, "summary_total_label")

    def inputform(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first).send_keys(first_name)
        self.driver.find_element(*self.last).send_keys(last_name)
        self.driver.find_element(*self.zip).send_keys(zip_code)

    def contin(self):
        self.driver.find_element(*self.conbutton).click()

    def pricetotal(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.total))
        price = self.driver.find_element(*self.total)
        return price.text
