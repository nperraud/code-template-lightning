packagename: Template for Python packages with pytorch lightning
=================================================================

**The first thing you need to do is to replace `packagename` in all files with the name of your package.
Then rename the folder `packagename` to the name of your package.**

Once this is done, you can proceed with the instatllation of the package as described below.


Getting started
===============

To get started, make sure you have the necessary permissions and clone the repository:

.. code-block:: bash

   git clone 
   cd leap

Working with Poetry
====================

To install Poetry, run the following command in the terminal:

.. code-block:: bash

   curl -sSL https://install.python-poetry.org | python3 -

Activate the Poetry shell and install the dependencies:

.. code-block:: bash

   poetry shell
   poetry install

To add an additional package to the project, use the add command. For example:

.. code-block:: bash

   poetry add numpy

To run tests, use the following command:

.. code-block:: bash

    pytest .

The tests code are located in the folder packagename/tests.

Tests
-----

The tests are located in the folder packagename/tests. The tests are run using pytest. To run the tests, use the following command:

```bash
pytest packagename
```
or
```bash
make test
```


Documentation
-------------

Check the sphynx documentation in the folder doc. Update the documentation accordingly.

You can compile the doc using the following command:

```bash
make doc
```

Style and linting
-----------------

The code is linted using flake8. To run the linter, use the following command:

```bash
flake8 --doctests --exclude=doc --ignore=E501
```
or
```bash
make lint
```

To help you to get the right format, you can use `black`:
```bash
black packagename
```

Package information
-------------------

The package information is stored in the file pyproject.toml. Update the information accordingly.



TODOs
-----
