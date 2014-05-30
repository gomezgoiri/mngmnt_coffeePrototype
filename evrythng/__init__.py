
'''
Created on 18/05/2014

@author: tulvur
'''
import json
import requests
import ConfigParser
from requests.auth import HTTPBasicAuth


config = ConfigParser.RawConfigParser()
config.read("config.ini")
API_KEY = config.get('EvryThng', 'apikey')

API_URL = "https://api.evrythng.com/"
SEARCH_URL = API_URL + "search"
THNGS_URL = API_URL + "thngs/"
PROPERTIES_URL = THNGS_URL + "%s/properties"
COLLECTIONS_URL = API_URL + "collections/"


def get_headers():
    return {'content-type': 'application/json', 'Authorization': API_KEY}

def get_all_thngs():
    r = requests.get(THNGS_URL, headers=get_headers())
    return r # text, status_code

def get_thng(thng_id):
    r = requests.get(THNGS_URL + thng_id, headers=get_headers())
    return r

def create_user():
    payload = {'name': 'tulvur', 'description': 'Me.', 'properties': {'favorite_machines': '0'}}
    r = requests.post(THNGS_URL, data=json.dumps(payload), headers=get_headers())
    return r

def modify_user(user_id, favorite_id):
    payload = [{'key': 'favorite_machines', 'value': favorite_id}]
    r = requests.put(PROPERTIES_URL % user_id, data=json.dumps(payload), headers=get_headers())
    return r

def create_favorite_machines(user_id):
    payload = {'name': 'tulvur_favorite_machines', 'properties': {'who': user_id}}
    r = requests.post(COLLECTIONS_URL, data=json.dumps(payload), headers=get_headers())
    return r

def get_users():
    r = requests.get(SEARCH_URL + "?q=user", headers=get_headers())
    return json.loads(r.text)['thngs']

if __name__ == "__main__":
    #print get_all_thngs().text
    #print get_thng("UAh2m7n2PBKw6Xs6wEF5es8s").text
    #print create_user().text

    #print get_thng("UUhmyxw5sVKwqXPMwYFKnMqe").text
    #print create_favorite_machines("UUhmyxw5sVKwqXPMwYFKnMqe").text
    #print modify_user("UUhmyxw5sVKwqXPMwYFKnMqe", "UAYGTnxCsB5aEHEVQHmMDard").text
    print get_users()
