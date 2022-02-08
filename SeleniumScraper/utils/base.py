from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)


class Base:
    driver = None

    class __WebDriver:
        def __init__(self, driver=None):
            self.driver = driver

    def __init__(self, driver=None):
        self.ignored_exceptions = (
            NoSuchElementException,
            StaleElementReferenceException,
        )
        if not self.driver:
            Base.driver = Base.__WebDriver(driver).driver

    def tear_down(self):
        self.driver.quit()
