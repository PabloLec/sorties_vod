#! /usr/bin/python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/whatsnew/')
from mainscript import app as application
application.secret_key = '0397'

