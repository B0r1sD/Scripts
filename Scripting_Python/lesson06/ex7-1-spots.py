#!/usr/bin/python3

import urllib.request
import urllib.parse
import time
from bs4 import BeautifulSoup

#url = "https://github.com/B0r1sD"
url = 'https://www.ncbi.nlm.nih.gov/sra/SRX4179991%5baccn%5d'


#modify user-agent
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"

try:
    request = urllib.request.Request(url)
    
    response = urllib.request.urlopen(request)
    
    response_data = response.read()
    
    soup = BeautifulSoup(response_data,'html.parser')
    spots = soup.find_all('table')
    for child in spots[0].descendants:

        child = soup.find_all('td')
        print(child[1].text)
        break

    #print(response_data)
    #print(soup.prettify())

    #print(spots)
    #print(spots2)

    save_file = open('spots.txt','w')
    save_file.write(str(spots))
    save_file.close()
except Exception as e:
    print(str(e))

#print(headers)



