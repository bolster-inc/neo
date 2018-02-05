#! /usr/bin/env python
import requests
import time
import pprint

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
        # avoid rate limit by the server
        r = requests.post(api_end_point, json=payload)

        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            pprint.pprint(r.json())

    def submit_url(self, url):
        end_point = '/neo/scan'
        api_end_point = self.api_host + end_point
        payload = {
            "apiKey": self.api_key,
            "urlInfo": {
                "url": url
            }
        }
        time.sleep(0.5)
        r = requests.post(api_end_point, json=payload)
        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            pprint.pprint(r.json())
