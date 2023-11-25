#case1 : we have url of jason data and we have to extract particular data.

import json
import requests
# if response is slow , timeout will show.
from socket import timeout
import logging

# we are defining a method and passing url as a variable.
def hit_endpoint(url):
    list=[]
    if(url!="null"):
        data = requests.get(url)
        #print(data.json())
        dump = data.json()
        print(dump["count"])
        for link in dump["entries"]:
            print(link['Link'])
            try:
                data2 = requests.get(link['Link'],timeout=10)  # If website is not opening in 10sec,
                if (data2.status_code==200):
                    list.append(link['Link'])
                    print(list)
                else:
                    print("Status Code is not 200")
            except requests.exceptions.Timeout:
                logging.error("timeout")

    else:
        print("Error loading the url")

hit_endpoint("https://api.publicapis.org/entries")
