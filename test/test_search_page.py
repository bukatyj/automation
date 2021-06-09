from pages.search_page import SearchPage
from time import sleep
from test import LOG
import pytest


class SearchPageSuite:
    @pytest.mark.currency
    def test_price_in_dollar(self, browser):
        prestashop_page = SearchPage(browser)
        for i in prestashop_page.check_price_in_dollar():
            assert i.text[-1] == prestashop_page.check_currency()[-1]
            LOG.info(f'The currency is set in {i.text[-1]}, that\'s okay.')

    @pytest.mark.sorting
    def test_sorting(self, browser):
        prestashop_page = SearchPage(browser)
        LOG.info('Sorting product from high price to low')
        prestashop_page.click_sorting_from_high()
        sleep(5)
        for i in range(len(prestashop_page.check_sorting()) - 1):
            assert prestashop_page.check_sorting()[i].text >= prestashop_page.check_sorting()[i + 1].text
            LOG.info(f'{prestashop_page.check_sorting()[i].text} >= {prestashop_page.check_sorting()[i + 1].text}, '
                     f'that\'s okay')

    @pytest.mark.discount
    def test_discount_product(self, browser):
        LOG.info('Check discount on the site')

        for i in SearchPage(browser).check_discount():
            assert all([
                SearchPage(i).regular_price(),
                SearchPage(i).discount_percentage(),
                SearchPage(i).price_in_discount()

            ])

            LOG.info("This product have discount")

            regular_price, discount_percentage, price_in_discount = [
                SearchPage(i).regular_price()[0].text,
                SearchPage(i).discount_percentage()[0].text,
                SearchPage(i).price_in_discount()[0].text
            ]

            regular_price_int, discount_percentage_int, price_in_discount_int = [
                (int(regular_price[:5].replace(',', '')) / 100),
                (int(discount_percentage[1:].replace('%', '')) / 100),
                (int(price_in_discount[:5].replace(',', '')) / 100)
            ]

            assert round((regular_price_int - regular_price_int * discount_percentage_int), 2) == price_in_discount_int
            LOG.info(f"Regular price = {regular_price},  discount percentage = {discount_percentage} , "
                     f" finish price = {price_in_discount}")
