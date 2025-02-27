# -*- coding: utf-8 -*-

"""
*******************
tests.conftest
*******************

Utility functions that are used to configure Py.Test context.

"""

import os
import pytest


def pytest_addoption(parser):
    """Define options that the parser looks for in the command-line.

    Pattern to use::

      parser.addoption("--cli-option",
                       action="store",
                       default=None,
                       help="cli-option: help text goes here")

    """
    parser.addoption("--inputs",
                     action="store",
                     default="/home/travis/build/highcharts-for-python/highcharts-gantt/tests/input_files",
                     help=("inputs: the absolute path to the directory where input"
                           " files can be found"))
    parser.addoption("--downloads",
                     action="store",
                     default="true",
                     help=("downloads: set to 'false' to disable tests of chart export "
                           "via the Highsoft-provided Export Server."))
    parser.addoption("--pyspark",
                     action="store",
                     default="false",
                     help=("pyspark: set to 'false' to disable tests of pyspark-related"
                           " functionality, or 'true' to enable those tests. Defaults to"
                           " 'false'"))


def pytest_runtest_makereport(item, call):
    """Connect current incremental test to its preceding parent."""
    # pylint: disable=W0212
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    """Fail test if preceding incremental test failed."""
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail(
                "previous test failed (%s) for reason: %s" % (previousfailed.name,
                                                              previousfailed))
