import unittest
from selenium import webdriver

from tests.handlers.youtube_main_page import YouTubeMainPage


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://https://github.com/devhammed/use-global-hook"
        web_driver = webdriver.Chrome()
        web_driver.get(cls.base_url)
        cls.youtube_main_page = YouTubeMainPage(web_driver)
        super().setUpClass()
