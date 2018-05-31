# Introduction 

[![Build Status](https://travis-ci.org/ronanmu/luas.py.svg?branch=master)](https://travis-ci.org/ronanmu/luas.py) [![Coverage Status](https://coveralls.io/repos/ronanmu/luas.py/badge.svg)](https://coveralls.io/r/ronanmu/luas.py) [![PyPI version](https://badge.fury.io/py/luas.py.svg)](https://badge.fury.io/py/luas.py)

luas.py is a python module providing an interface to the the Luas Forecasting API from [data.gov.ie](https://data.gov.ie/dataset/luas-forecasting-api/resource/078346e0-fe7f-4e71-9c51-21c78520dc3d). 

luas.py is licensed under the MIT license.

Getting started
===============

This module permits you to request:
* details for all trams at a stop
* trams in a particular direction at a stop

It validates that the stop names exist in data set available at [data.gov.ie](https://data.gov.ie/dataset/luas-network-2012-stops-itm). Note that the stop abbreviation or name can used when querying the Luas API, e.g.:

```commandline
'BAL' or 'Balally'
'RAN' or 'Ranelagh'
'MYS' or 'Mayor Square - NCI'
``` 



Requirements
------------

luas.py requires:
 * requests>=2.0


Install
-------
```commandline
pip install luas.py
```

# Usage

```python
import luas.api
from luas.api import LuasLine, LuasDirection

luas_client = luas.api.LuasClient()

# This will return the status text for the Green Line
green_line_status = luas_client.line_status(LuasLine.Green)

# This will return the next tram from Balally, in the default direction (inbound)
next_bal = luas_client.next_tram('BAL')

# This will return the next outbound tram from Ranelagh
next_ran = luas_client.next_tram('RAN', LuasDirection.Outbound)

# Return raw JSON for a stop
stop_details = luas_client.stop_details('Balally')

```

Developer
=========

luas.py is hosted by Github at https://github.com/ronanmu/luas.py.

Code has been tested with the following before commit:

```commandline
flake8 luas
pylint luas
coverage run --source luas -m unittest discover tests
```

Copyright (c) 2018 Ronan Murray.