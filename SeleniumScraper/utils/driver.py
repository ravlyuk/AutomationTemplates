from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


def init_driver():
    options = webdriver.FirefoxOptions()
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.set_window_size(1800, 1200)
    driver.implicitly_wait(20)
    return driver
