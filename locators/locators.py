from selenium.webdriver.common.by import By


class LocatorsMainPage:
    LOCATOR_CURRENCY = (By.XPATH, "//span[@class='expand-more _gray-darker hidden-sm-down']")
    LOCATOR_CURRENCY_SELECTION = (By.XPATH, "//div[@class='currency-selector dropdown js-dropdown']/a")
    LOCATOR_CURRENCY_DOLLAR = (By.XPATH, "//div[@class='currency-selector dropdown js-dropdown open']/ul/li[3]/a")
    LOCATOR_FOUND = (By.NAME, 's')
    LOCATOR_PRICE = (By.CLASS_NAME, 'price')
    LOCATOR_NUMBER_PRODUCTS_TEXT = (By.XPATH, "//div[@class='col-md-6 hidden-sm-down total-products']/p")
    LOCATOR_NUMBER_PRODUCTS = (By.CLASS_NAME, 'product-description')


class LocatorsSearchPage:
    LOCATOR_CURRENCY = (By.XPATH, "//span[@class='expand-more _gray-darker hidden-sm-down']")
    LOCATOR_PRICE = (By.CLASS_NAME, 'price')
    LOCATOR_SELECT_TITLE = (By.CLASS_NAME, 'select-title')
    LOCATOR_SORTING_FROM_HIGH = (
        By.XPATH, "//div[@class='col-sm-12 col-xs-12 col-md-9 products-sort-order dropdown open']/div/a[5]"
    )
    LOCATOR_PRICE_FROM_HIGH = (By.XPATH, "//div[@class='product-price-and-shipping']/span[1]")
    LOCATOR_PRODUCT = (By.XPATH, "//article[@class='product-miniature js-product-miniature']")
    LOCATOR_DISCOUNT_PRODUCT = (By.XPATH, ".//div/ul/li")
    LOCATOR_REGULAR_PRICE = (By.XPATH, ".//div/div[1]/div/span[@class='regular-price']")
    LOCATOR_DISCOUNT_PERCENTAGE = (By.XPATH, ".//div/div[1]/div/span[@class='discount-percentage']")
    LOCATOR_PRICE_IN_DISCOUNT = (By.XPATH, ".//div/div[1]/div/span[@class='price']")
