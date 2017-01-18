import time
import random
import requests

from bs4 import BeautifulSoup

URL = "https://www.cs.utexas.edu/~dana/MLClass/"
DEST_DIR = "pdfs/"


def get_page(url=URL):
    req = requests.get(url)
    return req.content


def get_hrefs(soup, head_url=URL, last_latency=0):
    """
    TODO: adjust reqs/sec
        > The MercatorWeb crawler follows an adaptive politeness policy: if it took
        > t seconds to download a document from a given server, the crawler waits
        > for 10t seconds before downloading the next page.
    """
    for link in soup.find_all('a'):
        url = link.get('href')
        if not url.startswith("http"):
            # means its a relative path
            url = ''.join((head_url, url))
        tail_fn = url.split('/')[-1] if url.split('/')[-1] != '' else url.split('/')[-2]
        if tail_fn[-4::] == '.pdf':
            # only download pdfs
            with open('/'.join((DEST_DIR, tail_fn)), 'wb') as f:
                # generate random number of seconds to sleep for
                print "Downloading {}.".format(tail_fn)
                sleeptime = random.randrange(5, 10)
                print "Sleeping for {}.s".format(sleeptime)
                time.sleep(sleeptime)
                fresponse = requests.get(url)
                f.write(fresponse.content)
                print "Response code was {}.".format(fresponse.status_code)


if __name__ == "__main__":
    soup = BeautifulSoup(get_page(), 'html.parser')
    get_hrefs(soup)
