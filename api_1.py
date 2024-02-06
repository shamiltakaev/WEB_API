from utils import geoobject, get_coords


def get_address_coords(address):
    long, lat = get_coords(address)
    return " ".join(map(str, [lat, long]))


def main():
    for address in ["Москва, Красная площадь, 1"]:
        coords = get_address_coords(address)
        print(f"{address} имеет координаты: {coords}")
    print("")


if __name__ == "__main__":
    main()
