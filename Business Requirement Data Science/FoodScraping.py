import requests

response = requests.get('https://gateflipp.flippback.com/bf/flipp/items/search?locale=en-ca&postal_code=N2L6P2&sid=&q=onion')


if response.status_code == 200 :
    items = response.json()["items"]
    mainList = []
    mainDictonary = {}
    minPrice = 0

    for eachItem in items:
        name = eachItem.get('name')
        currentPrice = eachItem.get('current_price')
        merchantName = eachItem.get('merchant_name')
        valid_to = eachItem.get('valid_to')
        valid_from = eachItem.get('valid_from')
        clipping_image_url = eachItem.get('clipping_image_url')
        dictonary = {}
        
        if  isinstance(currentPrice,float) or isinstance(currentPrice,int):
            dictonary = {'name' : name, 'currentPrice' : currentPrice, 'merchantName' : merchantName, 'valid_to' : valid_to, 
            'valid_from' : valid_from,'clipping_image_url' : clipping_image_url }
            mainList.append(dictonary)

    price_list = []
    for items in mainList:
        itemsInList = items.get('currentPrice')
        price_list.append(itemsInList)
    
    price_list.sort()
    cheapestList = []
    for price in price_list:
        for items in mainList:
            if(items.get('currentPrice')==price):
                cheapestList.append(items)
        if(len(cheapestList) >= 5 ):
            break
    print(cheapestList)
else:
    print('There is a problem with the Url or with the website.' + response.status_code)