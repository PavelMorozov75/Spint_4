import sys
sys.path.insert(1, './pages')
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from mainpage import MainPageScooter
from selenium.webdriver.common.keys import Keys

class OrderPage(MainPageScooter):

    LOGO_SCOOTER = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    YANDEX = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    HEADER_FOR_WHO = [By.XPATH, "//div[@class='Order_Header__BZXOb']"]
    NAME = [By.XPATH, "//div[@class='Order_Form__17u6u']/div[1]/input"]
    SURNAME = [By.XPATH, "//div[@class='Order_Form__17u6u']/div[2]/input"]
    ADDRESS = [By.XPATH, "//div[@class='Order_Form__17u6u']/div[3]/input"]
    METRO = [By.XPATH, "//input[@class='select-search__input']"]
    PHONE_NUMBER = [By.XPATH, "//div[@class='Order_Form__17u6u']/div[5]/input"]
    BUTTON_CONTINUE = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    HEADER_ABOUT_RENT = [By.XPATH, "//div[@class='Order_Header__BZXOb']"]
    WHEN = [By.XPATH, "//div[@class='react-datepicker-wrapper']/div[@class='react-datepicker__input-container']/input"]
    DATE_PICKER = [By.XPATH, "//div[@class='react-datepicker-popper']"]
    RENTAL_PERIOD = [By.XPATH, "//div[@class='Dropdown-placeholder']"]
    DROP_DOWN_MENU = [By.XPATH, "//div[@class='Dropdown-menu']"]
    RENTAL_PERIOD_DAY = [By.XPATH, "//div[@class='Dropdown-menu']/div[1]"]
    RENTAL_PERIOD_TWO_DAYS = [By.XPATH, "//div[@class='Dropdown-menu']/div[2]"]
    CHECKBOX_COLOR_BLACK = [By.XPATH, "//div[@class='Order_Checkboxes__3lWSI']/label[1]"]
    CHECKBOX_COLOR_GRAY = [By.XPATH, "//div[@class='Order_Checkboxes__3lWSI']/label[2]"]
    COMMENT = [By.XPATH, "//div[@class ='Input_InputContainer__3NykH']/input[@class ='Input_Input__1iN_Z"
                         " Input_Responsible__1jDKN']"]
    ORDER_BUTTON_BELOW = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    ORDER_BUTTON_AT_THE_TOP = [By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[1]"]
    CONFIRMATION_BUTTON = [By.XPATH, "//div[@class='Order_Modal__YZ-d3']/div[2]/button[2]"]
    ORDER_COMPLITED = [By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"]


    def set_element_by_order_for_who(self, firstname, surname, address, metro, phonenumber):

        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located((self.HEADER_FOR_WHO)))
        self.driver.find_element(*self.NAME).send_keys(firstname)
        self.driver.find_element(*self.SURNAME).send_keys(surname)
        self.driver.find_element(*self.ADDRESS).send_keys(address)
        WebDriverWait(self.driver, 8).until(
            expected_conditions.visibility_of_element_located((self.METRO)))
        self.driver.find_element(*self.METRO).click()
        self.driver.find_element(*self.METRO).send_keys(metro)
        element = self.driver.find_element(*self.METRO)
        element.send_keys(Keys.ARROW_DOWN, Keys.RETURN)
        self.driver.find_element(*self.PHONE_NUMBER).send_keys(phonenumber)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((self.BUTTON_CONTINUE)))
        self.driver.find_element(*self.BUTTON_CONTINUE).click()

    def check_filling_order_for_who(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((self.HEADER_ABOUT_RENT)))
        assert self.driver.find_element(*self.HEADER_ABOUT_RENT)

    def set_element_by_order_about_rent(self, date, rental_periode, color, comment):
        self.driver.find_element(*self.WHEN).clear()
        self.driver.find_element(*self.WHEN).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((self.DATE_PICKER)))
        self.driver.find_element(*self.WHEN).send_keys(date)
        self.driver.find_element(*self.WHEN).send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 8).until(
            expected_conditions.element_to_be_clickable((self.RENTAL_PERIOD)))
        self.driver.find_element(*self.RENTAL_PERIOD).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((self.DROP_DOWN_MENU)))
        if rental_periode == 'сутки':
            self.driver.find_element(*self.RENTAL_PERIOD_DAY).click()
        elif rental_periode == 'двое суток':
            self.driver.find_element(*self.RENTAL_PERIOD_TWO_DAYS).click()
        if color == 'черный':
            self.driver.find_element(*self.CHECKBOX_COLOR_BLACK).click()
        elif color == 'серый':
            self.driver.find_element(*self.CHECKBOX_COLOR_GRAY).click()
        self.driver.find_element(*self.COMMENT).send_keys(comment)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((self.ORDER_BUTTON_BELOW)))
        self.driver.find_element(*self.ORDER_BUTTON_BELOW).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((self.CONFIRMATION_BUTTON)))
        self.driver.find_element(*self.CONFIRMATION_BUTTON).click()

    def check_order_complited(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((self.ORDER_COMPLITED)))
        assert self.driver.find_element(*self.ORDER_COMPLITED)

    def set_element_logo_scooter(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((self.LOGO_SCOOTER)))
        self.driver.find_element(*self.LOGO_SCOOTER).click()

    def check_transition_to_main_page(self):
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def set_element_yandex(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((self.YANDEX)))
        self.driver.find_element(*self.YANDEX).click()
        self.driver.switch_to.window(self.driver.window_handles[1])













