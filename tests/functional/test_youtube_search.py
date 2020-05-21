from tests.functional.test_base import TestBase


class TestGitLabProject(TestBase):

    def test_youtube(self):
        self.youtube_main_page.search_field.send_keys("funny dogs")
        self.youtube_main_page.search_button.click()
        self.assertTrue(True)
