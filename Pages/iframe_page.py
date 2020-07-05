from Pages.base_page import BasePage
from locators import IframeLocators


class SwitchIframes(BasePage):
    _frame_for_youtube = IframeLocators.video_frame
    _video_title = IframeLocators.video_title_assert

    def __init__(self, driver):
        self.driver = driver

    def iframe_displayed_(self):
        return self._is_displayed(self._frame_for_youtube, timeout=5)

    def switch_to_video_frame_(self):
        self.driver.switch_to.frame(self._find(self._frame_for_youtube))

    def get_video_title_(self):
        return self._find(self._video_title).text
