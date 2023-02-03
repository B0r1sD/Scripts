#!/usr/bin/python3

import urllib.request
import urllib.parse

url = 'https://www.howest.be/en/brochure'

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"

params = {
    'voornaam': 'Boris',
    'naam': 'Python'
}

query = urllib.parse.urlencode(params)  #query = parse + encode params
data = query.encode("utf-8")            #encode utf-8 query  (what if you don't do this?)

try:
    response = urllib.request.urlopen(url,data)   
    response_data = response.read().decode('utf-8')
    print(response_data)
    save_file = open('BITsite.html','w')
    save_file.write(str(response_data))
    save_file.close()

except Exception as e:
    print(str(e))