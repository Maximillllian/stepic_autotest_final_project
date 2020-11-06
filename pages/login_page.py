from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_field.send_keys(password)
        repeat_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_REPEAT_PASSWORD)
        repeat_password_field.send_keys(password)
        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_submit.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url_contains_element('login')

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form not found'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Login form not found'
