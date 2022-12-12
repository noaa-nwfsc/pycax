pycax
======

|pypi| |docs|

Python client for the `CAX API
<https://api.streamnet.org/api/v1>`__.

`Source on GitHub at nwfsc-math-bio/pycax <https://github.com/nwfsc-math-bio/pycax>`__

Other CAX clients:

* R: `rCAX`, `nwfsc-math-bio/rCAX <https://nwfsc-math-bio.github.io/rCAX>`__

Installation
============

from pypi

.. code-block:: console

    pip install pycax

dev version

.. code-block:: console

    pip install git+git://github.com/nwfsc-math-bio/pycax.git#egg=pycax


Library API
===========

``pycax`` is split up into modules for the list of tables (/ca/tables) and individual tables (/ca?table_id=...).

* ``datasets`` - The tables available for download with metadata.
* ``tables`` - Download an individual table given its name (as in the datasets table)
* ``hli`` - Download a HLI table in either "XPort" or base format. "XPort" is the same as the CAP Tabular Query.

For accessing the HLI tables, you only need to import the hli module. A maximum of 1000 rows of data are downloaded (by default).
Typically you will want to filter the query by passing in `fargs` as dictionary with the column name values. For example,
`{'popid': 7}` would return popid equal to 7 only.

Examples of functions returning the data as a pandas data frame are shown.

HLI module
###########

.. code-block:: python

    from pycax import hli

    res = hli.getdf("NOSA", tabletype="xport", fargs={'popid':  7})
    res.head()


Tables module
#################

.. code-block:: python

    from pycax import tables

    res = tables.getdf("EscData", fargs={'popid':  7})
    res.head()

Datasets module
##############

.. code-block:: python

    from pycax import datasets

    res = datasets.getdf()
    res['name', 'id'].head()

Meta
====

* License: MIT

.. |pypi| image:: https://img.shields.io/pypi/v/pycax.svg
   :target: https://pypi.python.org/pypi/pycax

.. |docs| image:: https://github.com/nwfsc-math-bio/pycax/actions/workflows/deploy-docs.yml/badge.svg
   :target: https://nwfsc-math-bio.github.io/pycax



Contents
========

.. toctree::
   :maxdepth: 2

   hli
   tables
   datasets
   changelog_link

License
=======

MIT


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
