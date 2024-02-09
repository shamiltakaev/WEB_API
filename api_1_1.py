import requests

url = "https://geocode-maps.yandex.ru/1.x/?"
api_key = "a51286fd-602b-4dc7-a21a-7594bf3786d6"
address = "Москва, Красная площадь, 1"

params = {
    "apikey": api_key,
    "lang": "ru_RU",
    "format": "json",
    "geocode": address,
}

response = requests.get(url, params=params)

if response:
    json_res = response.json()

    geo_ojbect = json_res["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

    coords = " ".join(geo_ojbect["Point"]["pos"].split()[::-1]) 
    # Меняем местами долготу и широту из ответа. 
    # API возвращает немного не так, как работают наши карты
    print(f"{address} находится на координатах {coords}")
