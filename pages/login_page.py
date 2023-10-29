import time
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger



class Login_page(Base):



    # Locators

    names = "//select[@id='userSelect']"       # Меню "Your name"
    harry = "//option [.='Harry Potter']"       # Выбор логина "Harry Potter"
    login_button = "//button[@class='btn btn-default']"       # Кнопка "Login"


    # Getters

    def get_names(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.names)))

    def get_harry(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.harry)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))


    # Actions

    def click_names(self):
        self.get_names().click()
        print("Click Your names")

    def click_harry(self):
        self.get_harry().click()
        print("Select Harry Potter")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login button")


    # Methods

    def login(self):
        with allure.step("login"):
            Logger.add_start_step(method="login")
            self.click_names()
            self.click_harry()
            self.click_names()
            time.sleep(2)
            self.click_login_button()
            Logger.add_end_step(url=self.driver.current_url, method="login")

    def select_harry(self):
        self.click_harry()


    def select_login(self):
        self.click_login()