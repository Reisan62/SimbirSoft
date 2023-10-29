from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger
import allure


class Main_page(Base):

    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer_button'

    # Locators

    customer_button = "//button[@ng-click='customer()']"       # Кнопка "Customer Name"


    # Getters

    def get_customer_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.customer_button)))


    # Actions

    def click_customer_button(self):
        self.get_customer_button().click()
        print("Click Customer Login button")

    # Methods

    def select_customer_button(self):
        with allure.step("select_customer_button"):
            Logger.add_start_step(method="select_customer_button")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_customer_button()
            self.assert_url("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
            Logger.add_end_step(url=self.driver.current_url, method="select_customer_button")