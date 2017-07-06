#! /usr/bin/env python
#
# see documentation here
# ##
import time
import pprint
from neo import neo

# specify your api key
# get your API Key by contacting redmarlin at support.redmarlin.ai
RM_API_KEY = '<YOUR-API-KEY>'
API_HOST = 'https://developers.redmarlin.ai/api'


def main():
    neo_client = neo.Neo(RM_API_KEY, API_HOST)

    # add urls here
    urls_list = [
        'https://redmarlin.ai'
    ]
    jobs = []
    # submit all the urls for processing
    for url in urls_list:
        print("> submitting url: ", url)
        result = neo_client.submit_url(url)
        if result:
            jobs.append(result['job_id'])

    print("> urls submitted waiting for results...")
    # lets wait for 7 seconds so results are ready
    time.sleep(7)

    # now we have all the job ids lets query the results
    for job in jobs:
        result = neo_client.get_job_status(job)
        pprint.pprint(result)


if __name__ == '__main__':
    main()
