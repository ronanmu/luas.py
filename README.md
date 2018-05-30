# Introduction [![Build Status](https://travis-ci.org/ronanmu/luas.py.svg?branch=master)](https://travis-ci.org/ronanmu/luas.py) [![Coverage Status](https://coveralls.io/repos/ronanmu/luas.py/badge.svg)](https://coveralls.io/r/ronanmu/luas.py)
luas.py is a python module providing a simple interface to the Dublin Luas API
luas.py is licensed under the MIT license.

Getting started
===============

luas.py uses the Luas Forecasting API from [data.gov.ie](https://data.gov.ie/dataset/luas-forecasting-api/resource/078346e0-fe7f-4e71-9c51-21c78520dc3d).

Requirements
------------

luas.py requires:
 * requests>=2.0


Install
-------
```python
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
next_bal = client.next_tram('BAL')

# This will return the next outbound tram from Ranelagh
next_ran = client.next_tram('RAN', LuasDirection.Outbound)

# Return raw JSON for a stop
stop_details = client.stop_details('BAL')

```

Developer
=========

luas.py is hosted by Github at https://github.com/ronanmu/luas.py.

Code has been tested with the following before commit:

```python
flake8 luas
pylint luas
coverage run --source luas -m unittest discover tests
```

Copyright (c) 2018 Ronan Murray.