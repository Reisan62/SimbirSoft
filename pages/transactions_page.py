import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
import csv
from utilities.logger import Logger
import allure
from datetime import datetime
import pandas as pd
from allure_commons.types import AttachmentType

class Transactions_page(Base):



    # Locators

    table_trans = "//table"       # Таблица транзакций


    # Getters


    # Actions


    # Methods

    def are_both_transactions_present(self):
        # Поиск всех элементов транзакций
        transactions = self.driver.find_elements(By.XPATH, "//table//tbody//tr")
        # Проверка, что найдено минимум 2 транзакции
        assert len(transactions) >= 2
        print(f"Количество транзакций равно: {len(transactions)}")

    def pars_table(self):
        with allure.step("pars_table"):
            Logger.add_start_step(method="pars_table")
            time.sleep(1)
            self.are_both_transactions_present()
            tablet_element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.table_trans)))
            # Получаем все строки (строки транзакций) в таблице
            rows = tablet_element.find_elements(By.TAG_NAME, "tr")
            formatted_csv_data = []     # Создаем пустой список для отформатированных данных транзакций
            # Перебираем строки транзакций
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")     # Находим ячейки в текущей строке
                row_data = [cell.text for cell in cells]     # Извлекаем текст из каждой ячейки

                date_time_str = row_data[0]     # Получаем строку с датой и временем транзакции из первой ячейки

                # Пытаемся преобразовать строку даты и времени в объект datetime
                try:
                    date_time_obj = datetime.strptime(date_time_str, '%b %d, %Y %I:%M:%S %p')
                    # Форматируем дату и время в нужный формат "ДД Месяц ГГГГ ЧЧ:ММ:СС"
                    formatted_date_time = date_time_obj.strftime("%d %B %Y %H:%M:%S")
                    # Добавляем отформатированную дату и время вместе с остальными данными в список
                    formatted_csv_data.append([formatted_date_time] + row_data[1:])
                except ValueError:
                    # Если преобразование даты и времени не удалось, добавляем исходные данные в список
                    formatted_csv_data.append(row_data)

            # Записываем отформатированные данные в CSV-файл
            with open('transactions.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(formatted_csv_data)
            print("Файл transactions.csv сформирован")
            # Дабавляем к файл к отчету Allure
            with open('transactions.csv', 'rb') as file:
                allure.attach(file.read(), name='transactions', attachment_type=AttachmentType.CSV)
            self.trans_rus()
            print("Файл transactions_rus.csv сформирован")
            Logger.add_end_step(url=self.driver.current_url, method="pars_table")


    def trans_rus(self):
        # Чтение данных из файла и переименование столбцов с использованием pandas
        df = pd.read_csv('transactions.csv')
        df = df.rename(columns={"Date-Time": "Дата-времяТранзакции", "Amount": "Сумма", "Transaction Type": "ТипТранзакции"})
        df.to_csv('transactions_rus.csv', index=False)
        # Дабавляем к файл к отчету Allure
        with open('transactions_rus.csv', 'rb') as file_rus:
            allure.attach(file_rus.read(), name='transactions_rus', attachment_type=AttachmentType.CSV)