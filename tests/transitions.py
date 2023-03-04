import sys
import allure
sys.path.insert(1, './pages')
from orderpage import OrderPage
from yandexpage import YandexPage

class TestTransitions:

    @allure.title('Переход на главную страницу')
    @allure.description('Кликаем на логотип самоката вверху страницы и переходим на главную')
    def test_transition_to_main_page_click_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        order_page.set_element_logo_scooter()
        order_page.check_transition_to_main_page()

    @allure.title('Переход на страницу Яндекса')
    @allure.description('Кликаем на надпись Яндекс вверху страницы и переходим на страницу Яндекса')
    def test_transition_to_yandex_page(self, driver):
        yandex_page = YandexPage(driver)
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        order_page.set_element_yandex()
        yandex_page.weit_for_load_yandex_page()
        yandex_page.chek_transition_to_yandex_page()

