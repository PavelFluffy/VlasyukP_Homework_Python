from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageCalc:
    def __init__(self, driver):
        self.driver = driver
        self.wait = (By.CSS_SELECTOR, "#delay")
        self.num7 = (
            By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']"
            )
        self.num8 = (
            By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']"
            )
        self.numsum = (
            By.XPATH, "//span[@class='operator btn btn-outline-success' and "
            "text()='+']")
        self.numres = (
            By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']"
            )
        self.result = (By.CLASS_NAME, "screen")

    def calcwait(self, query):
        calcwaitelement = self.driver.find_element(*self.wait)
        calcwaitelement.clear()
        calcwaitelement.send_keys(query)

    def calcinput(self, button_text):
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    def getresult(self, timeout=45):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result, "15"))
        result = self.driver.find_element(*self.result)
        return result.text
