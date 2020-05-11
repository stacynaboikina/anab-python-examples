import requests


CALL_URL = "http://google.com"


class Feature:
    # such methods are private and very hard, maybe even impossible to mock
    def __internal(self):
        print("Internal method")

    def call_url(self, url):
        print("Call url was called")
        return requests.get(url)

    def req_get(self):
        print(f"Calling get with url {CALL_URL}")
        result = self.call_url(CALL_URL)
        return result.text

