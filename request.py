import requests

def get_price_bitcoin():
    '''return bitcoin price'''
    page=requests.get("https://api.coinstats.app/public/v1/coins/bitcoin?currency=USD")
    json_object_string=page.json()
    #print(json_object_string)
    price=str(json_object_string['coin']['price'])
    #print(price)
    return price

print(get_price_bitcoin())

API_KEY="676C4932524F4959477076626C6A58502F7859424B3676694F706E47687676315247524C6A7758574A74383D"
url=f'https://api.kavenegar.com/v1/{API_KEY}/sms/send.json'

data={
    'receptor':"#########", #your phone number
    'message':get_price_bitcoin(), # return bitcoin price
}
page=requests.post(url=url,data=data)
print(page.ok)
print(page)
