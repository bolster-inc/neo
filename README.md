## RedMarlin Neo API -Artificial Intellgience Based RealTime Phishing Detection.

### Live Demo
##### For live demo you can checkout https://checkphish.ai

### Setup
###### First clone the repository
     git clone git@github.com:redmarlinai/neo.git

###### Make sure you have python requests installed
     sudo pip install requests

### API KEY
###### Request api key from https://redmarlin.ai/#!/contact-us and specify in the src/client.py file
      
        
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
      cd src/
      python client.py  -k <YOUR_API_KEY>  -f "urls.txt"
      
