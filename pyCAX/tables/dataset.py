"""
ca/tables/ API endpoints.
"""

import pandas as pd

from ..caxutils import build_api_url, handle_arrstr, cax_baseurl, cax_GET

def get(**kwargs):
    """
    Get tables

    :param id: [Fixnum] An OBIS dataset identifier.

    :return: A DatasetResponse object

    Usage::

        from pyCAX import tables
        query = tables.get()
        query.execute() # execute the query
        query.data # returns the data of the query
        query.api_url # returns the CAX API URL
    """
    url = cax_baseurl + "ca/tables/"
    args = {}
  
    # returns a DatasetResponse object
    return DatasetResponse(url, args)


class DatasetResponse:
    """
    An CAX Dataset Response Object
    """

    def __init__(self, url, args):
        """
        Initialise the object parameters
        """
        # public members
        self.data = None
        self.api_url = build_api_url(url, args)
        self.mapper_url = None
    
        # private members
        self.__args = args
        self.__url = url

    def execute(self, **kwargs):
        """
        Execute or fetch the data based on the query
        """
        out = cax_GET(
            self.__url, self.__args, "application/json; charset=utf-8", **kwargs
        )
        self.data = out
        return self.data

    def to_pandas(self):
        """
        Convert the results into a pandas DataFrame
        """
        return pd.DataFrame(self.data["results"])
