"""
tests.test_next_tram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests the Luas API

Copyright (c) 2017 Ronan Murray <https://github.com/ronanmu>
Licensed under MIT License
"""
# flake8: noqa
import unittest
import requests_mock
from luas.api import LuasDirection, LuasLine
import luas.api
import os

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
        self.assertEqual(all_trams[0].direction, LuasDirection.Inbound)
        self.assertEqual(all_trams[0].destination, 'Broombridge')

    @requests_mock.mock()
    def test_default_line_status(self, m):
        with open(self._file_path('balally.xml')) as xml_file:
            m.register_uri('GET', '/xml/get.ashx?action=forecast&encrypt=false&stop=STS', text=xml_file.read(), status_code=200)

        client = luas.api.LuasClient()
        self.assertEqual("Green Line services operating normally", client.line_status())

    @requests_mock.mock()
    def test_red_line_status(self, m):
        with open(self._file_path('tallaght.xml')) as xml_file:
            m.register_uri('GET', '/xml/get.ashx?action=forecast&encrypt=false&stop=TAL', text=xml_file.read(), status_code=200)

        client = luas.api.LuasClient()
        self.assertEqual("Red Line services operating normally", client.line_status(LuasLine.Red))

    @requests_mock.mock()
    def test_tallaght_status(self, m):
        with open(self._file_path('tallaght.xml')) as xml_file:
            m.register_uri('GET', '/xml/get.ashx?action=forecast&encrypt=false&stop=TAL', text=xml_file.read(), status_code=200)

        client = luas.api.LuasClient()
        tallaght = client.all_trams('TAL')
        self.assertIsNotNone(tallaght)
        self.assertEqual(2, len(tallaght))

    @requests_mock.mock()
    def test_tallaght_outbound(self, m):
        with open(self._file_path('tallaght.xml')) as xml_file:
            m.register_uri('GET', '/xml/get.ashx?action=forecast&encrypt=false&stop=TAL', text=xml_file.read(), status_code=200)

        client = luas.api.LuasClient()
        tallaght = client.next_tram('Tallaght', LuasDirection.Outbound)
        # There are never any outbound trams from Tallaght as it is the end of the line
        self.assertIs(None, tallaght)

    @requests_mock.mock()
    def test_endpoint_failure(self, m):
        m.register_uri('GET', '/xml/get.ashx?action=forecast&encrypt=false&stop=STS', status_code=404)

        client = luas.api.LuasClient()
        status = client.line_status()
        self.assertEqual('n/a', status)

    @requests_mock.mock()
    def test_invalid_response(self, m):
        with open(self._file_path('failed.xml')) as xml_file:
            m.register_uri('GET', '/xml/get.ashx?action=forecast&encrypt=false&stop=STS', text=xml_file.read(), status_code=200)

        client = luas.api.LuasClient()
        status = client.line_status()
        self.assertEqual('n/a', status)

    @requests_mock.mock()
    def test_invalid_response_empty(self, m):
        with open(self._file_path('empty_response')) as xml_file:
            m.register_uri('GET', '/xml/get.ashx?action=forecast&encrypt=false&stop=STS', text=xml_file.read(), status_code=200)

        client = luas.api.LuasClient()
        status = client.line_status()
        self.assertEqual('n/a', status)

    def test_invalid_stop_name(self):
        client = luas.api.LuasClient()
        details = client.next_tram('My pretend stop')
        self.assertIs(None, details)
        stop_details = client.stop_details('My pretend stop')
        self.assertEqual('n/a', stop_details['status'])

    def test_load_stops_file(self):
        from luas.models import LuasStops
        stops = LuasStops()
        self.assertIsNotNone(stops.stops)
        self.assertTrue(stops.stop_exists('BAL'))
        self.assertTrue(stops.stop_exists('Dundrum'))
        self.assertTrue(stops.stop_exists('St. Stephen\'s Green'))
        self.assertTrue(stops.stop_exists('O\'Connell - GPO'))
        self.assertFalse(stops.stop_exists('123'))

        balally = stops.stop('Balally')
        self.assertEqual('1', balally['isParkRide'])

    @staticmethod
    def _file_path(file_name):
        thispath = os.path.dirname(__file__)
        return "{}/{}".format(thispath, file_name)
