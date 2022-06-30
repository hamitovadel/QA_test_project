from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def return_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def return_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def checking_added_to_basket_product_name(self, product_name):
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME)
        assert product_name == alert_product_name.text, "Product name is {}, but reported name is {}"\
            .format(product_name, alert_product_name.text)

    def checking_added_to_basket_product_price(self, product_price):
        alert_product_price = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE)
        assert product_price == alert_product_price.text, "Product price is {}, but reported price is {}"\
            .format(product_price, alert_product_price.text)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_be_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappear, but should be"
