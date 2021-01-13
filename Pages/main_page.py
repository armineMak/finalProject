from Pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):
    _click_login_button = MainPageLocators.login_button
    _click_sign_up_button = MainPageLocators.sign_up_button

    def __init__(self, driver):
        self.driver = driver

    def go_login(self):
        self._click(self._click_login_button)

    def go_register(self):
        self._click(self._click_sign_up_button)