import requests

url = "https://geocode-maps.yandex.ru/1.x/?"
api_key = "a51286fd-602b-4dc7-a21a-7594bf3786d6"

params = {
    "apikey": api_key,
    "lang": "ru_RU",
    "format": "json",
}

for town in ["Хабаровск", "Уфа", "Нижний Новгород", "Калининград"]:
    params["geocode"] = town

    response = requests.get(url, params=params)
    if response:
        json_res = response.json()

        geo_object = json_res["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        district = geo_object["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"]
        print(f"{town}: {district}")

