"""
tests.test_next_tram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests the Luas API

Copyright (c) 2017 Ronan Murray <https://github.com/ronanmu>
Licensed under MIT License
"""

import unittest
import requests_mock
from luas.api import LuasDirection
import luas.api
import sys, os

class TestApi(unittest.TestCase):
    """ Tests luas.api module. """

    @requests_mock.mock()
    def test_default_balally(self, m):
        with open(self._file_path('balally.xml')) as xml_file:
            m.register_uri('GET', '/xml/get.ashx?action=forecast&encrypt=false&stop=BAL', text=xml_file.read(), status_code=200)
        client = luas.api.LuasClient()
        next = client.next_tram('BAL')
        self.assertIsNotNone(next)
        self.assertEqual(next.direction, LuasDirection.Inbound)

    @requests_mock.mock()
    def test_inbound_ranelagh(self, m):
        with open(self._file_path('ranelagh.xml')) as xml_file:
            m.register_uri('GET', '/xml/get.ashx?action=forecast&encrypt=false&stop=RAN', text=xml_file.read(), status_code=200)

        client = luas.api.LuasClient()
        next = client.next_tram('RAN', LuasDirection.Inbound)
        self.assertIsNotNone(next)
        self.assertEqual(next.direction, LuasDirection.Inbound)
        self.assertEqual(next.due, 'DUE')

    @requests_mock.mock()
    def test_outbound_balally(self, m):
        with open(self._file_path('balally.xml')) as xml_file:
            m.register_uri('GET', '/xml/get.ashx?action=forecast&encrypt=false&stop=BAL', text=xml_file.read(), status_code=200)

        client = luas.api.LuasClient()
        next = client.next_tram('BAL', LuasDirection.Outbound)
        self.assertIsNotNone(next)
        self.assertEqual(next.direction, LuasDirection.Outbound)
        self.assertEqual(next.due, '3')

    @requests_mock.mock()
    def test_raw_balally(self, m):
        with open(self._file_path('balally.xml')) as xml_file:
            m.register_uri('GET', '/xml/get.ashx?action=forecast&encrypt=false&stop=BAL', text=xml_file.read(), status_code=200)

        client = luas.api.LuasClient()
        stop_details = client.stop_details('BAL')
        self.assertIsNotNone(stop_details)
        self.assertIsNotNone(stop_details['status'])
        self.assertIsNotNone(stop_details['trams'])

    @requests_mock.mock()
    def test_all_trams(self, m):
        with open(self._file_path('balally.xml')) as xml_file:
            m.register_uri('GET', '/xml/get.ashx?action=forecast&encrypt=false&stop=BAL', text=xml_file.read(), status_code=200)

        client = luas.api.LuasClient()
        all_trams = client.all_trams('BAL')
        self.assertIsNotNone(all_trams)
        self.assertIsNotNone(all_trams[0])
        self.assertEqual(all_trams[0].due, '5')

    @requests_mock.mock()
    def test_default_line_status(self, m):
        with open(self._file_path('balally.xml')) as xml_file:
            m.register_uri('GET', '/xml/get.ashx?action=forecast&encrypt=false&stop=STS', text=xml_file.read(), status_code=200)

        client = luas.api.LuasClient()
        self.assertEqual("Green Line services operating normally", client.line_status())

    @staticmethod
    def _file_path(file_name):
        thispath = os.path.dirname(__file__)
        return "{}/{}".format(thispath, file_name)
