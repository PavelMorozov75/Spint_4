from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePageScooter:

    def __init__(self, driver):
        self.driver = driver

    def set_element_by_main_page(self, by, locator):
        element = self.driver.find_element(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((by, locator)))
        element.click()

    def check_element_by_main_page(self, by_for_question, locator_for_question, by_for_answer, locator_for_answer,
                                   answer_text):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((by_for_answer, locator_for_answer)))
        question = self.driver.find_element(by_for_question, locator_for_question)
        answer = self.driver.find_element(by_for_answer, locator_for_answer)
        assert question.get_attribute('aria-expanded') == "true" and answer.text == answer_text

    def go_to_order_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')

    def wait_for_element_located(self, by, locator):
        return WebDriverWait(self.driver, 8).until(expected_conditions.visibility_of_element_located((by, locator)))

    def wait_for_element_to_be_clickable(self, by, locator):
        return WebDriverWait(self.driver, 8).until(expected_conditions.element_to_be_clickable((by, locator)))