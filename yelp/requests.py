import requests
import os
import environ
from dotenv import load_dotenv

load_dotenv()
url= os.environ['YELP_URL']
api_key = os.environ['YELP_API_KEY']
headers = {
    "accept": "application/json",
    "Authorization": api_key
}

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
    )

def getResturants(params):
    call_url = url + "businesses/search"
    response = requests.get(call_url, headers=headers, params=params)
    if response.status_code == 200:
        jsonResponse = response.json()
        resturants = []
        for rest in jsonResponse['businesses']:
            temp = {}
            temp['id'] = rest['id']
            temp['name'] = rest['name']
            temp['image'] = rest['image_url']
            temp['categories'] = [i['title'] for i in rest['categories']]
            temp['rating'] = rest['rating']
            temp['address'] = rest['location']['display_address']
            temp['phone_number'] = rest['display_phone']
            temp['distance'] = rest['distance']
            resturants.append(temp)
        return resturants
    else:
        return response.text

    

def getResturantsbyId(ResturantId):
    resturants = []
    for id in ResturantId:
        call_url = url + "businesses/" + id
        response = requests.get(call_url, headers=headers)
        rest = response.json()
        temp = {}
        temp['id'] = rest['id']
        temp['name'] = rest['name']
        temp['image'] = rest['image_url']
        temp['categories'] = [i['title'] for i in rest['categories']]
        temp['rating'] = rest['rating']
        temp['address'] = rest['location']['display_address']
        temp['phone_number'] = rest['display_phone']
        temp['distance'] = rest['distance']
        resturants.append(temp)
    
    return resturants
        



    params = {"location":"tysons", "attributes":"resturants","sort_by":"best_match","limit":20}