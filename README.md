## RedMarlin Neo API -Artificial Intellgience Based RealTime Phishing Detection.

### Live Demo
##### For live demo you can checkout https://checkphish.ai

### Current Clients
Client in this repository is python client. Client in other languages are coming soon.

### Setup
###### First clone the repository
     git clone git@github.com:redmarlinai/neo.git

###### Make sure you have python requests installed
     sudo pip install requests

### API KEY & URLS
###### Request api key from https://redmarlin.ai/#!/contact-us and specify in the src/client.py file
      RM_API_KEY = '<YOUR-API-KEY>'
        
###### Now specifiy list of urls
    # add urls here
    urls_list = [
        'https://example.com'
    ]

###  Run client
Sample client is client.py. At first client will submit all urls and then the apis will return the job_ids. Job_ids need to be store so they can be queried at a later time.
    
###
 
