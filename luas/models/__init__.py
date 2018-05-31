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

    @property
    def direction(self):
        """ Fetch the direction property """
        return self._direction

    @property
    def destination(self):
        """ Fetch the destination property """
        return self._destination


class LuasStops(object):
    """Represents Luas stops"""

    def __init__(self):
        import json
        with open(self._file_path('luas_stops.json')) as stops_file:
            self._stops = json.load(stops_file)

    @property
    def stops(self):
        """Return the list of Luas Stops"""
        return self._stops

    def stop(self, stop_name):
        """
        Returns the stop matching the provided name or abbreviation
        :param stop_name:
        :return:
        """
        return next((stop for stop in self._stops
                     if stop['abrev'] == stop_name
                     or stop['name'] == stop_name), None)

    def stop_exists(self, stop):
        """Check if a stop exists or not"""
        return self.stop(stop) is not None

    @staticmethod
    def _file_path(file_name):
        import os
        thispath = os.path.dirname(__file__)
        return "{}/{}".format(thispath, file_name)
