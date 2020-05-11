import requests

from unittest import TestCase
from unittest.mock import MagicMock

from feature import Feature, CALL_URL


class FakeReqGet:
    text = "<html> Mocked text </html>"
    status_code = 200


class TestFeature(TestCase):
    def setUp(self):
        print("SET UP")
        requests.get = MagicMock(return_value=FakeReqGet())
        self.feature = Feature()

    def test_feature_req_get_integration(self):
        print("TEST 1")
        resp = self.feature.req_get()
        self.assertTrue(requests.get.called, "Verify requests.get was called")
        self.assertEqual(resp, FakeReqGet.text, "Verify req_get returned expected text")

    def test_feature_req_get_unit(self):
        print("TEST 2")
        self.feature.call_url = MagicMock(return_value=FakeReqGet)
        resp = self.feature.req_get()
        self.assertEqual(self.feature.call_url.call_args[0][0], CALL_URL,
                         f"Verify call_url was called with params {CALL_URL}")
        self.assertEqual(self.feature.call_url.call_count, 1)
        self.assertEqual(self.feature.call_url.return_value.status_code, FakeReqGet.status_code)
        self.assertEqual(resp, FakeReqGet.text, "Verify req_get returned expected text")
