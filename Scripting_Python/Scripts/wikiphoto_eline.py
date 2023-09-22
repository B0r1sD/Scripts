#!/usr/bin/python3


import urllib
import urllib.request
from bs4 import BeautifulSoup
import wget
import requests

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename


headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"

url = "https://nl.wikipedia.org/wiki/Kunstformen_der_Natur"

request = urllib.request.Request(url, headers = headers)
response = urllib.request.urlopen(request)
response_data = response.read().decode('utf-8')
soup = BeautifulSoup(response_data, 'html.parser')

figures_list = soup.find_all("a", {"class":"image"})

for figure in figures_list:
    image = figure.find("img")
    image_url = image["src"]
    image_url = image_url.replace("//", "https://")
    print("\nDownloading image ..." + image_url)
    wget.download(image_url)
    download_file(image_url)


    