"""
Utility functions for internal use across various modules.
"""
from urllib.parse import urlencode

import requests
import pkgutil
import pycax

cax_baseurl = "https://api.streamnet.org/api/v1/"

cax_api_key = "7A2F1EA9-4882-49E8-B23D-7DC202C2ACA5"

class NoResultException(Exception):
    """
    Thrown when query returns no results.
    """

    pass


def build_api_url(url, args):
    """
    Builds the API URL based on the base url and the arguments
    """
    return url + "?" + urlencode({k: v for k, v in args.items() if v is not None})

def make_ua():
    return {
        "user-agent": "python-requests/"
        + requests.__version__
        + ",pycax/"
        + pycax.__version__
    }

def cax_GET(url, args, **kwargs):
    """
    Handles technical details of sending GET request to the API
    """
    args['XApiKey']=cax_api_key
    out = requests.get(url, params=args, headers=make_ua(), **kwargs)
    out.raise_for_status()
    stopifnot(out.headers["content-type"])
    return out.json()
    

def cax_write_disk(url, path, **kwargs):
    out = requests.get(url, stream=True, **kwargs)
    out.raise_for_status()
    with open(path, "wb") as f:
        for chunk in out.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return path


def stopifnot(x, ctype="application/json;charset=utf-8"):
    if x != ctype:
        raise NoResultException("content-type did not equal " + str(ctype))


def stop(x):
    raise ValueError(x)


def handle_arrstr(x):
    """Converts array arguments into comma-separated strings if applicable."""
    if x.__class__.__name__ == "NoneType":
        pass
    else:
        if x.__class__.__name__ == "str":
            return x
        else:
            return ",".join(x)


def handle_arrint(x):
    """Converts array arguments into comma-separated integers if applicable."""
    if x.__class__.__name__ == "NoneType":
        pass
    else:
        if x.__class__.__name__ == "int":
            return x
        else:
            x = list(map(str, x))
            return ",".join(x)

def as_list(x):
    if type(x) is list:
        return x
    else:
        return [x]

def get_data(filename):
    # Read the data file
    data = pkgutil.get_data('pycax', 'data/' + filename)

    # Return the data
    return data
