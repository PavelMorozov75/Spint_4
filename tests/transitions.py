import sys
import allure
import pytest
sys.path.insert(1, './pages')
from orderpage import OrderPage
from yandexpage import YandexPage
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class TestTransitions:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        cls.driver = webdriver.Firefox(executable_path=r'C:\WebDriver\bin\geckodriver.exe', options=options)
        cls.driver.get('https://qa-scooter.praktikum-services.ru/order')
        cls.order_page = OrderPage(cls.driver)
        cls.yandex_page = YandexPage(cls.driver)

    @allure.title('Переход на главную страницу')
    @allure.description('Кликаем на логотип самоката вверху страницы и переходим на главную')
    def test_transition_to_main_page_click_logo(self):
        self.order_page.set_element_logo_scooter()
        self.order_page.check_transition_to_main_page()

    @allure.title('Переход на страницу Яндекса')
    @allure.description('Кликаем на надпись Яндекс вверху страницы и переходим на страницу Яндекса')
    def test_transition_to_yandex_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')
        self.driver.implicitly_wait(7)
        self.order_page.set_element_yandex()
        self.yandex_page.weit_for_load_yandex_page()
        self.yandex_page.chek_transition_to_yandex_page()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()