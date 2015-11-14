from flask import Flask
from flask import request
import os
import random
import logging
import sys
from socket import gethostname

app = Flask(__name__)
redis_cli = None

logger = logging.getLogger()

@app.route("/")
def index():
    index = """
<html>
    <body>
        <h1>Tsuru test</h1>
        <ul>
            <li><a href="/print?string=bonjour">Print string 'bonjour'</a></li>
        </ul>
    </body>
</html>
"""
    logger.debug(gethostname() + ": index")
    return index

@app.route("/print")
def print_string():
    string = request.args.get('string', 'no string to print')
    logger.debug(gethostname() + ": print string " + string)
    return string

if __name__ == "__main__":
    bind_port = int(os.environ.get('PORT', '1234'))
 
    debug_string = os.environ.get('DEBUG', 'false')
    if debug_string.lower() == 'true':
        debug = True
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    else:
        debug = False
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    app.run(host = '0.0.0.0', port = bind_port, debug = debug)