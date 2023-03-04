import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def driver():
    url = 'https://qa-scooter.praktikum-services.ru/'
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser_driver = webdriver.Firefox(executable_path=r'C:\WebDriver\bin\geckodriver.exe', options=options)
    browser_driver.get(url)
    yield browser_driver
    browser_driver.quit()