import sys
import allure
sys.path.insert(1, './pages')
from mainpage import MainPageScooter
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class TestAccordionInMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        cls.driver = webdriver.Firefox(executable_path=r'C:\WebDriver\bin\geckodriver.exe', options=options)
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.scooter_page = MainPageScooter(cls.driver)

    @allure.title('Сколько стоит и как оплатить')
    @allure.description('На странице ищем элемент аккордеона Сколько стоит и как оплатить и кликаем на него')
    def test_click_on_how_much(self):
        self.scooter_page.wait_for_load_main_page()
        self.scooter_page.set_element_how_much_on_main_page()
        self.scooter_page.check_answer_for_how_much()

    @allure.title('Хочу сразу несколько самокатов! Так можно?')
    @allure.description('На странице ищем элемент аккордеона Хочу сразу несколько самокатов! Так можно? '
                        'и кликаем на него')
    def test_click_on_want_some_scooters(self):
        self.scooter_page.set_element_want_some_scooters_on_main_page()
        self.scooter_page.check_answer_for_want_some_scooters()

    @allure.title('Как рассчитывается время аренды?')
    @allure.description('На странице ищем элемент аккордеона Как рассчитывается время аренды? и кликаем на него')
    def test_click_on_how_calculate_rental_time(self):
        self.scooter_page.set_element_how_calculate_rental_time_on_main_page()
        self.scooter_page.check_answer_for_how_calculate_rental_time()

    @allure.title('Можно ли заказать самокат прямо на сегодня?')
    @allure.description('На странице ищем элемент аккордеона Можно ли заказать самокат прямо на сегодня? '
                        'и кликаем на него')
    def test_click_on_can_i_order_today(self):
        self.scooter_page.set_element_can_i_order_today_on_main_page()
        self.scooter_page.check_answer_for_can_i_order_today()

    @allure.title('Можно ли продлить заказ или вернуть самокат раньше?')
    @allure.description('На странице ищем элемент аккордеона Можно ли продлить заказ или вернуть самокат раньше? '
                        'и кликаем на него')
    def test_click_on_can_expent_reurn_earlier(self):
        self.scooter_page.set_element_can_expand_return_earlier_on_main_page()
        self.scooter_page.check_answer_for_can_expand_return_earlier()

    @allure.title('Вы привозите зарядку вместе с самокатом?')
    @allure.description('На странице ищем элемент аккордеона Вы привозите зарядку вместе с самокатом? '
                        'и кликаем на него')
    def test_click_on_charging_with_a_scooter(self):
        self.scooter_page.set_element_charging_with_a_scooter_on_main_page()
        self.scooter_page.check_answer_for_charging_with_a_scooter()

    @allure.title('Можно ли отменить заказ?')
    @allure.description('На странице ищем элемент аккордеона Можно ли отменить заказ? '
                        'и кликаем на него')
    def test_click_on_can_cancel_order(self):
        self.scooter_page.set_element_can_cancel_order_on_main_page()
        self.scooter_page.check_answer_for_can_cancel_order()

    @allure.title('Я живу за МКАДом, привезёте?')
    @allure.description('На странице ищем элемент аккордеонаЯ живу за МКАДом, привезёте? '
                        'и кликаем на него')
    def test_click_on_live_further_than_mkad(self):
        self.scooter_page.set_element_live_further_than_mkad_on_main_page()
        self.scooter_page.check_answer_for_live_further_than_mkad()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

