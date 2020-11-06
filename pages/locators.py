from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_BUTTON = (By.CSS_SELECTOR, 'div.basket-mini span.btn-group')
    CURRENT_LANGUAGE = (By.CSS_SELECTOR, 'select[name="language"] option[selected]')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    CONTINUE_SHOPPING_TEXT = (By.CSS_SELECTOR, '#content_inner p a')


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#register_form [type="email"]')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#register_form [name="registration-password1"]')
    REGISTER_REPEAT_PASSWORD = (By.CSS_SELECTOR, '#register_form [name="registration-password2"]')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success .alertinner strong ')
    TOTAL_BASKET_VALUE = (By.CSS_SELECTOR, '.alert-info .alertinner strong ')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')