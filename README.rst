gmt2sed
================

Compute galaxy SEDs from HACC hydro galaxy merger trees

Installation
------------
To install gmt2sed into your environment from the source code::

    $ cd /path/to/root/gmt2sed
    $ python setup.py install

Documentation
-------------
Online documentation for gmt2sed is available at 
`gmt2sed.readthedocs.io <https://gmt2sed.readthedocs.io/en/latest/>`_.

Testing
-------
To run the suite of unit tests::

    $ cd /path/to/root/gmt2sed
    $ pytest

To build html of test coverage::

    $ pytest -v --cov --cov-report html
    $ open htmlcov/index.html

