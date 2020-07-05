from Pages.base_page import BasePage
from locators import SearchLocators


class SearchInput(BasePage):
    _search_input = SearchLocators.search_field
    _assert_movie_title = SearchLocators.movie_page_title
    _find_search_icon = SearchLocators.movie_item

    def __init__(self, driver):
        self.driver = driver

    def search_movies_(self, search_field):
        self._type(self._search_input, search_field)

    def click_on_movie_item_(self):
        self._click(self._find_search_icon)

    def search_movies_titles_(self):
        return self._is_displayed(self._assert_movie_title)