======================
Setuptools-LocalImport
======================

Shim to Setuptools's PEP 517 build backend to patch `sys.path`. An attempt to
work around `pypa/pip#6163`_.

.. _`pypa/pip#6163`: https://github.com/pypa/pip/issues/6163


Usage
=====

Add the followings to your pyproject.toml::

    [build-system]
    requires = ["setuptools-localimport"]
    build-backend = "setuptools_localimport"
