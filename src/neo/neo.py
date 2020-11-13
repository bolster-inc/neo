#! /usr/bin/env python
import requests
import time
import pprint
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class Neo:
    def __init__(self, api_key, api_host):
        self.api_key = api_key
        self.api_host = api_host

    def get_job_status(self, job_id):
        end_point = '/neo/scan/status'

        api_end_point = self.api_host + end_point
        payload = {
            'apiKey': self.api_key,
            'jobID': job_id
        }
        print("getting job status:", job_id)
        try:
            r = self.requests_retry_session().post(api_end_point, json=payload)
            json = r.json()
            print(json)
            if r.status_code == requests.codes.ok:
                return json
            else:
                pprint.pprint(json)
        except Exception as e:
            print("Error getting result for jobID:", job_id, format(e))

    def requests_retry_session(self, retries=10, backoff_factor=0.3, status_forcelist=(413, 429, 500, 502, 503, 504), session=None):
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
            method_whitelist=["HEAD", "GET", "POST"]
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def submit_url(self, url):
        end_point = '/neo/scan'
        api_end_point = self.api_host + end_point
        payload = {
            "apiKey": self.api_key,
            "urlInfo": {
                "url": url
            },
            "scanType": "full"
        }
        # avoid rate limiting by the server, do not change this.
        time.sleep(0.5)
        try:
            r = self.requests_retry_session().post(api_end_point, json=payload)
            if r.status_code == requests.codes.ok:
                return r.json()
            else:
                pprint.pprint(r.json())
        except Exception as e:
            print('Error sending request:', format(e))
