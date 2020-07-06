from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.search_box import SearchInput
from Pages.iframe_page import SwitchIframes
from Pages.user_account import UserAccountSettings


class TestFinalProject():

     # using config.json
    def test_final_project(self, browser):

        # Open the main page, go to the sign page and sign in with valid credentials, assert log out
        # button is displayed
        main_page = MainPage(browser)
        main_page.go_login()

        signin_page = LoginPage(browser)
        signin_page.login_fields_("armine4@mailinator.com", "armine")
        assert signin_page.button_displayed_()

        # After log in, click the username button, go to the user account, fill in the empty fields,
        # click the save button, make sure that after saving the information, the user is redirected to the home page
        user_account_page = UserAccountSettings(browser)
        user_account_page.click_on_username_button_()
        user_account_page.fill_first_last_username_("armine", "test", "armineTest4")
        user_account_page.click_on_save_button_()
        assert user_account_page.movies_container_displayed_()

    def test_search_box(self, browser):
        # Find the search box, input some movie title, click on the movie and assert the title
        main_page = MainPage(browser)
        user_page = SearchInput(browser)
        user_page.search_movies_("Kalki")
        user_page.click_on_movie_item_()
        assert user_page.search_movies_titles_()

        # Switch to youtube iframe, find the title and assert it
        video_frame = SwitchIframes(browser)
        video_frame.iframe_displayed_()
        video_frame.switch_to_video_frame_()
        assert video_frame.get_video_title_()




