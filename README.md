#:card_index: gdoh-client [![Build Status](https://travis-ci.org/bizarrechaos/gdoh-client.svg?branch=master)](https://travis-ci.org/bizarrechaos/gdoh-client)

Python libraries and command line interface for Google's DNS-over-HTTPS

####Installation:

You can install the latest available version of gdoh-client from GitHub using pip:

```
pip install git+git://github.com/bizarrechaos/gdoh-client.git
```

You can also clone the repository and install gdoh-client:

```
git clone https://github.com/bizarrechaos/gdoh-client.git
cd gdoh-client
python setup.py install
```

####Usage overview:
```
gdoh

Usage:
    gdoh <domain> type <records>... [options]

Options:
    -d, --dnssec                            Enables DNSSEC [default: False].
    -e <subnet>, --edns <subnet>            EDNS client subnet to be sent.
    -h, --help                              Show this page.
    -v, --version                           Show the application version.
```

######powered by [Google DNS-over-HTTPS](https://developers.google.com/speed/public-dns/docs/dns-over-https)
