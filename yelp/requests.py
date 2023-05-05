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
            temp['resturant_id'] = rest['id']
            temp['resturant_name'] = rest['name']
            temp['resturant_image'] = rest['image_url']
            temp['resturant_url'] = rest['url']
            temp['resturant_categories'] = [i['title'] for i in rest['categories']]
            temp['resturant_rating'] = rest['rating']
            temp['resturant_address'] = rest['location']['display_address']
            temp['resturant_phone_number'] = rest['display_phone']
            temp['resturant_distance'] = rest['distance']
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
        temp['resturant_id'] = rest['id']
        temp['resturant_name'] = rest['name']
        temp['resturant_image'] = rest['image_url']
        temp['resturant_categories'] = [i['title'] for i in rest['categories']]
        temp['resturant_rating'] = rest['rating']
        temp['resturant_url'] = rest['url']
        temp['resturant_address'] = rest['location']['display_address']
        temp['resturant_phone_number'] = rest['display_phone']
        temp['resturant_distance'] = rest['distance']
        resturants.append(temp)
    
    return resturants
        



    params = {"location":"tysons", "attributes":"resturants","sort_by":"best_match","limit":20}