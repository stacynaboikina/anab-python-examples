from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import AbstractEventListener
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep

def wait_for_true(callable_ref, timeout=20):
    for _ in range(timeout):
        if not callable_ref():
            sleep(1)
        return



class CustomEventListener(AbstractEventListener):
    # todo: we can conditionally enable checks by configuring the environment

    def before_click(self, element, driver):
        print("Wait for element to be displayed before click")
        wait_for_true(element.is_enabled)

    def before_change_value_of(self, element, driver):
        print("Wait for element to be displayed before changing it's value")
        wait_for_true(element.is_displayed)
        wait_for_true(element.is_enabled)

    def before_find(self, by, value, driver):
        print("Wait for element to be located")
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((by, value))
        )
