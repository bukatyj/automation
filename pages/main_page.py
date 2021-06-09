from pages.base_page import BasePage
from locators.locators import LocatorsMainPage
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    def check_currency(self):
        return self.find_element(LocatorsMainPage.LOCATOR_CURRENCY, time=2).text

    def check_currency_in_price(self):
        return self.find_elements(LocatorsMainPage.LOCATOR_PRICE, time=2)

    def select_dollar_currency(self):
        return self.find_element(LocatorsMainPage.LOCATOR_CURRENCY_SELECTION, time=5).click(),\
               self.click_element(LocatorsMainPage.LOCATOR_CURRENCY_DOLLAR, time=5).click()

    def select_dress(self):
        return self.find_element(LocatorsMainPage.LOCATOR_FOUND, time=2).clear, \
               self.find_element(LocatorsMainPage.LOCATOR_FOUND, time=2).send_keys('dress', Keys.ENTER)

    def check_text_num_product(self):
        return self.find_element(LocatorsMainPage.LOCATOR_NUMBER_PRODUCTS_TEXT, time=2).text

    def check_num_product(self):
        return self.find_elements(LocatorsMainPage.LOCATOR_NUMBER_PRODUCTS, time=2)
