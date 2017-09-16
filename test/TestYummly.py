import yummly
import requests
import ujson as uj


# default option values
TIMEOUT = 15.0
RETRIES = 2

# Yummly mjboothaus Account: Hackathon Plan - Access granted 24 July 2017

API_ID = 'b4f167ed'
API_KEY = 'f69184af19beb4b76e7b7b1984046581'

"""
YURL = 'https://api.yummly.com/v1/api/'

YMETA = 'metadata/ingredient?_app_id=' + API_ID + '&_app_key=' + API_KEY

my_request = YURL + YMETA

print my_request

ingredients = requests.get(my_request)

ingredients_json = ingredients.content
ingredients_json = ingredients_json[27:-2]

tmp = uj.decode(ingredients_json)

"""

client = yummly.Client(api_id=API_ID, api_key=API_KEY, timeout=TIMEOUT, retries=RETRIES)

ingredients = client.metadata('ingredient')
diets = client.metadata('diet')
sources = client.metadata('source')

#search = client.search('green eggs and ham')
#match = search.matches[0]
#match.id

#recipe = client.recipe(match.id)

#print recipe
