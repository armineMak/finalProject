from Pages.base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    _username_or_email_input = LoginPageLocators.username_field
    _password_input = LoginPageLocators.password_field
    _submit_button = LoginPageLocators.sign_in_button
    _assert_element = LoginPageLocators.homepage_assert
    _error_message = LoginPageLocators.error_message_content

    def __init__(self, driver):
        self.driver = driver

    def login_fields_(self, username_field, password_field):
        self._type(self._username_or_email_input, username_field)
        self._type(self._password_input, password_field)
        self._click(self._submit_button)

    def button_displayed_(self):
        return self._is_displayed(self._assert_element)

    def error_content_displayed_(self):
        return self._is_displayed(self._error_message)

    def get_error_message_text_(self):
        return self._find(self._error_message).text