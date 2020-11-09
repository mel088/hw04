import requests
from bs4 import BeautifulSoup

keyword='painting'
#can change keyword to whatever you want to search for
page_number = '1'
# part 1) test:
# page_number = '5'
results = []

headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15'
}

#for downloading the first 10 webpages 1):
for i in range(10):
#for i in range(1,11):
#indent the all lines below to be containned in the for loop except for the import json portion
    ###r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword, headers=headers)
#when testing for part 1):
    r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn'+page_number, headers=headers)
    print('r.status_code=',r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')

#print('r.text=',r.text)
######comment these out eventually below
    ###items = soup.select('a')
    items = soup.select('li.s-item--watch-at-corner.s-item > .clearfix.s-item__wrapper')
#items = soup.select('li.s-item--wat..etc.) use ublock origin
#items = soup.select('.a-text-normal.a-color-base.a-size-base-plus)

    ###for item in items:
        ###print('item=',item)
    #use ublock origin, click shield, dropper, item name, css selector

    ###prices = soup.select('.s-item__price')
    ###for price in prices:
        ###print('price=',price.text)

    ###statuses = soup.select('.SECONDARY_INFO')
    ###for status in statuses:
       ###print('status=', status.text)
####comment out above portion 

#extract the "item boxes" rather than just the names/prices
    boxes = soup.select('li.s-item--watch-at-corner.s-item')
    for box in boxes:
        print('---')
        result = {}
        names = box.select('li.s-item--watch-at-corner.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__link > .s-item__title')
        for name in names:
            print('name=',name.text)
            result['name'] = name.text
        prices = box.select('.s-item__price')
        for price in prices:
            print('price=',price.text)
            result['price'] = price.text
        statuses = soup.select('.SECONDARY_INFO')
        for status in statuses:
            print('status=', status.text)
            result['status'] = status.text
        print('result=',result)
        results.append(result)

    print('len(results)=', len(results))


   
#Mike got 62, want to check how many results per page, should be close, ads don't count
#3 last steps:
# 1) works on not just 1 webpage, but the top 10 results pages. Works.
# 2) not just the item name and price, but also it's "status" (new, used, etc.). Works.
# 3) output to a json file. Works.


# 3)

import json
j = json.dumps(results)
with open('items.json','w') as f:
    f.write(j)
#print('j=', j)
