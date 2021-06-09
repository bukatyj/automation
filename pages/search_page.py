from pages.base_page import BasePage
from locators.locators import LocatorsSearchPage
from selenium.common.exceptions import TimeoutException


class SearchPage(BasePage):

    def check_price_in_dollar(self):
        return self.find_elements(LocatorsSearchPage.LOCATOR_PRICE, time=2)

    def click_sorting_from_high(self):
        return self.click_element(LocatorsSearchPage.LOCATOR_SELECT_TITLE, time=5).click(), \
               self.click_element(LocatorsSearchPage.LOCATOR_SORTING_FROM_HIGH, time=5).click()

    def check_sorting(self):
        return self.find_elements(LocatorsSearchPage.LOCATOR_PRICE_FROM_HIGH, time=5)

    def product(self):
        return self.find_elements(LocatorsSearchPage.LOCATOR_PRODUCT, time=2)

    def discount_product(self):
        return self.find_elements(LocatorsSearchPage.LOCATOR_DISCOUNT_PRODUCT, time=2)

    def regular_price(self):
        return self.find_elements(LocatorsSearchPage.LOCATOR_REGULAR_PRICE, time=2)

    def discount_percentage(self):
        return self.find_elements(LocatorsSearchPage.LOCATOR_DISCOUNT_PERCENTAGE, time=2)

    def price_in_discount(self):
        return self.find_elements(LocatorsSearchPage.LOCATOR_PRICE_IN_DISCOUNT, time=2)

    def check_currency(self):
        return self.find_element(LocatorsSearchPage.LOCATOR_CURRENCY, time=2).text

    def check_discount(self):
        product, list_discount_product = self.product(), []
        for i in product:
            try:
                SearchPage(i).discount_product()
                list_discount_product.append(i)
            except TimeoutException:
                pass
        return list_discount_product

    def wait(self, time=10):
        return self.driver.implicitly_wait(time)
