"""Hit enable.txconvergent.org every 29 minutes.
"""

import sys
import requests
import time

from datetime import datetime

URL = 'http://enable.txconvergent.org'


def stayin_alive():
    print("hello")
    while True:
        print("You're stayin' alive, stayin alive 😎")
        r = requests.get(URL)
        print(r.status_code)
        if r.status_code != 200:
            with open("{}".format('.'.join((datetime.now().strftime('%Y-%m-%d.%H:%M:%S'), 'enable', 'log'))), 'w') as f:
                f.write("{}\n\n{}\n\n{}".format(r.status_code, r.reason, r.text))
            print("Stop right there! 🚔 ")
            sys.exit("goodbye")
        time.sleep(1740)


if __name__ == "__main__":
    stayin_alive()
