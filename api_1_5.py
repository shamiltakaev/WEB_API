import requests
import pygame
import sys
import os


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
    import json
    with open("1.json", "w", encoding="utf8") as file:
        json.dump(json_response, file, ensure_ascii=False, indent=4)
    features = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return features[0]["GeoObject"] if features else None


def get_coords(address):
    top = geoobject(address)
    if not top:
        return 43.325803, 45.711564

    coords = top["Point"]["pos"]
    longtitude, lattitude = map(float, coords.split())
    return ",".join(map(str, [longtitude, lattitude]))


def show_map(ll="43.325803,45.711564", spn="0.002,0.002", map_type="map", add_params=None):
    api_key = "dbcb1a72-711c-454c-8aad-1732cd8bda67"
    url = "https://static-maps.yandex.ru/v1"
    params = {
        "apikey": api_key,
        "ll": ll,
        "spn": spn,
        "l": map_type
    }

    if add_params:
        params.update(add_params)
    print(params)
    response = requests.get(url, params=params)
    print(response.url)
    if not response:
        print("Error run")
        sys.exit(1)

    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Error", ex)
        sys.exit(2)

    pygame.init()
    screen = pygame.display.set_mode((600, 450))

    screen.blit(pygame.image.load(map_file), (0, 0))

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()

    os.remove(map_file)


# from utils import geoobject, get_coords, show_map


def main():
    coords = get_coords("Австралия")
    show_map(ll=coords, spn="20,20")


if __name__ == "__main__":
    main()
    

