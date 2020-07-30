import requests

URL = 'http://api.cpanomer1.affise.com/3.0/'
HEADER = {
    "API-Key": 'e60a98867d363b0d43b9e7c58ec498ed'
}


def get_offer():
    response = requests.get(f'{URL}partner/offers', headers=HEADER)
    offer = response.json()['offers'][0]
    print("Information about offer: ", offer)
    print("Available countries: ", offer['countries'])
    return offer['id']


def get_conversion(off_id):
    response = requests.get(f"{URL}stats/conversions?date_from=", headers=HEADER)
    conversion = response.json()['conversions'][0]
    print("Information about conversion: ", conversion)
    if off_id == conversion['offer_id']:
        print("Conversion click id: ", conversion['action_id'])
        print("Conversion from: ", conversion['country_name'], conversion['city'])


if __name__ == '__main__':
    offer_id = get_offer()
    get_conversion(offer_id)

