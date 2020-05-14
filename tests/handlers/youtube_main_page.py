

class YouTubeMainPage:
    def __init__(self, web_driver):
        self.__web_driver = web_driver

    @property
    def search_field(self):
        return self.__web_driver.find_element_by_id("search-form")