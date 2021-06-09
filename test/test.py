from utils.helpers import Helper
from time import sleep
from selenium.common.exceptions import TimeoutException
from test import LOG
import pytest


class Test:
    @pytest.mark.start_main_page
    def test_main_page(self, browser):
        prestashop_page = Helper(browser)
        LOG.info("Open the main page of the site")
        prestashop_page.go_to_site()
        LOG.info('A check is made that the price of the products is in accordance with the set currency')
        for i in prestashop_page.check_currency_in_price():
            assert i.text[-1] == prestashop_page.check_currency()[-1]
            LOG.info(f'The currency is set in {i.text[-1]}, that\'s right.')

    @pytest.mark.search_box
    def test_select_dress(self, browser):
        prestashop_page = Helper(browser)
        LOG.info('Select currency dollar to price')
        prestashop_page.select_currency()
        prestashop_page.dollar_currency()
        LOG.info('Write "dress" in search box')
        prestashop_page.select_dress()
        assert int(prestashop_page.check_text_num_product()[-2]) == len(prestashop_page.check_num_product())
        LOG.info(f'The quantity of goods corresponds to the quantity in the inscription and is equal to '
                 f'{len(prestashop_page.check_num_product())}')

    @pytest.mark.currency
    def test_price_in_dollar(self, browser):
        prestashop_page = Helper(browser)
        for i in prestashop_page.check_price_in_dollar():
            assert i.text[-1] == prestashop_page.check_currency()[-1]
            LOG.info(f'The currency is set in {i.text[-1]}, that\'s okay.')

    @pytest.mark.sorting
    def test_sorting(self, browser):
        prestashop_page = Helper(browser)
        LOG.info('Sorting product from high price to low')
        prestashop_page.click_sorting()
        prestashop_page.sorting_from_high()
        sleep(5)
        for i in range(len(prestashop_page.check_sorting())-1):
            assert prestashop_page.check_sorting()[i].text >= prestashop_page.check_sorting()[i+1].text
            LOG.info(f'{prestashop_page.check_sorting()[i].text} >= {prestashop_page.check_sorting()[i+1].text}, '
                     f'that\'s okay')

    @pytest.mark.discount
    def test_discount_product(self, browser):
        prestashop_page = Helper(browser)
        LOG.info('Check discount on the site')
        product = prestashop_page.product()
        list_discount_product = []
        for i in product:
            child_page = Helper(i)
            try:
                child_page.discount_product()
                list_discount_product.append(i)
            except TimeoutException:
                pass

        for i in list_discount_product:
            child_page = Helper(i)
            assert all([
                child_page.regular_price(),
                child_page.discount_percentage(),
                child_page.price_in_discount()

            ])

            LOG.info("This product have discount")

            regular_price, discount_percentage, price_in_discount = [
                child_page.regular_price()[0].text,
                child_page.discount_percentage()[0].text,
                child_page.price_in_discount()[0].text

            ]
            regular_price_int, discount_percentage_int, price_in_discount_int = [
                (int(regular_price[:5].replace(',', ''))/100),
                (int(discount_percentage[1:].replace('%', ''))/100),
                (int(price_in_discount[:5].replace(',', ''))/100)
             ]

            assert round((regular_price_int - regular_price_int*discount_percentage_int), 2) == price_in_discount_int
            LOG.info(f"Regular price = {regular_price_int},  discount percentage = -{discount_percentage_int}% , "
                     f" finish price = {price_in_discount_int}")

