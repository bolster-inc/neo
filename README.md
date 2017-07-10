## RedMarlin Neo API -Artificial Intellgience Based RealTime Phishing Detection.

### Live Demo
##### For live demo you can checkout https://checkphish.ai

### API KEY
###### Request api key from https://redmarlin.ai/#!/contact-us

###### Make sure you have python requests installed
     sudo pip install requests

### Setup
###### Now clone the repository
     git clone git@github.com:redmarlinai/neo.git
      
        
### Usage
     python src/client.py -h
          usage: client.py [-h] -f FILE

     usage: client.py [-h] -k KEY -f FILE
     
     required arguments:
          -k KEY, --key KEY     provide your api key
          -f FILE, --file FILE  file containing urls
          
     optional arguments:
          -h, --help            show this help message and exit
  


###  Run client     
###### now provide your API KEY and  file with urls to the client
      cd neo/src/
      python client.py  -k <YOUR_API_KEY>  -f "urls.txt"


### Results
#### results will be saved in 4 different files in the same directory
     phish.txt - all the urls that have been identified as phish
     clean.txt - all the urls that have been identified as clean
     suspicious.txt - all the urls that have been identify as suspicious
     pending.txt - all the urls that still being processed. Please query these urls again.
     
#### A results summary will also be printed. Sample summary would look something like

	================ SAVING RESULTS ===========================

	phish urls saved to file:       /home/john/projects/neo_client/pending.txt
	phish urls saved to file:       /home/john/projects/neo_client/phish.txt
	clean urls saved to file:       /home/john/projects/neo_client/clean.txt
	suspicious urls saved to file:  /home/john/projects/neo_client/suspicious.txt

	================ SCAN SUMMARY ===========================

	Total Urls submitted:     175
	Processing completed:     175
	Processing pending:       0
	Total phishing urls:      132
	Total suspicious urls:    9
	Total clean urls:         34
	
###  Support
For any issues please follow instructions on this link
###### https://redmarlin.ai/#!/support
