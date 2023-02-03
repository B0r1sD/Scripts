#!/var/bin/python3

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

date_after = '2022-01-01'
#input('Enter date after (YYYY-MM-DD format): ')
date_before = '2023-01-01'
#input('Enter date before (YYYY-MM-DD format): ')
species_group = 3
#input('Species group: 1 birds 2 mammals 3 reptiles/amfi 4 butterflies\nGive Number: ')
province = 15
#input('Province: 14 Limburg 15 West-Vl 16 Oost-Vl 17 Anwterp\nGive number: ')
rarity = 3
#input('Rarities: 1 common 2 rel common 3 rare 4 very rare \nEnter number: ')

url = 'https://waarnemingen.be/photos/?'

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"


params = urllib.parse.urlencode({'date_after':date_after,'date_before':date_before,'species_group':species_group,'province':province,'rarity':rarity})
#params = params.encode('utf-8') 
print(url + params)

try:
    request = urllib.request.Request(url, headers=headers)
    respons = urllib.request.urlopen(request)
    data_content = respons.read().decode('utf-8')

    soup = BeautifulSoup(data_content,'html.parser')
    
    
    
    for fotos in soup.find_all("a",class_="lightbox-gallery-image"):
        htmlfoto = (fotos.img)
        strip1 = str(htmlfoto).split('"')
        strip2 = strip1[3]
        print(strip2)
    
    for title in soup.find_all("a",class_="mod-stealth"):
    
        print(title.text.strip())
    
    '''
    #save_file = open('Waarnemingen.txt','w')
    
    for foto in gallery.figure.a.img:
        #print(foto)
    
        save_file.write(str(foto))
    save_file.close()
    '''
except Exception as e:
    print(str(e))

#print(data_content)