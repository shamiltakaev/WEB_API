import requests
from io import BytesIO
import requests
from PIL import Image
from utils import geoobject


def geoobject(address):
    search_api_server = "http://geocode-maps.yandex.ru/1.x/?"
    api_key = "a51286fd-602b-4dc7-a21a-7594bf3786d6"
    search_params = {
        "apikey": api_key,
        "lang": "ru_RU",
        "format": "json",
        "geocode": address
    }

    response = requests.get(search_api_server, params=search_params)
    if response:
        json_response = response.json()
    
    features = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return features[0]["GeoObject"] if features else None


def get_coords(address):
    top = geoobject(address)
    if not top:
        return 43.325803, 45.711564

    coords = top["Point"]["pos"]
    longtitude, lattitude = map(float, coords.split())
    return longtitude, lattitude


def show_map(ll, spn, map_type="map"):
    """Показываем карту с меткой с помощью аргумента pt, который получает координаты где эта метка должна быть
    """
    ll, spn = ll, spn
    params = {
        "ll": ll,
        "spn": spn,
        "l": map_type,
        "pt": ll
    }
    api_server = "http://static-maps.yandex.ru/1.x/"

    response = requests.get(api_server, params=params)
    Image.open(BytesIO(response.content)).show()


