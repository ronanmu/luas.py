"""
luas.models
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides models for interrogating Dublin's Luas tram API

Copyright (c) 2017 Ronan Murray <https://github.com/ronanmu>
Licensed under the MIT License
"""
# pylint: disable=bad-continuation
from enum import Enum

LUAS_STOPS = [
  {
    "abrev": "TPT",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.34835",
    "long": "-6.22925833333333",
    "pronunciation": "The Point",
    "name": "The Point"
  },
  {
    "abrev": "SDK",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.3488222222222",
    "long": "-6.23714722222222",
    "pronunciation": "Spencer Dock",
    "name": "Spencer Dock"
  },
  {
    "abrev": "MYS",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.3492472222222",
    "long": "-6.24339444444444",
    "pronunciation": "Mayor Square - NCI",
    "name": "Mayor Square - NCI"
  },
  {
    "abrev": "GDK",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.349528",
    "long": "-6.247575",
    "pronunciation": "George's Dock",
    "name": "George's Dock"
  },
  {
    "abrev": "CON",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3509222222222",
    "long": "-6.24994166666667",
    "pronunciation": "Connolly",
    "name": "Connolly"
  },
  {
    "abrev": "BUS",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.350075",
    "long": "-6.25145",
    "pronunciation": "Busáras",
    "name": "Busáras"
  },
  {
    "abrev": "ABB",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3485888888889",
    "long": "-6.25817222222222",
    "pronunciation": "Abbey Street",
    "name": "Abbey Street"
  },
  {
    "abrev": "JER",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3476861111111",
    "long": "-6.26533333333333",
    "pronunciation": "Jervis",
    "name": "Jervis"
  },
  {
    "abrev": "FOU",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.3468638888889",
    "long": "-6.27343611111111",
    "pronunciation": "Four Courts",
    "name": "Four Courts"
  },
  {
    "abrev": "SMI",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3471333333333",
    "long": "-6.27772777777778",
    "pronunciation": "Smithfield",
    "name": "Smithfield"
  },
  {
    "abrev": "MUS",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.3478666666667",
    "long": "-6.28671388888889",
    "pronunciation": "Museum",
    "name": "Museum"
  },
  {
    "abrev": "HEU",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3466472222222",
    "long": "-6.29180833333333",
    "pronunciation": "Heuston",
    "name": "Heuston"
  },
  {
    "abrev": "JAM",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.3419416666667",
    "long": "-6.29336111111111",
    "pronunciation": "James's",
    "name": "James's"
  },
  {
    "abrev": "FAT",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3384388888889",
    "long": "-6.29254722222222",
    "pronunciation": "Fatima",
    "name": "Fatima"
  },
  {
    "abrev": "RIA",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.3379083333333",
    "long": "-6.29724166666667",
    "pronunciation": "Rialto",
    "name": "Rialto"
  },
  {
    "abrev": "SUI",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3366166666667",
    "long": "-6.30721111111111",
    "pronunciation": "Suir Road",
    "name": "Suir Road"
  },
  {
    "abrev": "GOL",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3358916666667",
    "long": "-6.31356944444444",
    "pronunciation": "Goldenbridge",
    "name": "Goldenbridge"
  },
  {
    "abrev": "DRI",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.3353611111111",
    "long": "-6.31816111111111",
    "pronunciation": "Drimnagh",
    "name": "Drimnagh"
  },
  {
    "abrev": "BLA",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.3342583333333",
    "long": "-6.32739444444444",
    "pronunciation": "Blackhorse",
    "name": "Blackhorse"
  },
  {
    "abrev": "BLU",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3292972222222",
    "long": "-6.33379166666667",
    "pronunciation": "Bluebell",
    "name": "Bluebell"
  },
  {
    "abrev": "KYL",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.3266555555556",
    "long": "-6.34344444444444",
    "pronunciation": "Kylemore",
    "name": "Kylemore"
  },
  {
    "abrev": "RED",
    "isParkRide": "1",
    "isCycleRide": "1",
    "lat": "53.3168333333333",
    "long": "-6.36987222222222",
    "pronunciation": "Red Cow",
    "name": "Red Cow"
  },
  {
    "abrev": "KIN",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3036944444444",
    "long": "-6.36525",
    "pronunciation": "Kingswood",
    "name": "Kingswood"
  },
  {
    "abrev": "BEL",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.2992861111111",
    "long": "-6.37488611111111",
    "pronunciation": "Belgard",
    "name": "Belgard"
  },
  {
    "abrev": "COO",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.2935055555556",
    "long": "-6.38439722222222",
    "pronunciation": "Cookstown",
    "name": "Cookstown"
  },
  {
    "abrev": "HOS",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.2893694444444",
    "long": "-6.37885",
    "pronunciation": "Hospital",
    "name": "Hospital"
  },
  {
    "abrev": "TAL",
    "isParkRide": "1",
    "isCycleRide": "1",
    "lat": "53.2874944444444",
    "long": "-6.37458888888889",
    "pronunciation": "Tallaght",
    "name": "Tallaght"
  },
  {
    "abrev": "FET",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.29351885",
    "long": "-6.395553516667",
    "pronunciation": "Fettercairn",
    "name": "Fettercairn"
  },
  {
    "abrev": "CVN",
    "isParkRide": "1",
    "isCycleRide": "1",
    "lat": "53.290982416667",
    "long": "-6.4068485",
    "pronunciation": "Cheeverstown",
    "name": "Cheeverstown"
  },
  {
    "abrev": "CIT",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.28783255",
    "long": "-6.418914583333",
    "pronunciation": "Citywest Campus",
    "name": "Citywest Campus"
  },
  {
    "abrev": "FOR",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.284250633333",
    "long": "-6.42460165",
    "pronunciation": "Fortunestown",
    "name": "Fortunestown"
  },
  {
    "abrev": "SAG",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.28467885",
    "long": "-6.43776255",
    "pronunciation": "Saggart",
    "name": "Saggart"
  },
  {
    "abrev": "BRO",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.37223956",
    "long": "-6.29768465",
    "pronunciation": "Broombridge",
    "name": "Broombridge"
  },
  {
    "abrev": "CAB",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.36433419",
    "long": "-6.28196899",
    "pronunciation": "Cabra",
    "name": "Cabra"
  },
  {
    "abrev": "PHI",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.36037646",
    "long": "-6.27888498",
    "pronunciation": "Phibsborough",
    "name": "Phibsborough"
  },
  {
    "abrev": "GRA",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.35719205",
    "long": "-6.27733848",
    "pronunciation": "Grangegorman",
    "name": "Grangegorman"
  },
  {
    "abrev": "BRD",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.35407442",
    "long": "-6.27375642",
    "pronunciation": "Broadstone - DIT",
    "name": "Broadstone - DIT"
  },
  {
    "abrev": "DOM",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.3513492",
    "long": "-6.26554234",
    "pronunciation": "Dominick",
    "name": "Dominick"
  },
  {
    "abrev": "PAR",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.35310356",
    "long": "-6.26050153",
    "pronunciation": "Parnell",
    "name": "Parnell"
  },
  {
    "abrev": "OUP",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.35161218",
    "long": "-6.26102943",
    "pronunciation": "O'Connell - Upper",
    "name": "O'Connell - Upper"
  },
  {
    "abrev": "OGP",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.34884509",
    "long": "-6.25988168",
    "pronunciation": "O'Connell - GPO",
    "name": "O'Connell - GPO"
  },
  {
    "abrev": "MAR",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.34924219",
    "long": "-6.25773649",
    "pronunciation": "Marlborough",
    "name": "Marlborough"
  },
  {
    "abrev": "WES",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.34635626",
    "long": "-6.25897083",
    "pronunciation": "Westmoreland",
    "name": "Westmoreland"
  },
  {
    "abrev": "TRY",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.34528172",
    "long": "-6.25825674",
    "pronunciation": "Trinity",
    "name": "Trinity"
  },
  {
    "abrev": "DAW",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.34216927",
    "long": "-6.25796366",
    "pronunciation": "Dawson",
    "name": "Dawson"
  },
  {
    "abrev": "STS",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.3390722222222",
    "long": "-6.26133333333333",
    "pronunciation": "St. Stephen's Green",
    "name": "St. Stephen's Green"
  },
  {
    "abrev": "HAR",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3333583333333",
    "long": "-6.26265",
    "pronunciation": "Harcourt",
    "name": "Harcourt"
  },
  {
    "abrev": "CHA",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3306694444444",
    "long": "-6.25868333333333",
    "pronunciation": "Charlemont",
    "name": "Charlemont"
  },
  {
    "abrev": "RAN",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3264333333333",
    "long": "-6.25620277777778",
    "pronunciation": "Ranelagh",
    "name": "Ranelagh"
  },
  {
    "abrev": "BEE",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3208222222222",
    "long": "-6.25465277777778",
    "pronunciation": "Beechwood",
    "name": "Beechwood"
  },
  {
    "abrev": "COW",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3164666666667",
    "long": "-6.25344722222222",
    "pronunciation": "Cowper",
    "name": "Cowper"
  },
  {
    "abrev": "MIL",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3099166666667",
    "long": "-6.25172777777778",
    "pronunciation": "Milltown",
    "name": "Milltown"
  },
  {
    "abrev": "WIN",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.3015583333333",
    "long": "-6.25070833333333",
    "pronunciation": "Windy Arbour",
    "name": "Windy Arbour"
  },
  {
    "abrev": "DUN",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.2923583333333",
    "long": "-6.24511666666667",
    "pronunciation": "Dundrum",
    "name": "Dundrum"
  },
  {
    "abrev": "BAL",
    "isParkRide": "1",
    "isCycleRide": "1",
    "lat": "53.2861055555556",
    "long": "-6.23677222222222",
    "pronunciation": "Balally",
    "name": "Balally"
  },
  {
    "abrev": "KIL",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.2830083333333",
    "long": "-6.22388611111111",
    "pronunciation": "Kilmacud",
    "name": "Kilmacud"
  },
  {
    "abrev": "STI",
    "isParkRide": "1",
    "isCycleRide": "1",
    "lat": "53.2793111111111",
    "long": "-6.20991944444444",
    "pronunciation": "Stillorgan",
    "name": "Stillorgan"
  },
  {
    "abrev": "SAN",
    "isParkRide": "1",
    "isCycleRide": "1",
    "lat": "53.2776027777778",
    "long": "-6.20467777777778",
    "pronunciation": "Sandyford",
    "name": "Sandyford"
  },
  {
    "abrev": "CPK",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.27015",
    "long": "-6.20376388888889",
    "pronunciation": "Central Park",
    "name": "Central Park"
  },
  {
    "abrev": "GLE",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.2663361111111",
    "long": "-6.20994166666667",
    "pronunciation": "Glencairn",
    "name": "Glencairn"
  },
  {
    "abrev": "GAL",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.2611638888889",
    "long": "-6.20602222222222",
    "pronunciation": "The Gallops",
    "name": "The Gallops"
  },
  {
    "abrev": "LEO",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.2582472222222",
    "long": "-6.19836111111111",
    "pronunciation": "Leopardstown Valley",
    "name": "Leopardstown Valley"
  },
  {
    "abrev": "BAW",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.255047",
    "long": "-6.184475",
    "pronunciation": "Ballyogan Wood",
    "name": "Ballyogan Wood"
  },
  {
    "abrev": "CCK",
    "isParkRide": "0",
    "isCycleRide": "1",
    "lat": "53.2540333333333",
    "long": "-6.16990833333333",
    "pronunciation": "Carrickmines",
    "name": "Carrickmines"
  },
  {
    "abrev": "LAU",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.2506055555556",
    "long": "-6.15500555555556",
    "pronunciation": "Laughanstown",
    "name": "Laughanstown"
  },
  {
    "abrev": "CHE",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.2453333333333",
    "long": "-6.14585277777778",
    "pronunciation": "Cherrywood",
    "name": "Cherrywood"
  },
  {
    "abrev": "BRI",
    "isParkRide": "0",
    "isCycleRide": "0",
    "lat": "53.242075",
    "long": "-6.14288611111111",
    "pronunciation": "Bride's Glen",
    "name": "Bride's Glen"
  }
]


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
        self._stops = LUAS_STOPS

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
