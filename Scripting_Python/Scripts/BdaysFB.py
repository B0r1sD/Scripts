#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# path to the geckodriver
webdriver_path = 'geckodriver_v0.18.exe'

# define xpaths
xpaths = {'friends': "//li[@class='_43q7']",
         'hoverovertext': 'data-tooltip-content'}

driver = webdriver.Firefox(executable_path = webdriver_path)
driver.get('https://www.facebook.com/events/birthdays/')
print(driver)

time.sleep(60)

# scroll all the way down
for scroll in range(20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# define lists
names = []
bds =[]

# loop through friends
for person in driver.find_elements(By.XPATH, xpaths['friends']):
    
    print(person)
    
    # get hoverover text
    person_text = person.find_element_by_class_name('link').get_attribute(xpaths['hoverovertext'])
    
    # retrieve name
    name = person_text.split('(')[0]
    
    # retrieve date of birth
    bd = person_text.split('(')[1].replace(')','')
    
    # append to lists
    names.append(name)
    bds.append(bd)
    
print('Got %d friends' % len(names))

# save to csv
bd_db = pd.DataFrame({'Name': names, 'BD': bds})
bd_db['Name'] = bd_db['Name'].str.encode("ascii","ignore")
bd_db.to_csv('%s FB Birthdays.csv' % str(time.strftime('%Y%m%d')))