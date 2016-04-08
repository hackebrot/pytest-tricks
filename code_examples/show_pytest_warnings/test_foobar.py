# -*- coding: utf-8 -*-

import unittest


class Client:
    def get(self, url, *args, **kwargs):
        # Send a real request based on the given parameters
        pass


class TestResponse:
    def __init__(self, method, url, *args, **kwargs):
        if 'foobar' in url:
            self.status = 404
            self.reason = 'foobar'
        else:
            self.status = 200
            self.reason = None


class TestClient(Client):
    def get(self, url, *args, **kwargs):
        return TestResponse('get', url)


class TestScrapingTool(unittest.TestCase):
    def setUp(self):
        self.client = TestClient()

    def test_success(self):
        response = self.client.get('https://github.com/pytest-dev')
        self.assertEqual(response.status, 200)
        self.assertEqual(response.reason, None)

    def test_failure(self):
        response = self.client.get('foobar')
        self.assertEqual(response.status, 404)
        self.assertEqual(response.reason, 'foobar')
