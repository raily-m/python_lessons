class Color:
    def __init__(self, r, g, b):
    if 0 <=r <= 255 and 0 <=b <= 255:
        self._r = r
        self._g = g
        self.b = b
    else:
        self._r = 0
        self._g = 0
        self.b = 0

@property

def r(self):
    return self.__r


@property
def g(self):
    return self.__g

@property
def b(self):
    return self.__b

@property
def hex_color(self):
    r = hex(self.__r)[2:]
    g = hex(self.__g) [2:]
    b = hex(self.__b) [2:]
    return f"#{r}{g}{b}".upper()


header = Color(200, 215, 0)
header.hex_color #F0080808
print(header.hex_color)



