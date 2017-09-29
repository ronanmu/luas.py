"""
luas.api
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides methods for interrogating Dublin's Luas tram API

Copyright (c) 2017 Ronan Murray <https://github.com/ronanmu>
Licensed under the MIT License
"""

import logging
from xml.etree import ElementTree
from luas.models import LuasLine, LuasDirection, LuasTram
import requests

_LOGGER = logging.getLogger(__name__)

DEFAULT_LUAS_API = "http://luasforecasts.rpa.ie/xml/get.ashx"
DEFAULT_PARAMS = {'action': 'forecast', 'encrypt': 'false', 'stop': ''}
DEFAULT_GREEN_LINE_STOP = 'STS'
DEFAULT_RED_LINE_STOP = 'TAL'
ATTR_STOP_VAL = 'stop'
ATTR_DUE_VAL = 'dueMins'
ATTR_DESTINATION_VAL = 'destination'

XPATH_STATUS = ".//message"
XPATH_DIRECTION_INBOUND = ".//direction[@name='Inbound']/tram"
XPATH_DIRECTION_OUTBOUND = ".//direction[@name='Outbound']/tram"


class LuasClient(object):
    """
    Create new Luas API client interface
    """

    def __init__(self, api_endpoint=None):

        if not api_endpoint:
            api_endpoint = DEFAULT_LUAS_API

        _LOGGER.debug("Using API at %s", api_endpoint)
        self.api_endpoint = api_endpoint

    def line_status(self, line=LuasLine.Green):
        """
        Fetches the status of the Luas line
        """

        luas_params = DEFAULT_PARAMS
        if line == LuasLine.Green:
            luas_params[ATTR_STOP_VAL] = DEFAULT_GREEN_LINE_STOP
        else:
            luas_params[ATTR_STOP_VAL] = DEFAULT_RED_LINE_STOP

        response = requests.get(self.api_endpoint, params=luas_params)

        if response.status_code == 200:
            _LOGGER.info('Response %s', response.content)
            try:
                tree = ElementTree.fromstring(response.content)
                result = tree.findall(XPATH_STATUS)
                return result[0].text.strip()

            except AttributeError as attib_err:
                _LOGGER.error(
                    'There was a problem parsing the Luas API response %s',
                    attib_err)
                _LOGGER.error('Entire response: %s', response.content)
                return
        return

    def next_tram(self, stop, direction=LuasDirection.Inbound):
        """
        Selects the next tram available from selected stop
        """

        luas_params = DEFAULT_PARAMS
        DEFAULT_PARAMS[ATTR_STOP_VAL] = stop
        response = requests.get(self.api_endpoint, params=luas_params)

        if response.status_code == 200:
            _LOGGER.debug('Response received for %s', stop)
            try:
                tree = ElementTree.fromstring(response.content)
                direction_xpath = XPATH_DIRECTION_INBOUND
                if direction == LuasDirection.Outbound:
                    direction_xpath = XPATH_DIRECTION_OUTBOUND

                result = tree.findall(direction_xpath)
                if result is not None and result[0] is not None:
                    return LuasTram(result[0].attrib[ATTR_DUE_VAL],
                                    direction,
                                    result[0].attrib[ATTR_DESTINATION_VAL])

            except AttributeError as attib_err:
                _LOGGER.error(
                    'There was a problem parsing the Luas API response %s',
                    attib_err)
                _LOGGER.error('Entire response: %s', response.content)
                return
        else:
            _LOGGER.error(
                'HTTP error processing Luas response %s', response.status_code
            )

        return
