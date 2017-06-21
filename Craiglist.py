from selenium import webdriver
import time
from text_unidecode import unidecode

YOUR_ZIPCODE = 85281  # enter your zipcode here
RADIUS = 25  # enter the radius within which you can go to collect the item
MAX_PRICE = 250  # enter the max price you want to pay
WAIT = 1 # time in minutes the code should wait before checking for updates
ITEMS_TO_LOOK =  ['chair','mobile']# list of items to look. This should be a list such as ['chair', 'desk']

## generate the url for the above parameters for your area.
## here its generated for hartford area but you might want to change based on
## your location. Open craiglist and it will direct you the relevant subdomain﻿﻿

url = 'https://hartford.craigslist.org/search/zip?search_distance=' + str(RADIUS) + '&postal=' + str(
    YOUR_ZIPCODE) + '&max_price=' + str(MAX_PRICE)

## intantiate a firefox browser instance
driver = webdriver.Firefox()
## load the url
driver.get(url)

## declare and empty list to keep the items. This will also come in handy to check items
## that are newly added﻿
items = []

## get all the items on the first page. Not concerned about the other pages
results = driver.find_elements_by_css_selector('.result-row')

## iterate through the results to find the text
for result in results:
    a = results[0].find_element_by_css_selector('.result-info')
    items.append(unidecode(a.find_element_by_tag_name('a').text))

## in a while loop. This makes it an infinite loop
## LOGIC - keep checking every WAIT minutes and find new items that are added
## if any new item found, email it to the user
## else sleep. ﻿﻿﻿
while True:
    driver.get(url)
    time.sleep(5)
    results = driver.find_elements_by_css_selector('.result-row')
    for result in results:
        a = results[0].find_element_by_css_selector('.result-info')
        text = unidecode(a.find_element_by_tag_name('a').text)
        if (text not in items) and (any(ext.lower().strip() in text.lower().strip() for ext in ITEMS_TO_LOOK)):
            items.append(text)

    time.sleep(WAIT * 60)  ## sleep