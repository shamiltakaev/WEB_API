from utils import geoobject, get_coords


def get_address_component(address):
    top = geoobject(address)
    postal_code = top["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
    return postal_code


def main():
    address = "Московского Уголовного Розыска (МУРа) «Петровки, 38»"
    postal_code = get_address_component(address)
    print(f"{address} имеет почтовый индекс: {postal_code}")


if __name__ == "__main__":
    main()
