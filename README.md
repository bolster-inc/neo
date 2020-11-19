## CheckPhish Neo API -Artificial Intellgience Based RealTime Phishing Detection

### Live Demo

##### For live demo you can checkout https://checkphish.ai

### API KEY

###### Request api key from https://bolster.ai/contact-us

### Setup

###### Make sure you have python requests installed

     sudo pip install requests

###### Now clone or download the respository

     git clone https://github.com/bolster-inc/neo.git

###### if downloading then do

    wget https://github.com/bolster-inc/neo/archive/master.zip
    unzip master.zip

### Usage

     python src/client.py -h
          usage: client.py [-h] -f FILE

     usage: client.py [-h] -k KEY -f FILE

     required arguments:
          -k KEY, --key KEY     provide your api key
          -f FILE, --file FILE  file containing urls

     optional arguments:
          -h, --help            show this help message and exit

### Run client

###### now provide your API KEY and file with urls to scan to the client. Each url needs to be in a new line.

      cd neo/src/
      python client.py  -k <YOUR_API_KEY>  -f "urls_to_scan.txt"

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

### Support

For any issues please follow instructions on this link

###### https://bolster.ai/contact-us
