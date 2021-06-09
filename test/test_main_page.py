from pages.main_page import MainPage
from test import LOG
import pytest


class MainPageSuite:
    @pytest.mark.start_main_page
    def test_main_page(self, browser):
        prestashop_page = MainPage(browser)
        LOG.info("Open the main page of the site")
        prestashop_page.go_to_site()
        LOG.info('A check is made that the price of the products is in accordance with the set currency')
        for i in prestashop_page.check_currency_in_price():
            assert i.text[-1] == prestashop_page.check_currency()[-1]
            LOG.info(f'The currency is set in {i.text[-1]}, that\'s right.')

    @pytest.mark.search_box
    def test_select_dress(self, browser):
        prestashop_page = MainPage(browser)
        LOG.info('Select currency dollar to price')
        prestashop_page.select_dollar_currency()
        LOG.info('Write "dress" in search box')
        prestashop_page.select_dress()
        assert int(prestashop_page.check_text_num_product()[-2]) == len(prestashop_page.check_num_product())
        LOG.info(f'The quantity of goods corresponds to the quantity in the inscription and is equal to '
                 f'{len(prestashop_page.check_num_product())}')
