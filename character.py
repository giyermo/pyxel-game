import pyxel


class Character:
    def __init__(self, x, y, w, h, sprite):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.sprite = sprite

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def sprite(self):
        return self.__sprite

    @w.setter
    def w(self, w):
        if type(w) is not int:
            raise TypeError("w must be an integer")
        elif w > pyxel.width:
            self.__w = pyxel.width
        elif w < 0:
            self.__w = 0
        else:
            self.__w = w

    @h.setter
    def h(self, h):
        if type(h) is not int:
            raise TypeError("h must be an integer")
        elif h > pyxel.height:
            self.__h = pyxel.height
        elif h < 0:
            self.__h = 0
        else:
            self.__h = h

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x + self.w > pyxel.width:
            self.__x = pyxel.width - self.w
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y + self.h > pyxel.height:
            self.__y = pyxel.height - self.h
        elif y < 0:
            self.__y = 0
        else:
            self.__y = y

    @sprite.setter
    def sprite(self, sprite):
        if type(sprite) is not int:
            raise TypeError("sprite must be an integer")
        elif sprite > pyxel.num_tiles:
            self.__sprite = pyxel.num_tiles - 1
        elif sprite < 0:
            self.__sprite = 0
        else:
            self.__sprite = sprite

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, self.sprite, 0, 0, self.w, self.h, 0)
