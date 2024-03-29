[![pypi](https://img.shields.io/pypi/v/pycax-client.svg)](https://pypi.python.org/pypi-client/pycax-client)
[![github](https://img.shields.io/github/v/release/noaa-nwfsc/pycax?color=brightgreen&label=GitHub)](https://github.com/noaa-nwfsc/pycax/releases/latest)
[![docs](https://github.com/noaa-nwfsc/pycax/actions/workflows/deploy-docs.yml/badge.svg)](https://noaa-nwfsc.github.io/pycax)
[![tests](https://github.com/noaa-nwfsc/pycax/actions/workflows/tests.yml/badge.svg)](https://github.com/noaa-nwfsc/pycax/actions/workflows/tests.yml)
[![coverage](https://noaa-nwfsc.github.io/pycax/coverage.svg)](https://noaa-nwfsc.github.io/pycax/_codecoverage/index.html)
[![PyPi license](https://badgen.net/pypi/license/pycax-client/)](https://pypi.org/project/pycax-client/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7855729.svg)](https://doi.org/10.5281/zenodo.7855729)

pycax <img src="https://raw.githubusercontent.com/nwfsc-math-bio/pycax/main/docs/pycaxlogo.png" align="right" width="20%"  hspace="20" vspace="20"/>
========

<!--
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pycax-client.svg)](https://anaconda.org/conda-forge/pycax-client)
-->

pycax is a Python client for the Coordinated Assessments [REST API](https://www.streamnet.org/resources/exchange-tools/rest-api-documentation/). Make sure to review the [StreamNet Terms of Use](https://nwfsc-math-bio.github.io/rCAX/articles/terms.html) for these data, the [StreamNet Data Policy](https://www.streamnet.org/resources/exchange-tools/data-agreements/) and the [citation information](https://www.streamnet.org/resources/citing-sn/) for database queries. pycax was developed by the Northwest Fisheries Science Center Math Bio Program by Elizabeth Holmes and Mari Williams.

NWFSC Math Bio CAX REST API clients:

* Python client: [pycax on GitHub at noaa-nwfsc/pycax](https://github.com/noaa-nwfsc/pycax)
* R client: [rCAX on GitHub at nwfsc-math-bio/rCAX](https://github.com/nwfsc-math-bio/rCAX)

## Citation

Holmes, E. E and M. Williams. 2023. pycax: a Python client for the Coordinated Assessments data exchange REST API. vX.X.X. doi:10.5281/zenodo.7855729.

Make sure to include a citation for the Coordinated Assessments Partnership (CAP) data tables that you use. For details on citing CAP content see: https://www.streamnet.org/resources/citing-sn/

See [CITATION](https://github.com/noaa-nwfsc/pycax/blob/main/CITATION) file for bibtex version.

## Installation

From pypi

```bash
pip install pycax-client
```

From GitHub (development version)

```bash
pip install git+git://github.com/noaa-nwfsc/pycax.git#egg=pycax-client
```

## Documentation

The official documentation is hosted on GitHub Pages [https://noaa-nwfsc.github.io/pycax](https://noaa-nwfsc.github.io/pycax).

## Library API

`pycax` is split up into modules for each of the groups of API methods.

+ `hli` - Get HLI tables.
+ `datasets` - Get metadata of tables
+ `tables` - The workhorse modules for querying tables

## Sample analysis

Some Jupyter notebooks are in the [notebooks](https://github.com/noaa-nwfsc/pycax/tree/main/notebooks) directory.

## Contributing

Fork and put in a pull request!

To install editable dev version from github for local development. System prerequisites: python3, conda. Note replace `python3` with `python` if your Python installation points to 3+. `requirements-dev.txt` includes all the requirements needed for local development, testing and documentation building.

```bash
# fetch code
git clone git@github.com:noaa-nwfsc/pycax.git
cd pycax
# install the requirements
python3 -m pip install -r requirements.txt
python3 -m pip install -r requirements-dev.txt
# After making changes, reinstall using
python3 -m pip install -e .
# test your installation
python3 -m pytest
# test and generate a coverage report
python3 -m pytest -rxs --cov=pycax --cov-report term-missing ./pycax
# make the documentation in docs/_build/html
cd docs # pycax/docs
make clean html codecov # linkcheck # linkcheck not working
```

## Credits

Thanks to the developers of [pyobis](https://github.com/iobis/pyobis) package who created a package that was easy to use as a full template for a REST API client with tests, documentation files, and GitHub Actions and included the instructions and requirements for local development. The structure of pycax mimics pyobis structure but was adapted and changed for the CAX API. The [pygbif](https://github.com/gbif/pygbif) package is similar (and seems to have influenced pyobis). pygbif source was used for reference and study though no code directly used. Some pygbif code may appear in pycax if pyobis used pygbif functions for reference. Notably the Sphinx documentation configuration files seem to originate from pygbif.

## Contributors

[![Contributors](https://contrib.rocks/image?repo=noaa-nwfsc/pycax)](https://github.com/noaa-nwfsc/pycax/graphs/contributors)

<hr>

### Disclaimer

This repository is a scientific product and is not official communication of the National Oceanic and Atmospheric Administration, or the United States Department of Commerce. All NOAA GitHub project content is provided on an ‘as is’ basis and the user assumes responsibility for its use. Any claims against the Department of Commerce or Department of Commerce bureaus stemming from the use of this GitHub project will be governed by all applicable Federal law. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by the Department of Commerce. The Department of Commerce seal and logo, or the seal and logo of a DOC bureau, shall not be used in any manner to imply endorsement of any commercial product or activity by DOC or the United States Government.

### License

This content was created by U.S. Government employees as part of their official duties. This content is not subject to copyright in the United States (17 U.S.C. §105) and is in the public domain within the United States of America. Additionally, copyright is waived worldwide through the MIT License.


