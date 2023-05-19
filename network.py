import requests
from apiconfig import *
from requests.auth import HTTPDigestAuth
import json
import urllib3
from datetime import *
import time
import unittest
import logging

from http.client import HTTPConnection  # py3
urllib3.disable_warnings()
logging.captureWarnings(True)


class network (unittest.TestCase):
    def setup(self):
        self.url = url
        self.cert = cert
        self.key = key
        urllib3.disable_warnings()

    
    def test_get(self):
        print("Starting get test:")
        rGet = requests.get(url=url, cert=(cert, key), verify=False)
        print(rGet.text)
        if rGet.status_code == 200:
            print("Test passed. The current status:", rGet)
        else:
            print("Test failed. The current status is not 200 (OK) and it is ",  rGet)

    def test_post(self):
        print("Starting post test:")
        rPost = requests.post(url=url, json=json.dumps(json_data), cert=(cert, key), verify=False)
        print(rPost.text)
        if rPost.status_code == 200:
            print("Test post passed. The current status:", rPost)
        else:
            print("Test post failed. The current status is not 200 (OK) and it is ",  rPost)

    def tearDown(self):
        
        time.sleep(5)
        log = logging.getLogger('urllib3')
        log.setLevel(logging.DEBUG)

        # logging from urllib3 to console
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        log.addHandler(ch)

        # print statements from `http.client.HTTPConnection` to console/stdout
        HTTPConnection.debuglevel = 1
        today = date.today()
        logs = print(log.debug)
        
        print("Test ended.")
    



if __name__ == "__main__":
    unittest.main()
