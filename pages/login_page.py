from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegisterPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Wrong url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.enter_to_form(*RegisterPageLocators.EMAIL_FIELD, email)
        self.enter_to_form(*RegisterPageLocators.PASSWORD_FIELD, password)
        self.enter_to_form(*RegisterPageLocators.CONFIRM_PASSWORD_FIELD, password)
        self.press_button(*RegisterPageLocators.REGISTER_BUTTON)
        assert self.is_element_present(*RegisterPageLocators.SUCCESS_REG_MESSAGE), \
            "Registration message is not present"
