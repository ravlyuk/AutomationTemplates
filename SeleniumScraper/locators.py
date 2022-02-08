from selenium.webdriver.common.by import By


class AutoScout24Locators:
    url_xpath = (By.XPATH, '//div[@class="position-relative"]/*/*/a[@data-qa="details-link"]/@href')
    button = (By.XPATH, '//div[@aria-label="Click to verify"]')
