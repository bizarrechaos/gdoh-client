import requests


class GDoH(object):
    """docstring for GDoH."""
    def __init__(self, domain, records, dnssec, edns):
        super(GDoH, self).__init__()
        self.baseurl = 'https://dns.google.com/resolve?'
        self.domain = domain
        self.records = records
        self.dnssec = dnssec
        self.edns = edns

    def resolve(self):
        responselist = []
        for record in self.records:
            if self.edns is None:
                url = '{0}name={1}&type={2}&cd={3}'.format(self.baseurl,
                                                           self.domain,
                                                           record,
                                                           self.dnssec)
            else:
                url = ('{0}name={1}&type={2}&cd={3}&edns_client_subnet={4}'
                       .format(self.baseurl,
                               self.domain,
                               record,
                               self.dnssec,
                               self.edns))
            r = requests.get(url)
            if r.ok:
                if r.json():
                    responselist.append(r.json())
        return responselist
