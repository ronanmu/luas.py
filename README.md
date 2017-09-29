# Introduction [![Build Status](https://travis-ci.org/ronanmu/luas.py.svg?branch=master)](https://travis-ci.org/ronanmu/luas.py) [![Coverage Status](https://coveralls.io/repos/ronanmu/luas.py/badge.svg)](https://coveralls.io/r/ronanmu/luas.py)
luas.py is a python module providing a simple interface to the Dublin Luas API
luas.py is licensed under the MIT license.

Getting started
===============

luas.py uses the Luas Forecasting API from data.gov.ie. 

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
from luas.api import LuasLine

# This will use http by default (not https)
luas_client = luas.api.LuasClient()

green_line_status = luas_client.line_status(LuasLine.Green)
```
n

Developer
=========

luas.py is hosted by Github at https://github.com/ronanmu/luas.py.

Code has been tested with the following before commit:

```python
flake8 openwebif
pylint openwebif
coverage run -m unittest discover tests
```

Copyright (c) 2017 Ronan Murray.