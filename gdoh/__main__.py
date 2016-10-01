"""gdoh

Usage:
    gdoh <domain> type <records>... [options]

Options:
    -d, --dnssec                            Enables DNSSEC [default: False].
    -e <subnet>, --edns <subnet>            EDNS client subnet to be sent.
    -h, --help                              Show this page.
    -v, --version                           Show the application version.
"""

from docopt import docopt

from . import gdoh
from . import gdohtable


def main():
    args = docopt(__doc__, version='gdoh.py 1.0')
    g = gdoh.GDoH(args['<domain>'],
                  args['<records>'],
                  args['--dnssec'],
                  args['--edns'])
    for t in gdohtable.to_table(g.resolve()):
        print t
        print

if __name__ == "__main__":
    main()
