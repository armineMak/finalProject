from selenium.webdriver.common.by import By


# To find most items, use id
class MainPageLocators(object):
    login_button = {"by": By.ID, "value": "login"}


class LoginPageLocators(object):
    username_field = {"by": By.ID, "value": "email"}
    password_field = {"by": By.ID, "value": "password"}
    sign_in_button = {"by": By.ID, "value": "sign_in"}
    homepage_assert = {"by": By.CSS_SELECTOR, "value": ".logOutHolder"}


class SearchLocators(object):
    search_field = {"by": By.ID, "value": "searchInput"}
    movie_item = {"by": By.CSS_SELECTOR, "value": "#homeSearchResult > li:nth-child(3) > a"}
    movie_page_title = {"by": By.CSS_SELECTOR, "value": "section.poster.bg-light > div > div > h1"}


class IframeLocators(object):
    video_frame = {"by": By.CSS_SELECTOR, "value": ".video-frame"}
    you_tube_video_play = {"by": By.ID, "value": "player"}
    video_title_assert = {"by": By.CSS_SELECTOR, "value": ".ytp-title-link.yt-uix-sessionlink"}