"""
pyCAX library
~~~~~~~~~~~~~~~~~~~~~

pyCAX is a Python client for CAX.

Example usage:

# Import entire library
import pyCAX
# or import modules as needed
## hli_xport
from pyCAX import hli_xport
## hli
from pyCAX import hli
## tables
from pyCAX import tables
## utils
from pyCAX import utils

## use advanced logging
### setup first
import requests
import logging
import httplib as http_client
http_client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
### then make request
#from pyCAX import hli_xport
#occurrence.search(geometry='POLYGON((30.1 10.1, 10 20, 20 40, 40 40, 30.1 10.1))')
"""

try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"

__title__ = "pyCAX"
__author__ = "Eli Holmes and Mari Williams"
__license__ = "MIT"

from .hli_xport import hli_xport
from .hli import hli
from .tables import tables
from .utils import utils

__all__ = [
    "hli_xport",
    "hli",
    "tables",
    "utils",
]
