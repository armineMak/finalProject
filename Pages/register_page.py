import time

from Pages.base_page import BasePage
from Pages.utils import only_domain_gen
from locators import RegisterPageLocators


class RegisterPage(BasePage):
    _user_email = RegisterPageLocators.email_field
    _register_pass = RegisterPageLocators.register_password_field
    _confirm_pass = RegisterPageLocators.confirm_password_field
    _create_account_button = RegisterPageLocators.register_submit_button
    _success_message_displayed = RegisterPageLocators.success_message
    _message_after_signup = RegisterPageLocators.success_message_after_signup

    # mailinator
    _mailinator_email = RegisterPageLocators.mailinator_email_field
    _click_on_button = RegisterPageLocators.inbox_submit_button
    _click_on_email_row = RegisterPageLocators.email_row
    _switch_to_mailinator_frame = RegisterPageLocators.mailinator_frame
    _click_on_confirm_email = RegisterPageLocators.confirm_email_link
    # yopmail
    _yopmail_email = RegisterPageLocators.yopmail_email_field
    _switch_to_yopmail_frame = RegisterPageLocators.yopmail_frame
    _click_on_email_confirm = RegisterPageLocators.confirm_email_link1

    def __init__(self, driver):
        self.driver = driver

    def register_fields_(self, email_field, register_password_field, confirm_password_field):
        self._type(self._user_email, email_field)
        self._type(self._register_pass, register_password_field)
        self._type(self._confirm_pass, confirm_password_field)
        self._click(self._create_account_button)

    def success_message_content_displayed_(self):
        return self._is_displayed(self._success_message_displayed)

    def get_success_message_text_(self):
        return self._find(self._success_message_displayed)

    def confirm_email_(self, mailinator_email_field, yopmail_email_field):
        if only_domain_gen == "mailinator.com":
            iteration = 4
            while iteration > 0:
                iteration = iteration - 1
                self._find_and_clear(self._mailinator_email)
                self._type(self._mailinator_email, mailinator_email_field)
                if self._find(self._mailinator_email).get_attribute('value') == mailinator_email_field:
                    break
            self._click(self._click_on_button)
            self._click(self._click_on_email_row)
            self.driver.switch_to.frame(self._find(self._switch_to_mailinator_frame))
            self._click_by_js(self._click_on_confirm_email)
        elif only_domain_gen == "yopmail.com":
            self._find_and_clear(self._yopmail_email)
            self._type(self._yopmail_email, yopmail_email_field)
            self._enter_button(self._yopmail_email)
            self.driver.switch_to.frame(self._find(self._switch_to_yopmail_frame))
            self._is_displayed(self._switch_to_yopmail_frame, timeout=5)
            self._click(self._click_on_email_confirm)

    def message_displayed_(self):
        return self._find(self._message_after_signup)
