from enum import Enum

class LuasLine(Enum):
    """ Enum for Luas Lines """
    Green = 1
    Red = 2


class LuasTram(object):
    """ Represents a tram """

    def __init__(self, due, direction, destination, line):
        self.due = due
        self.direction = direction
        self.destination = destination
        self.line = line

    @property
    def due(self):
        return self.__due

    @due.setter
    def due(self, due):
        self.__due = due

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction


class LuasStop(object):
    """ Represents a Luas stop """

    def __init__(self, name):
        self.name = name

