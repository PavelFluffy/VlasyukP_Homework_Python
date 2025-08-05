from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class PageCalc:
    def __init__(self, driver):
        """
        Конструктор класса CalcMainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
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

    @allure.step("Установка задержки {query} секунд")
    def calcwait(self, query):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param query: int — время задержки в секундах.
        """
        calcwaitelement = self.driver.find_element(*self.wait)
        calcwaitelement.clear()
        calcwaitelement.send_keys(query)

    @allure.step("Нажатие кнопки button")
    def calcinput(self, button_text):
        """
        Нажимает на кнопку калькулятора.

        :param button_text: str — текст на кнопке, которую нужно нажать.
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    @allure.step("Получение результата после ожидания")
    def getresult(self, timeout=45) -> int:
        """
        Ожидает 45 секунд и получает результат.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result, "15"))
        result = self.driver.find_element(*self.result)
        return result.text
