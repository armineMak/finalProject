from Pages.base_page import BasePage
from locators import UserAccountSettingsLocators


class UserAccountSettings(BasePage):
    _username_button_click = UserAccountSettingsLocators.username_button
    _first_name_input = UserAccountSettingsLocators.user_account_first_name
    _last_name_input = UserAccountSettingsLocators.user_account_last_name
    _account_username = UserAccountSettingsLocators.user_account_username
    _click_to_save = UserAccountSettingsLocators.account_save_button
    _movies_container = UserAccountSettingsLocators.homepage_movies_container

    def __init__(self, driver):
        self.driver = driver

    def click_on_username_button_(self):
        self._click(self._username_button_click)

    def fill_first_last_username_(self, user_account_first_name, user_account_last_name, user_account_username):
        self._type(self._first_name_input, user_account_first_name)
        self._type(self._last_name_input, user_account_last_name)
        self._type(self._account_username, user_account_username)

    def click_on_save_button_(self):
        self._click(self._click_to_save)

    def movies_container_displayed_(self):
        return self._is_displayed(self._movies_container)