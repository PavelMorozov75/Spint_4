from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class MainPageScooter:

    LOGO_SCOOTER = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    HOW_MUCH_QUESTION = [By.XPATH, "//div[@id='accordion__heading-0']"]
    HOW_MUCH_ANSWER = [By.XPATH, "//div[@id= 'accordion__panel-0']/p"]
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

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((self.LOGO_SCOOTER)))

    def set_element_how_much_on_main_page(self):
        element = self.driver.find_element(*self.HOW_MUCH_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((self.HOW_MUCH_QUESTION)))
        element.click()

    def check_answer_for_how_much(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((self.HOW_MUCH_ANSWER)))
        question = self.driver.find_element(*self.HOW_MUCH_QUESTION)
        answer = self.driver.find_element(*self.HOW_MUCH_ANSWER)
        assert question.get_attribute('aria-expanded') == "true"  \
               and answer.text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'\

    def set_element_want_some_scooters_on_main_page(self):
        element = self.driver.find_element(*self.WANT_SOME_SCOOTERS_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((self.WANT_SOME_SCOOTERS_QUESTION)))
        element.click()

    def check_answer_for_want_some_scooters(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((self.WANT_SOME_SCOOTERS_ANSWER)))
        question = self.driver.find_element(*self.WANT_SOME_SCOOTERS_QUESTION)
        answer = self.driver.find_element(*self.WANT_SOME_SCOOTERS_ANSWER)
        assert question.get_attribute('aria-expanded') == "true"  \
               and answer.text == 'Пока что у нас так: один заказ — один самокат. ' \
                                  'Если хотите покататься с друзьями, можете просто сделать несколько заказов' \
                                  ' — один за другим.'

    def set_element_how_calculate_rental_time_on_main_page(self):
        element = self.driver.find_element(*self.HOW_CALCULATE_RENTAL_TIME_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((self.HOW_CALCULATE_RENTAL_TIME_QUESTION)))
        element.click()

    def check_answer_for_how_calculate_rental_time(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((self.HOW_CALCULATE_RENTAL_TIME_ANSWER)))
        question = self.driver.find_element(*self.HOW_CALCULATE_RENTAL_TIME_QUESTION)
        answer = self.driver.find_element(*self.HOW_CALCULATE_RENTAL_TIME_ANSWER)
        assert question.get_attribute('aria-expanded') == "true"  \
               and answer.text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня.' \
                                  ' Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
                                  'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    def set_element_can_i_order_today_on_main_page(self):
        element = self.driver.find_element(*self.CAN_ORDER_TODAY_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((self.CAN_ORDER_TODAY_QUESTION)))
        element.click()

    def check_answer_for_can_i_order_today(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((self.CAN_ORDER_TODAY_ANSWER)))
        question = self.driver.find_element(*self.CAN_ORDER_TODAY_QUESTION)
        answer = self.driver.find_element(*self.CAN_ORDER_TODAY_ANSWER)
        assert question.get_attribute('aria-expanded') == "true" \
               and answer.text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def set_element_can_expand_return_earlier_on_main_page(self):
        element = self.driver.find_element(*self.CAN_EXPEND_RETURN_EARLIER_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((self.CAN_EXPEND_RETURN_EARLIER_QUESTION)))
        element.click()

    def check_answer_for_can_expand_return_earlier(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((self.CAN_EXPEND_RETURN_EARLIER_ANSWER)))
        question = self.driver.find_element(*self.CAN_EXPEND_RETURN_EARLIER_QUESTION)
        answer = self.driver.find_element(*self.CAN_EXPEND_RETURN_EARLIER_ANSWER)
        assert question.get_attribute('aria-expanded') == "true" \
               and answer.text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить' \
                                  ' в поддержку по красивому номеру 1010.'


    def set_element_charging_with_a_scooter_on_main_page(self):
        element = self.driver.find_element(*self.CHARGING_WITH_A_SCOOTER_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((self.CHARGING_WITH_A_SCOOTER_QUESTION)))
        element.click()

    def check_answer_for_charging_with_a_scooter(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((self.CHARGING_WITH_A_SCOOTER_ANSWER)))
        question = self.driver.find_element(*self.CHARGING_WITH_A_SCOOTER_QUESTION)
        answer = self.driver.find_element(*self.CHARGING_WITH_A_SCOOTER_ANSWER)
        assert question.get_attribute('aria-expanded') == "true" \
               and answer.text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток' \
                                  ' — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def set_element_can_cancel_order_on_main_page(self):
        element = self.driver.find_element(*self.CAN_CANCEL_ORDER_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((self.CAN_CANCEL_ORDER_QUESTION)))
        element.click()

    def check_answer_for_can_cancel_order(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((self.CAN_CANCEL_ORDER_ANSWER)))
        question = self.driver.find_element(*self.CAN_CANCEL_ORDER_QUESTION)
        answer = self.driver.find_element(*self.CAN_CANCEL_ORDER_ANSWER)
        assert question.get_attribute('aria-expanded') == "true" \
               and answer.text == 'Да, пока самокат не привезли. Штрафа не будет, ' \
                                  'объяснительной записки тоже не попросим. Все же свои.'

    def set_element_live_further_than_mkad_on_main_page(self):
        element = self.driver.find_element(*self.LIVE_FURTHER_THAN_MKAD_QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((self.LIVE_FURTHER_THAN_MKAD_QUESTION)))
        element.click()

    def check_answer_for_live_further_than_mkad(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((self.LIVE_FURTHER_THAN_MKAD_ANSWER)))
        question = self.driver.find_element(*self.LIVE_FURTHER_THAN_MKAD_QUESTION)
        answer = self.driver.find_element(*self.LIVE_FURTHER_THAN_MKAD_ANSWER)
        assert question.get_attribute('aria-expanded') == "true" \
               and answer.text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    def set_element_button_order_in_head_on_main_page(self):
        element = self.driver.find_element(*self.BUTTON_ORDER_IN_HEAD)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((self.BUTTON_ORDER_IN_HEAD)))
        element.click()

    def set_element_button_order_in_footer(self):
        element = self.driver.find_element(*self.BUTTON_ORDER_IN_FOOTER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((self.BUTTON_ORDER_IN_FOOTER)))
        element.click()

    def check_transition_to_orderpage(self):
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'