"""
tests.test_next_tram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests the Luas API

Copyright (c) 2017 Ronan Murray <https://github.com/ronanmu>
Licensed under MIT License
"""

import unittest
from luas.api import LuasDirection
import luas.api

class TestApi(unittest.TestCase):
    """ Tests luas.api module. """

    def test_default_balally(self):
        client = luas.api.LuasClient()
        next = client.next_tram('BAL')
        self.assertIsNotNone(next)

    def test_inbound_balally(self):
        client = luas.api.LuasClient()
        next = client.next_tram('BAL', LuasDirection.Inbound)
        self.assertIsNotNone(next)

    def test_outbound_balally(self):
        client = luas.api.LuasClient()
        next = client.next_tram('BAL', LuasDirection.Outbound)
        self.assertIsNotNone(next)