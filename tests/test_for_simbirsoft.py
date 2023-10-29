from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.main_page import Main_page
from pages.login_page import Login_page
from pages.account_page import Account_page
from pages.transactions_page import Transactions_page
import allure
from selenium.webdriver.common.keys import Keys
import pytest




# g = Service('C:\\Users\\baldy\\PycharmProjects\\resource\\chromedriver.exe')       # Путь к вашему chromedriver
@allure.description("Test Simbirsoft")
def test_simbirsoft(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = "none"
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors-spki-list')
    # driver = webdriver.Chrome(options=options, service=g)       # Локальный драйвер
    # Запуск через Selenium Grid
    command_executor = "http://localhost:4444/wd/hub"
    driver = webdriver.Remote(options=options, command_executor=command_executor)

    mp = Main_page(driver)
    mp.select_customer_button()

    lp = Login_page(driver)
    lp.login()

    ac = Account_page(driver)
    ac.select_deposit()

    trp = Transactions_page(driver)
    trp.pars_table()

    driver.quit()