import requests
from utils import get_coords

address = "Аптека"

lat, lon = get_coords(address=address)
ll = f"{lat},{lon}"
spn="0.005,0.005"

url = "https://search-maps.yandex.ru/v1/"
params = {
    "apikey": "",
    "text": address,
    "lang": "ru_RU",
    "ll": ll,
    "spn": spn,
    "type": "biz",
}

response = requests.get(url, params=params)

if response:
    json_r = response.json()
    organization = json_r["features"][0]

    point = organization["geometry"]["coordinates"]
    org_lat, org_lon = map(float, point)
    point_flag = f"pt={org_lat},{org_lon},pm2dgl"

    point_params = point_flag + f"~{ll}"
    


def find_organization(ll, spn, request, locale="ru_RU"):
    url = "https://search-maps.yandex.ru/v1/"
    api_key = ""
    params = {
        "apikey": api_key,
        "text": request,
        "lang": locale,
        "ll": ll,
        "spn": spn,
        "type": "biz"
    }

    response = requests.get(url, params=params)

    if response:
        return response.json()["features"][0]