"""
luas.api
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides methods for interrogating Dublin's Luas tram API

Copyright (c) 2017 Ronan Murray <https://github.com/ronanmu>
Licensed under the MIT License
"""

import logging
from luas.models import LuasLine
from xml.etree import ElementTree
import requests

_LOGGER = logging.getLogger(__name__)

DEFAULT_LUAS_API = "http://luasforecasts.rpa.ie/xml/get.ashx"
DEFAULT_PARAMS = {'action': 'forecast', 'encrypt': 'false', 'stop': ''}
DEFAULT_GREEN_LINE_STOP = 'STS'
DEFAULT_RED_LINE_STOP = 'TAL'


class LuasClient(object):
    """
    Create new Luas API client interface
    """

    def __init__(self, apiEndpoint=None):

        logging.basicConfig(level=logging.DEBUG)
        if not apiEndpoint:
            apiEndpoint = DEFAULT_LUAS_API

        _LOGGER.debug("Using API at %s", apiEndpoint)
        self._apiEndpoint = apiEndpoint

    def line_status(self, line=LuasLine.Green):
        """
        Fetches the status of the Luas line
        """

        luas_params = DEFAULT_PARAMS
        if line == LuasLine.Green:
            luas_params['stop'] = DEFAULT_GREEN_LINE_STOP
        else:
            luas_params['stop'] = DEFAULT_RED_LINE_STOP

        response = requests.get(self._apiEndpoint, params=luas_params)

        if response.status_code == 200:
            _LOGGER.info('Response %s', response.content)
            try:
                tree = ElementTree.fromstring(response.content)
                result = tree.findall(".//message")
                return result[0].text.strip()

            except AttributeError as attib_err:
                _LOGGER.error(
                    'There was a problem parsing the Luas API response %s'
                    , attib_err)
                _LOGGER.error('Entire response: %s', response.content)
                return
        return

    def next_tram(self, stop, direction=None):
        """
        Selects the next tram available from selected stop
        """

        luasApiParams = {'action': 'forecast', 'encrypt': 'false', 'stop': stop}

        response = requests.get(self._apiEndpoint, params=luasApiParams)

        if response.status_code == 200:
            _LOGGER.debug('Response received for %s', stop)
            #try:
            #    tree = ElementTree.fromstring(response.content)
            #    result

        return self._check_response_result(response)

    @staticmethod
    def _check_response_result(response):
        """

        :param response:
        :return Returns value
        """

        if response.status_code != 200:
            _LOGGER.error("an error occured %s", response.status_code)

        return response.json()['result']
