

class GoogleMainPage:
    def __init__(self, web_driver):
        self.web_driver = web_driver

    @property
    def search_field(self):
        return self.web_driver.find_element_by_class_name("a4bIc").find_elements_by_tag_name("input")[0]

    @property
    def search_button(self):
        return self.web_driver.find_element_by_class_name("gNO89b")