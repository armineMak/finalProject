import time

from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.search_box import SearchInput
from Pages.iframe_page import SwitchIframes
from Pages.user_account import UserAccountSettings
from Pages.register_page import RegisterPage
from Pages.utils import generate_random_emails, get_random_password, email_domains_link, replace_domain, \
    get_random_name, letters_for_account


class TestFinalProject():
    user_email = generate_random_emails(5)
    user_password = get_random_password(6)

    # def test_invalid_signin(self, browser):
    #
    #     main_page = MainPage(browser)
    #     main_page.go_login()
    #
    #     signin_page = LoginPage(browser)
    #     signin_page.login_fields_(self.user_email, self.user_password)
    #     assert signin_page.error_content_displayed_()
    #     print(signin_page.get_error_message_text_())

    def test_register(self, config, browser):
        main_page = MainPage(browser)

        for i in range(1):
            browser.get(config["baseURL"])
            main_page.go_register()
            user_email = generate_random_emails(5)
            user_password = get_random_password(6)

            register_page = RegisterPage(browser)
            register_page.register_fields_(user_email, user_password, user_password)
            assert register_page.success_message_content_displayed_()
            browser.execute_script("window.open()")
            browser.switch_to.window(browser.window_handles[1])
            browser.get(email_domains_link())
            email_page = RegisterPage(browser)
            email_page.confirm_email_(user_email, user_email)
            browser.switch_to.window(browser.window_handles[2])
            updated_url = replace_domain(browser.current_url)
            browser.get(updated_url)
            assert register_page.success_message_content_displayed_()

            browser.switch_to.window(browser.window_handles[0])
            browser.close()

            browser.switch_to.window(browser.window_handles[0])
            browser.close()

            browser.switch_to.window(browser.window_handles[0])

    def test_valid_signin(self, browser):
        main_page = MainPage(browser)
        main_page.go_login()

        signin_page = LoginPage(browser)
        signin_page.login_fields_(self.user_email, self.user_password)
        assert signin_page.button_displayed_()

        user_account_page = UserAccountSettings(browser)
        user_account_page.click_on_username_button_()
        user_account_page.fill_first_last_username_(get_random_name(letters_for_account, 6),
                                                    get_random_name(letters_for_account, 6),
                                                    get_random_name(letters_for_account, 6))
        user_account_page.click_on_save_button_()
        assert user_account_page.movies_container_displayed_()

    #
    # def test_search_box(self, browser):
    #
    #     main_page = MainPage(browser)
    #     user_page = SearchInput(browser)
    #     user_page.search_movies_("Kalki")
    #     user_page.click_on_movie_item_()
    #     assert user_page.search_movies_titles_()
    #
    #     video_frame = SwitchIframes(browser)
    #     video_frame.iframe_displayed_()
    #     video_frame.switch_to_video_frame_()
    #     assert video_frame.get_video_title_()
    #     print(video_frame.get_video_title_())
