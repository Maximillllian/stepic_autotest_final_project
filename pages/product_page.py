from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def get_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return name

    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return price

    def get_alert_product_name(self):
        name = self.browser.find_elements(*ProductPageLocators.ALERT_PRODUCT_NAME)[0].text
        return name

    def get_total_basket_value(self):
        value = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_VALUE).text
        return value

    def check_product_name_and_alert_product_name_equals(self, product_name, alert_product_name):
        assert product_name == alert_product_name, 'The names are different'

    def check_price_and_total_basket_value_equals(self, product_price, total_basket_value):
        assert product_price == total_basket_value, 'The prices are different'
