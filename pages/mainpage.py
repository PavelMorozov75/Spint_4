from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from basepage import BasePageScooter

class MainPageLocators:

    LOGO_SCOOTER = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    HOW_MUCH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-0']")
    HOW_MUCH_ANSWER = (By.XPATH, "//div[@id= 'accordion__panel-0']/p")
    WANT_SOME_SCOOTERS_QUESTION = [By.XPATH, "//div[@id='accordion__heading-1']"]
    WANT_SOME_SCOOTERS_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-1']/p"]
    HOW_CALCULATE_RENTAL_TIME_QUESTION = [By.XPATH, "//div[@id='accordion__heading-2']"]
    HOW_CALCULATE_RENTAL_TIME_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-2']/p"]
    CAN_ORDER_TODAY_QUESTION = [By.XPATH, "//div[@id='accordion__heading-3']"]
    CAN_ORDER_TODAY_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-3']/p"]
    CAN_EXPEND_RETURN_EARLIER_QUESTION = [By.XPATH, "//div[@id='accordion__heading-4']"]
    CAN_EXPEND_RETURN_EARLIER_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-4']/p"]
    CHARGING_WITH_A_SCOOTER_QUESTION = [By.XPATH, "//div[@id='accordion__heading-5']"]
    CHARGING_WITH_A_SCOOTER_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-5']/p"]
    CAN_CANCEL_ORDER_QUESTION = [By.XPATH, "//div[@id='accordion__heading-6']"]
    CAN_CANCEL_ORDER_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-6']/p"]
    LIVE_FURTHER_THAN_MKAD_QUESTION = [By.XPATH, "//div[@id='accordion__heading-7']"]
    LIVE_FURTHER_THAN_MKAD_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-7']/p"]
    BUTTON_ORDER_IN_HEAD = [By.XPATH, "//button[@class='Button_Button__ra12g']"]
    BUTTON_ORDER_IN_FOOTER = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

class MainPageScooter(BasePageScooter):

    answers = {'how_much': 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
               'some_scooters': 'Пока что у нас так: один заказ — один самокат. ' \
                                  'Если хотите покататься с друзьями, можете просто сделать несколько заказов' \
                                  ' — один за другим.',
               'how_calculate': 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня.' \
                                  ' Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
                                  'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
               'can_order_today': 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
               'can_expend': 'Пока что нет! Но если что-то срочное — всегда можно позвонить' \
                                  ' в поддержку по красивому номеру 1010.',
               'charging_with_a_scooter': 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток' \
                                  ' — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
               'can_cancel': 'Да, пока самокат не привезли. Штрафа не будет, ' \
                                  'объяснительной записки тоже не попросим. Все же свои.',
               'further_than_mkad': 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'}


    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((MainPageLocators.LOGO_SCOOTER)))

    def set_element_how_much_on_main_page(self):
        self.set_element_by_main_page(*MainPageLocators.HOW_MUCH_QUESTION)

    def check_answer_for_how_much(self):
        self.check_element_by_main_page(*MainPageLocators.HOW_MUCH_QUESTION, *MainPageLocators.HOW_MUCH_ANSWER,
                                        self.answers['how_much'])
    def set_element_want_some_scooters_on_main_page(self):
        self.set_element_by_main_page(*MainPageLocators.WANT_SOME_SCOOTERS_QUESTION)

    def check_answer_for_want_some_scooters(self):
        self.check_element_by_main_page(*MainPageLocators.WANT_SOME_SCOOTERS_QUESTION,
                                        *MainPageLocators.WANT_SOME_SCOOTERS_ANSWER, self.answers['some_scooters'])

    def set_element_how_calculate_rental_time_on_main_page(self):
        self.set_element_by_main_page(*MainPageLocators.HOW_CALCULATE_RENTAL_TIME_QUESTION)

    def check_answer_for_how_calculate_rental_time(self):
        self.check_element_by_main_page(*MainPageLocators.HOW_CALCULATE_RENTAL_TIME_QUESTION,
                                        *MainPageLocators.HOW_CALCULATE_RENTAL_TIME_ANSWER,
                                        self.answers['how_calculate'])

    def set_element_can_i_order_today_on_main_page(self):
        self.set_element_by_main_page(*MainPageLocators.CAN_ORDER_TODAY_QUESTION)

    def check_answer_for_can_i_order_today(self):
        self.check_element_by_main_page(*MainPageLocators.CAN_ORDER_TODAY_QUESTION,
                                        *MainPageLocators.CAN_ORDER_TODAY_ANSWER,
                                        self.answers['can_order_today'])

    def set_element_can_expand_return_earlier_on_main_page(self):
        self.set_element_by_main_page(*MainPageLocators.CAN_EXPEND_RETURN_EARLIER_QUESTION)

    def check_answer_for_can_expand_return_earlier(self):
        self.check_element_by_main_page(*MainPageLocators.CAN_EXPEND_RETURN_EARLIER_QUESTION,
                                        *MainPageLocators.CAN_EXPEND_RETURN_EARLIER_ANSWER,
                                        self.answers['can_expend'])

    def set_element_charging_with_a_scooter_on_main_page(self):
        self.set_element_by_main_page(*MainPageLocators.CHARGING_WITH_A_SCOOTER_QUESTION)

    def check_answer_for_charging_with_a_scooter(self):
        self.check_element_by_main_page(*MainPageLocators.CHARGING_WITH_A_SCOOTER_QUESTION,
                                        *MainPageLocators.CHARGING_WITH_A_SCOOTER_ANSWER,
                                        self.answers['charging_with_a_scooter'])

    def set_element_can_cancel_order_on_main_page(self):
        self.set_element_by_main_page(*MainPageLocators.CAN_CANCEL_ORDER_QUESTION)

    def check_answer_for_can_cancel_order(self):
        self.check_element_by_main_page(*MainPageLocators.CAN_CANCEL_ORDER_QUESTION,
                                        *MainPageLocators.CAN_CANCEL_ORDER_ANSWER,
                                        self.answers['can_cancel'])

    def set_element_live_further_than_mkad_on_main_page(self):
        self.set_element_by_main_page(*MainPageLocators.LIVE_FURTHER_THAN_MKAD_QUESTION)

    def check_answer_for_live_further_than_mkad(self):
        self.check_element_by_main_page(*MainPageLocators.LIVE_FURTHER_THAN_MKAD_QUESTION,
                                        *MainPageLocators.LIVE_FURTHER_THAN_MKAD_ANSWER,
                                        self.answers['further_than_mkad'])

    def set_element_button_order_in_head_on_main_page(self):
        self.set_element_by_main_page(*MainPageLocators.BUTTON_ORDER_IN_HEAD)

    def set_element_button_order_in_footer(self):
        self.set_element_by_main_page(*MainPageLocators.BUTTON_ORDER_IN_FOOTER)

    def check_transition_to_orderpage(self):
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'