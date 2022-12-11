"""
Query for a HLI base or XPort table

/ca?table_id=<id> API endpoint with id equal to one of the HLI or HLI_XPort table ids
"""
import pandas as pd

from ..caxutils import build_api_url, handle_arrstr, cax_baseurl, cax_GET

from pycax import tables

# Set up the variables

HLI_SHORT = {"NOSA", "SAR", "PNI", "JuvOut", "PreSmolt", "RperS"}
HLI_TABLENAMES = { 
    'base': {
        'NOSA': 'NOSA',  'SAR': 'SAR',  'PNI': 'PNI', 
        'JuvOut': 'JuvenileOutmigrants',  'PreSmolt': 'PresmoltAbundance', 
        'RperS': 'RperS'
        },
    'xport': {}
    }
for key in HLI_TABLENAMES['base']:
    HLI_TABLENAMES['xport'][key] = 'XPortCA_'+HLI_TABLENAMES['base'][key]+'_01'
 
def return_tablename(hli, tabletype):
    """
    Retrieve a table name for a hli short code for base or xport table type

    :param hli: [String] A HLI short code: NOSA, SAR, PNI, JuvOut, PreSmolt, RperS
    :param tabletype: [String] "base" or "xport"
    :return: A table name as a string

    Usage::

        from pycax import hli
        hli.tablename('NOSA', 'base')
    """
    valid = HLI_SHORT
    if status not in valid:
        raise ValueError("hli must be one of %r." % valid)
    
    return HLI_TABLENAMES[hli, tabletype]

def get(hli, tabletype="xport", args={}, fargs={}, **kwargs):
    """
    Get a table using the table name from /ca/tables API: pycax.datasets.getdf()

    :param hli: [String] A HLI short code: NOSA, SAR, PNI, JuvOut, PreSmolt, RperS
    :param tabletype: [String] 'base' or 'xport'
    :param args: [dict] a dictionary of query parameters. The default is no parameters. See usage for common query parameters
    :param fargs: [dict] a dictionary of filter values as {colname1: value}, {colname1: [value1, value2]} or {colname1: value, colname2: value}. The default is no filter. See usage for examples.

    :return: A dictionary of class HliResponse ready for execution

    Usage::

        from pycax import hli
        query = hli.get('NOSA', 'base', args={'limit': 1})
        query.execute()
        query.data # get the data
        query.api_url # get the API url

    """
    tablename = return_tablename(hli, tabletype)
    if len(fargs)>1: args['filter'] = tables.dict_to_json(fargs)

    return tables.TablesResponse(tablename, args)

def getdf(hli, tabletype="xport", args={}, fargs={}, **kwargs):
    """
    Get a HLI table and return a data frame

    :param hli: [String] A HLI short code: NOSA, SAR, PNI, JuvOut, PreSmolt, RperS
    :param tabletype: [String] 'base' or 'xport'
    :param args: [dict] a dictionary of query parameters. The default is no parameters. See usage for common query parameters
    :param fargs: [dict] a dictionary of filter values as {colname1: value}, {colname1: [value1, value2]} or {colname1: value, colname2: value}. The default is no filter. See usage for examples.

    :return: A dictionary of class HliResponse ready for execution

    Usage::

        from pycax import hli
        res = hli.getdf('NOSA', 'base', fargs={'popid': 7})
        res.head()

    """
    tablename = return_tablename(hli, tabletype)
    if len(fargs)>1: args['filter'] = tables.dict_to_json(fargs)

    return tables.TablesResponse(tablename, args)

