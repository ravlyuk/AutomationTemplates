from locators import AutoScout24Locators
from utils.base import Base
from utils.driver import init_driver


class AutoScout24(Base):
    def __init__(self, driver=None, url=None):
        super().__init__(driver)
        self.locators = AutoScout24Locators
        self.url = url

    def grub_links(self):
        self.driver.get(self.url)
        self.driver.find_element(*self.locators.button).click()
        return self.driver.find_element(*self.locators.url_xpath)


if __name__ == "__main__":
    main_url = 'https://www.autoscout24.ch/de/autos/bmw--335?make=9&model=1581&page=2&vehtyp=10'
    bot = AutoScout24(driver=init_driver(), url=main_url)
    links = bot.grub_links()
    print(links)
