import pytest

from prettytable import PrettyTable

from gdoh import gdohtable


class TestGdohTable(object):

    def test_to_table(self):
        t = gdohtable.to_table([{'Answer': [{'name': 'test',
                                             'data': 'test',
                                             'TTL': 'test'}]}])
        assert isinstance(t[0], type(PrettyTable([])))
