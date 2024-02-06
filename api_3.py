from utils import geoobject, get_coords


def get_address_component(address, component_index):
    top = geoobject(address)
    components = top["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
    return components[component_index]["name"]


def main():
    for town in ["Барнаул", "Мелеуз", "Йошкар-Ола"]:
        province = get_address_component(town, 2)
        print(f"{town}: {province}")
    print("")


if __name__ == "__main__":
    main()
