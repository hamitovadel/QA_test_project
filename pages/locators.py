from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginFormLocators:
    LOGIN_FORM = (By.CLASS_NAME, "login_form")


class RegisterFormLocators:
    REGISTER_FORM = (By.CLASS_NAME, "register_form")
