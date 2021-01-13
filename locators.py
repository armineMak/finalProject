from selenium.webdriver.common.by import By


# To find most items, use id
class MainPageLocators(object):
    login_button = {"by": By.ID, "value": "login"}
    sign_up_button = {"by": By.ID, "value": "register"}


class RegisterPageLocators(object):
    # register page locators
    email_field = {"by": By.ID, "value": "email"}
    register_password_field = {"by": By.ID, "value": "password"}
    confirm_password_field = {"by": By.ID, "value": "confirm_password"}
    register_submit_button = {"by": By.ID, "value": "register_submit"}
    success_message = {"by": By.CSS_SELECTOR, "value": "div.notifications-area > div > div > p.w-400"}
    success_message_after_signup = {"by": By.LINK_TEXT, "value": "Thank you for verifying your email address!"}

    # domains locators
    # damoin1
    mailinator_email_field = {"by": By.ID, "value": "inbox_field"}
    inbox_submit_button = {"by": By.ID, "value": "go_inbox"}
    email_row = {"by": By.LINK_TEXT, "value": "Email Verification"}
    mailinator_frame = {"by": By.ID, "value": "msg_body"}
    #confirm_email_link = {"by": By.PARTIAL_LINK_TEXT, "value": "signin"}
    confirm_email_link = {"by": By.XPATH, "value": '//*[@id="backgroundTable"]//tbody/tr[2]/td/table/tbody/tr[6]/td/a'}
    # domain2
    yopmail_email_field = {"by": By.ID, "value": "login"}
    yopmail_frame = {"by": By.ID, "value": "ifmail"}
    confirm_email_link1 = {"by": By.PARTIAL_LINK_TEXT, "value": "signin"}


class LoginPageLocators(object):
    username_field = {"by": By.ID, "value": "email"}
    password_field = {"by": By.ID, "value": "password"}
    sign_in_button = {"by": By.ID, "value": "sign_in"}
    homepage_assert = {"by": By.CSS_SELECTOR, "value": ".logOutHolder"}
    error_message_content = {"by": By.CSS_SELECTOR, "value": ".error-list"}


class SearchLocators(object):
    search_field = {"by": By.ID, "value": "searchInput"}
    movie_item = {"by": By.CSS_SELECTOR, "value": "#homeSearchResult > li:nth-child(3) > a"}
    movie_page_title = {"by": By.CSS_SELECTOR, "value": "section.poster.bg-light > div > div > h1"}


class IframeLocators(object):
    video_frame = {"by": By.CSS_SELECTOR, "value": ".video-frame"}
    you_tube_video_play = {"by": By.ID, "value": "player"}
    video_title_assert = {"by": By.CSS_SELECTOR, "value": ".ytp-title-link.yt-uix-sessionlink"}


class UserAccountSettingsLocators(object):
    username_button = {"by": By.CSS_SELECTOR, "value": ".userNameBtn"}
    user_account_first_name = {"by": By.ID, "value": "first_name"}
    user_account_last_name = {"by": By.ID, "value": "last_name"}
    user_account_username = {"by": By.NAME, "value": "username"}
    account_save_button = {"by": By.XPATH, "value": '//*[@id="users_add_form"]/div[3]/div/input'}
    homepage_movies_container = {"by": By.ID, "value": "movies_holder"}
