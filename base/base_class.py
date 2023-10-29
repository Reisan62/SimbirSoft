

class Base():
    def __init__(self, driver):
        self.driver = driver



    """Method get current url"""

    def get_current_url(self):       # Получаем текущую URL
        get_url = self.driver.current_url
        print("Current url " + get_url)


    """Method assert url"""

    def assert_url(self, result):       # Производим сравнение URL
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")