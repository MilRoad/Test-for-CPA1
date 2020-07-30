import requests


def affise_api():
    key = 'e60a98867d363b0d43b9e7c58ec498ed'
    url = 'http://api.cpanomer1.affise.com/3.0/'

    responce = requests.get(f'{url}partner/offers?api-key={key}')

    offer = responce.json()['offers'][0]
    print("Information about offer: ", offer)
    print("Available countries: ", offer['countries'])

    id = offer['id']

    responce = requests.get(f"{url}stats/conversions?api-key={key}&status=")
    conversion = responce.json()['conversions'][0]
    print("Information about conversion: ", conversion)
    if id == conversion['offer_id']:
        print("Conversion click id: ", conversion['action_id'])
        print("Conversion from: ", conversion['country_name'], conversion['city'])


affise_api()

