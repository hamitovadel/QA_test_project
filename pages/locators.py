from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, "login_form")


class RegisterPageLocators:
    REGISTER_FORM = (By.CLASS_NAME, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")

    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
