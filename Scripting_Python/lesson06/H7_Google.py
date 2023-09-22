#!/usr/bin/python3

import urllib.request
import urllib.parse
import time

#url = "https://github.com/B0r1sD"
url = 'https://google.com/search?q=bachelor+BIT'

values = {'q':'bachelor bioinformatics'}
params = urllib.parse.urlencode(values)
params = params.encode('utf-8')              #data should be bytes

#modify user-agent
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"

try:
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    print(response_data)
    save_file = open('google-headers.txt','w')
    save_file.write(str(response_data))
    save_file.close()
except Exception as e:
    print(str(e))

#print(headers)
