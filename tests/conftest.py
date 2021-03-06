from __future__ import print_function, division, absolute_import

import os

import pytest
import sqlalchemy

from framequery.util._record import Record, diff


@pytest.fixture(scope='module')
def database():
    if 'FQ_TEST_DB' in os.environ:
        return sqlalchemy.create_engine(os.environ['FQ_TEST_DB'])

    pytest.skip('test db not available')


def pytest_assertrepr_compare(op, left, right):
    if not(isinstance(left, Record) and isinstance(right, Record) and op == "=="):
        return

    return [
        'Comparing Records',
        '%r != %r' % (left, right),
    ] + list(diff(left, right))
