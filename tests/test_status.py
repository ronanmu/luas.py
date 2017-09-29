"""
tests.test_status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests the Luas API

Copyright (c) 2017 Ronan Murray <https://github.com/ronanmu>
Licensed under MIT License
"""

import unittest
from luas.api import LuasLine
import luas.api

from luas.models import LuasTram

class TestApi(unittest.TestCase):
    """ Tests luas.api module. """

    def test_default_line_status(self):
        client = luas.api.LuasClient()
        self.assertEqual("Green Line services operating normally", client.line_status())

    def test_red_line_status(self):
        client = luas.api.LuasClient()
        self.assertEqual("Red Line services operating normally", client.line_status(LuasLine.Red))

    def test_green_line_status(self):
        client = luas.api.LuasClient()
        self.assertEqual("Green Line services operating normally", client.line_status(LuasLine.Green))