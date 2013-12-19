"""
WSGI interface to the Mutalyzer HTTP/RPC+JSON webservice.

Example Apache/mod_wsgi configuration:

    WSGIScriptAlias /json /usr/local/bin/mutalyzer-service-json

Be sure to have this line first if you also define a / alias, like this:

    WSGIScriptAlias /json /usr/local/bin/mutalyzer-service-json
    WSGIScriptAlias / /usr/local/bin/mutalyzer-website

You can also use the built-in HTTP server by running this file directly.
"""


import argparse
import sys

from wsgiref.simple_server import make_server
from spyne.server.wsgi import WsgiApplication

from ..services import json


application = WsgiApplication(json.application)


def debugserver(port):
    """
    Run the webservice with the Python built-in HTTP server.
    """
    sys.stderr.write('Listening on http://localhost:%d/\n' % port)
    make_server('localhost', port, application).serve_forever()


def main():
    """
    Command-line interface to the HTTP/RPC+JSON webservice.
    """
    parser = argparse.ArgumentParser(
        description='Mutalyzer HTTP/RPC+JSON webservice.')
    parser.add_argument(
        '-p', '--port', metavar='NUMBER', dest='port', type=int,
        default=8082, help='port to run the webservice on (default: 8082)')

    args = parser.parse_args()
    debugserver(args.port)


if __name__ == '__main__':
    main()