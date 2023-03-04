from selenium.webdriver.common.by import By

class YandexPage:
    SEARCH_LINE = [By.XPATH, "//input[@class='arrow__input mini-suggest__input']"]

    def __init__(self, driver):
        self.driver = driver

    def weit_for_load_yandex_page(self):
        self.driver.implicitly_wait(5)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def chek_transition_to_yandex_page(self):
       assert len(self.driver.window_handles) == 2

