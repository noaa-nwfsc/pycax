"""Tests for tables module methods"""
import requests
import json

from pycax import tables
  
def test_tables_tableid():
    """
    tables.tableid - test that only one value returned
    """
    res = tables.tableid("NOSA")
    assert "ndarray" == res.__class__.__name__
    assert 1 == len(res)
    assert "str" == res[0].__class__.__name__

def test_tables_get():
    """
    tables.get - basic test for data, check type, size and other methods
    """
    query = tables.get("NOSA", args={'limit': 1})
    assert not query.data
    query.execute()
    assert "dict" == query.data.__class__.__name__
    assert 6 == len(query.data)
    assert list == list(query.data.keys()).__class__
    assert query.to_pandas().__class__.__name__ == "DataFrame"

def test_dict_to_json():
    """
    tables.dict_to_json - basic test for structure
    """
    res = tables.dict_to_json({'popid': '7'})
    assert "str" == res.__class__.__name__
    dictlist = json.loads(res)
    assert "list" == dictlist.__class__.__name__
    assert "dict" == dictlist[0].__class__.__name__
    dictkeys = [key for key in dictlist[0]]
    dictvals = [dictlist[0][key] for key in dictlist[0]]
    assert dictkeys == ['field', 'value', 'type']
    assert dictvals == ['popid', '7', 'string']
  