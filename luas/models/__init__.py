"""
luas.models
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides models for interrogating Dublin's Luas tram API

Copyright (c) 2017 Ronan Murray <https://github.com/ronanmu>
Licensed under the MIT License
"""

from enum import Enum


class LuasLine(Enum):
    """ Enum for Luas Lines """
    Green = 1
    Red = 2


class LuasDirection(Enum):
    """ Enum for Luas Directions """
    Inbound = 1
    Outbound = 2


class LuasTram(object):
    """ Represents a tram """

    def __init__(self, due, direction, destination):
        self._due = due
        self._direction = direction
        self._destination = destination

    @property
    def due(self):
        """ Fetch the due property """
        return self._due

    @due.setter
    def due(self, value):
        self._due = value

    @property
    def direction(self):
        """ Fetch the direction property """
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    @property
    def destination(self):
        """ Fetch the destination property """
        return self._destination

    @destination.setter
    def destiation(self, value):
        self._destination = value
