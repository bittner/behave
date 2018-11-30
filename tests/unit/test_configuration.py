# -*- coding: UTF-8 -*-
"""
Unittests for :mod:`behave.configuration` module.
"""

from unittest.mock import patch

from behave.configuration import read_configuration


def configparser_get(*args, **kwargs):
    if args == ('behave', 'paths'):
        return ('\n'
                'tests/acceptance \n'
                '  test_app\n'
                'more/features')
    return None


@patch.object('ConfigParser', 'get', configparser_get)
def test_read_multiline_no_empty_lines(mock_configparser_get):
    """
    Multi-line strings must not have empty lines
    """
    result = read_configuration('/path/to/behave.ini')
    paths_list = result.get('paths')
    expected = [
        'tests/acceptance',
        'test_app',
        'more/features',
    ]

    assert '' not in paths_list, \
        "Empty lines in multiline sequence must be stripped away."
    assert paths_list == expected, "Unexpected content."
