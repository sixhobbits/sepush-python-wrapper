import requests
from urllib.parse import urljoin
import os

ESP_TOKEN = os.environ.get("ESP_TOKEN")

if not ESP_TOKEN:
    print("Token not found. Please set the ESP_TOKEN environment variable")

BASE_URL = "https://developer.sepush.co.za/business/2.0/"

STATUS = "status"
AREA = "area"
AREAS_NEARBY = "areas_nearby"
AREAS_SEARCH = "areas_search"
TOPICS_NEARBY = "topics_nearby"
API_ALLOWANCE = "api_allowance"

def get(endpoint, params=None):
    url = urljoin(BASE_URL, endpoint)
    headers = {"Token": ESP_TOKEN}
    response = requests.get(url, headers=headers, params=params)
    return response

def get_status():
    r = get(STATUS)
    return r.json()

def get_area(area_id, test=None):
    params = {"id": area_id}
    if test:
        params['test'] = test
    r = get(AREA, params)
    return r.json()

def get_areas_nearby(lat, lon):
    params = {"lat": lat, "lon": lon}
    r = get(AREAS_NEARBY, params)
    return r.json()

def get_areas_search(text):
    params = {"text": text}
    r = get(AREAS_SEARCH, params)
    return r.json()

def get_topics_nearby(lat, lon):
    params = {"lat": lat, "lon": lon}
    r = get(TOPICS_NEARBY, params)
    return r.json()

def get_api_allowance():
    r = get(API_ALLOWANCE)
    return r.json()

