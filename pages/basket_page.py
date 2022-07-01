from pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def checking_that_the_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty, but should be"

    def checking_that_the_basket_is_empty_success_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "Empty basket message is not present, but should be"
