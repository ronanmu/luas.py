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

    def __init__(self, due, direction, destination, line):
        self.due = due
        self.direction = direction
        self.destination = destination
        self.line = line

    @property
    def due(self):
        """ Fetch the due property """
        return self.due

    @due.setter
    def due(self, due):
        self.due = due

    @property
    def direction(self):
        """ Fetch the direction property """
        return self.direction

    @direction.setter
    def direction(self, direction):
        self.direction = direction
