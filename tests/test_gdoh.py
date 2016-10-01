import json
import pytest
import responses

from gdoh import gdoh


class TestGDoH(object):

    def test_gdoh(self):
        g = gdoh.GDoH('example.com', ['A', 'CNAME', 'MX'], True, '0.0.0.0/0')
        assert g.domain == 'example.com'
        assert g.baseurl == 'https://dns.google.com/resolve?'
        assert g.records == ['A', 'CNAME', 'MX']
        assert g.dnssec
        assert g.edns == '0.0.0.0/0'

    @responses.activate
    def test_resolve_with_edns(self):
        g = gdoh.GDoH('example.com', ['A', 'CNAME', 'MX'], True, '0.0.0.0/0')
        responses.add(responses.GET,
                      'https://dns.google.com/resolve',
                      status=200,
                      body=json.dumps({'test': ['test']}))
        assert g.resolve() == [{u'test': [u'test']},
                               {u'test': [u'test']},
                               {u'test': [u'test']}]

    @responses.activate
    def test_resolve_without_edns(self):
        g = gdoh.GDoH('example.com', ['A', 'CNAME', 'MX'], True, None)
        responses.add(responses.GET,
                      'https://dns.google.com/resolve',
                      status=200,
                      body=json.dumps({'test': ['test']}))
        assert g.resolve() == [{u'test': [u'test']},
                               {u'test': [u'test']},
                               {u'test': [u'test']}]
