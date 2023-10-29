import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from datetime import datetime
from utilities.logger import Logger
import allure


class Account_page(Base):



    # Locators

    deposit = "//button[@ng-class='btnClass2']"       # Кнопка-меню "Deposit"
    withdrawl = "//button[@ng-class='btnClass3']"       # Кнопка "Withdrawl"
    transactions = "//button[@ng-class='btnClass1']"       # Кнопка "Transactions"
    amount = "//input[@type='number']"       # Поле для ввода суммы
    deposit_and_withdrawl_button = "//button[@type='submit']"       # Кнопка "Deposit" или "Withdrawl"
    message = "//span[@ng-show='message']"       # Сообщение
    balance = "//strong[.='0']"       # Значение поля баланс равно 0




    # Getters

    def get_deposit(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.deposit)))

    def get_withdrawl(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.withdrawl)))

    def get_transactions(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.transactions)))

    def get_amount(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.amount)))

    def get_deposit_and_withdrawl_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.deposit_and_withdrawl_button)))



    # Actions

    def click_deposit(self):
        self.get_deposit().click()
        print("Click Deposit Menu")

    def click_withdrawl(self):
        self.get_withdrawl().click()
        print("Click Withdrawl")

    def click_transactions(self):
        self.get_transactions().click()
        print("Click Transactions")

    def input_amount(self):
        self.get_amount().send_keys(self.fiba())
        print("Input Amount")

    def click_deposit_and_withdrawl_button(self):
        self.get_deposit_and_withdrawl_button().click()


    def click_buy_without_authorization_button(self):
        self.get_buy_without_authorization_button().click()
        print("Click Buy without authorization button")



    # Methods

    def select_deposit(self):
        with allure.step("select_deposit"):
            Logger.add_start_step(method="select_deposit")
            self.click_deposit()        # Нажимаем кнопку-меню "Deposit
            time.sleep(1)
            self.input_amount()        # Вводим сумму
            time.sleep(1)
            self.click_deposit_and_withdrawl_button()        # Нажимаем кнопку "Deposit
            print("Click Deposit Button")
            message_val = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.message))).text        # Парсим текст с собщения о пополнение депозита
            assert "Deposit Successful" == message_val        # Сравниваем, что спарсеное сообщение соответствует сообщению об успешном пополнение депозита
            print("Assert Deposit Successful")
            self.click_withdrawl()        # Нажимаем кнопку-меню "Withdrawl"
            time.sleep(1)
            self.input_amount()        # Вводим сумму
            time.sleep(1)
            self.click_deposit_and_withdrawl_button()        # Нажимаем кнопку "Withdrawl"
            print("Click Withdrawl Button")
            message_val = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.message))).text        # Парсим текст с собщения о снятие средств
            assert "Transaction successful" == message_val        # Сравниваем, что спарсеное сообщение соответствует сообщению об успешном снятие с депозита
            print("Assert Transaction successful")
            balance_zero = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.balance))).text        # Парсим нулевое значение баланса
            assert balance_zero == "0"        # Сравниваем значение баланса с 0
            print(f'Ваш баланс равен: {balance_zero}')
            time.sleep(2)
            self.click_transactions()        # Нажимаем кнопку-меню "Transactions"
            Logger.add_end_step(url=self.driver.current_url, method="select_deposit")


    def select_withdrawl(self):
        self.click_withdrawl()

    def select_transactions(self):
        self.click_transactions()

    def select_amount(self):
        self.input_amount()

    def select_deposit_and_withdrawl_button(self):
        self.click_deposit_and_withdrawl_button()


    def fiba(self):
        # Получаем сегодняшний день и прибавляем + 1
        data = datetime.now().day + 1
        # Вычисляем число Фибоначчи
        fib1 = fib2 = 1
        n = data
        while n >= 3:
            fib_sum = fib1 + fib2
            fib1 = fib2
            fib2 = fib_sum
            n -= 1
        return fib2