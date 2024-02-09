from utils import show_map, geoobject

  

def get_ll_span(address):
    toponym = geoobject(address=address)
    if toponym:
        coords = toponym["Point"]["pos"]
        ll = ",".join(coords.split())

        # Если просмотреть файл 1.json, то мы увидим поле ключ Envelope, который и указывает 
        # нам координаты левой верхней точки и правой нижней точки. 
        # Берем эти координаты и с помощью математики вычисляем масштаб карты, необходимый для вывода этого объекта на экран
        rect = toponym["boundedBy"]["Envelope"]
        left, bot = map(float, rect["lowerCorner"].split())
        right, top = map(float, rect["upperCorner"].split())

        dx = abs(left - right) / 2.5
        dy = abs(top - bot) / 2.5
        span = f"{dx},{dy}"
        return ll, span   



show_map(*get_ll_span("Грозный"), "map")