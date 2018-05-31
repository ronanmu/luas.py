"""
luas.api
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides methods for interrogating Dublin's Luas tram API

Copyright (c) 2018 Ronan Murray <https://github.com/ronanmu>
Licensed under the MIT License
"""

import logging
from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError
import requests
from luas.models import LuasLine, LuasDirection, LuasTram, LuasStops

_LOGGER = logging.getLogger(__name__)

ATTR_STATUS = 'status'
ATTR_TRAMS = 'trams'
ATTR_DUE = 'due'
ATTR_DESTINATION = 'destination'
ATTR_DIRECTION = 'direction'
ATTR_ABBREV = 'abrev'

ATTR_INBOUND_VAL = 'Inbound'
ATTR_OUTBOUND_VAL = 'Outbound'

DEFAULT_LUAS_API = "http://luasforecasts.rpa.ie/xml/get.ashx"
DEFAULT_PARAMS = {'action': 'forecast', 'encrypt': 'false', 'stop': ''}
DEFAULT_GREEN_LINE_STOP = 'STS'
DEFAULT_RED_LINE_STOP = 'TAL'
ATTR_STOP_VAL = 'stop'
ATTR_DUE_VAL = 'dueMins'
ATTR_DESTINATION_VAL = 'destination'
ATTR_NO_TRAMS = 'No trams forecast'

XPATH_STATUS = ".//message"
XPATH_DIRECTION_INBOUND = ".//direction[@name='Inbound']/tram"
XPATH_DIRECTION_OUTBOUND = ".//direction[@name='Outbound']/tram"


class LuasClient(object):
    """
    Create new Luas API client interface
    """

    def __init__(self, api_endpoint=None, use_gzip=True):

        if not api_endpoint:
            api_endpoint = DEFAULT_LUAS_API

        _LOGGER.debug("Using API at %s", api_endpoint)

        self._api_endpoint = api_endpoint
        self._use_gzip = use_gzip
        self._session = requests.Session()
        self._stops = LuasStops()

    def stop_details(self, stop):
        """
        Returns raw JSON of the Luas details from the requested stop.
        :param stop: Stop to enquire about
        :return:
        """
        response = {
            ATTR_STATUS: 'n/a',
            ATTR_TRAMS: []
        }

        luas_params = DEFAULT_PARAMS
        selected_stop = self._stops.stop(stop)
        if selected_stop is None:
            _LOGGER.error("Stop '%s' is not valid", stop)
            return response

        DEFAULT_PARAMS[ATTR_STOP_VAL] = selected_stop[ATTR_ABBREV]

        if self._use_gzip:
            self._session.headers.update({'Accept-Encoding': 'gzip'})

        api_response = self._session.get(self._api_endpoint,
                                         params=luas_params)

        if api_response.status_code == 200:
            _LOGGER.debug('Response received for %s', stop)
            try:
                tree = ElementTree.fromstring(api_response.content)
                status = tree.find(XPATH_STATUS).text.strip()
                trams = []

                result = tree.findall(XPATH_DIRECTION_INBOUND)
                if result is not None:
                    for tram in result:
                        if tram.attrib[ATTR_DESTINATION_VAL] != ATTR_NO_TRAMS:
                            trams.append({
                                ATTR_DUE: tram.attrib[ATTR_DUE_VAL],
                                ATTR_DIRECTION: ATTR_INBOUND_VAL,
                                ATTR_DESTINATION:
                                    tram.attrib[ATTR_DESTINATION_VAL]
                            })

                result = tree.findall(XPATH_DIRECTION_OUTBOUND)
                if result is not None:
                    for tram in result:
                        if tram.attrib[ATTR_DESTINATION_VAL] != ATTR_NO_TRAMS:
                            trams.append({
                                ATTR_DUE: tram.attrib[ATTR_DUE_VAL],
                                ATTR_DIRECTION: ATTR_OUTBOUND_VAL,
                                ATTR_DESTINATION:
                                    tram.attrib[ATTR_DESTINATION_VAL]
                            })

                response[ATTR_STATUS] = status
                response[ATTR_TRAMS] = trams
            except ParseError as parse_err:
                _LOGGER.error(
                    'There was a problem parsing the Luas API response %s',
                    parse_err
                )
                _LOGGER.error('Entire response %s', api_response.content)
            except AttributeError as attib_err:
                _LOGGER.error(
                    'There was a problem parsing the Luas API response %s',
                    attib_err)
                _LOGGER.error('Entire response: %s', api_response.content)

        else:
            _LOGGER.error(
                'HTTP error processing Luas response %s',
                api_response.status_code
            )

        return response

    def line_status(self, line=LuasLine.Green):
        """
        Fetches the status of the line in questions
        :param line: Luas line in question
        :return: text description of the current line status
        """

        stop = DEFAULT_GREEN_LINE_STOP
        if line == LuasLine.Red:
            stop = DEFAULT_RED_LINE_STOP

        response = self.stop_details(stop)
        return response[ATTR_STATUS]

    def all_trams(self, stop):
        """
        Returns all trams from the provided stop
        :param stop: stop to search from
        :return: list of all trams
        """
        stop_details = self.stop_details(stop)
        trams = []

        for tram in stop_details[ATTR_TRAMS]:
            trams.append(self._build_luas_tram_from_map(tram))

        return trams

    def next_tram(self, stop, direction=LuasDirection.Inbound):
        """
        Retrieves the next tram departing from the requested stop
        in the requested direction
        :param stop: Stop name
        :param direction: Luas Direction
        :return: LuasTram contain next tram details
        """

        stop_details = self.stop_details(stop)
        output_tram = None
        for tram in stop_details[ATTR_TRAMS]:
            if direction == LuasDirection.Inbound \
                    and tram[ATTR_DIRECTION] == ATTR_INBOUND_VAL:
                output_tram = tram
                break
            elif direction == LuasDirection.Outbound \
                    and tram[ATTR_DIRECTION] == ATTR_OUTBOUND_VAL:
                output_tram = tram
                break

        return self._build_luas_tram_from_map(output_tram)

    @staticmethod
    def _build_luas_tram_from_map(tram):
        if tram is not None:
            direction = LuasDirection.Inbound
            if tram[ATTR_DIRECTION] == ATTR_OUTBOUND_VAL:
                direction = LuasDirection.Outbound

            return LuasTram(
                tram[ATTR_DUE],
                direction,
                tram[ATTR_DESTINATION]
            )
        else:
            return None
