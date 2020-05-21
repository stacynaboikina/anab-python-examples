import logging
import unittest
from selenium import webdriver

from selenium.webdriver.support.events import EventFiringWebDriver

from tests.handlers.youtube_main_page import GoogleMainPage
from tests.handlers.event_handler import CustomEventListener

class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = "https://google.com"
        web_driver = webdriver.Chrome()
        web_driver.implicitly_wait(20)
        web_driver.get(cls.base_url)

        web_driver = EventFiringWebDriver(web_driver, CustomEventListener())

        cls.youtube_main_page = GoogleMainPage(web_driver)

    def setUp(self):
        self.logger = logging.getLogger(self.id())

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass


class TestSomething(TestBase):

    def test_some_feature(self):
        self.some_helper_method()

    def test_some_other_feature(self):
        pass

    def some_helper_method(self):
        pass




class A:
    def __init__(self):
        self.some_method()

    def some_method(self):
        print("In some method")
        pass


a = A()