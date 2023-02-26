import sys
import allure
import pytest
sys.path.insert(1, './pages')
from orderpage import OrderPage
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class TestOrderScooter:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        cls.driver = webdriver.Firefox(executable_path=r'C:\WebDriver\bin\geckodriver.exe', options=options)
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.order_page = OrderPage(cls.driver)

    @allure.title('Кнопка Заказать вверху страницы')
    @allure.description('В верхней части главной страницы ищем кнопку Заказать и кликаем на нее')
    def test_click_on_button_order_in_head(self):
        self.order_page.wait_for_load_main_page()
        self.order_page.set_element_button_order_in_head_on_main_page()
        self.order_page.check_transition_to_orderpage()

    @allure.title('Кнопка Заказать внизу страницы')
    @allure.description('В нижней части главной страницы ищем кнопку Заказать и кликаем на нее')
    def test_click_on_button_order_in_footer(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        self.order_page.wait_for_load_main_page()
        self.order_page.set_element_button_order_in_footer()
        self.order_page.check_transition_to_orderpage()

    @allure.title('Заполнение формы заказа')
    @allure.description('Заполняем форму заказа, которую видим после нажатия кнопки Заказать')
    @pytest.mark.parametrize('firstname, surname, address, metro, phonenumber, date, rental_periode, color, comment',
                             [['Иван', 'Иванов', 'г. Москва, ул Ленина 12-236', 'Черкизовская', 89052568936, '28',
                               'двое суток', 'серый', 'Зимняя резина'],
                              ['Петр', 'Петров', 'г. Москва, ул Далекая 12-237', 'Сокольники', 89062568938, '21',
                               'сутки', 'черный', 'Летняя резина']])
    def test_filling_user_by_order_for_who(self, firstname, surname, address, metro, phonenumber, date,
                                           rental_periode, color, comment):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')
        self.order_page.set_element_by_order_for_who(firstname, surname, address, metro, phonenumber)
        self.order_page.check_filling_order_for_who()
        self.order_page.set_element_by_order_about_rent(date, rental_periode, color, comment)
        self.order_page.check_order_complited()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()