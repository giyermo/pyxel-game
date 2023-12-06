import pyxel


class Character:
    def __init__(self, x, y, u, v, w, h, sprite=0):
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.sprite = sprite

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def u(self):
        return self.__u

    @property
    def v(self):
        return self.__v

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    @property
    def sprite(self):
        return self.__sprite

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        # elif x + self.w > pyxel.width:
        #     self.__x = pyxel.width - self.w
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        # elif y + self.h > pyxel.height:
        #     self.__y = pyxel.height - self.h
        elif y < 0:
            self.__y = 0
        else:
            self.__y = y

    @u.setter
    def u(self, u):
        if type(u) is not int:
            raise TypeError("u must be an integer")
        elif u > pyxel.width:
            self.__u = pyxel.width
        elif u < 0:
            self.__u = 0
        else:
            self.__u = u

    @v.setter
    def v(self, v):
        if type(v) is not int:
            raise TypeError("v must be an integer")
        elif v > pyxel.height:
            self.__v = pyxel.height
        elif v < 0:
            self.__v = 0
        else:
            self.__v = v

    @w.setter
    def w(self, w):
        if type(w) is not int:
            raise TypeError("w must be an integer")
        elif w > pyxel.width:
            self.__w = pyxel.width
        elif w < -pyxel.width:
            self.__w = -w
        else:
            self.__w = w

    @h.setter
    def h(self, h):
        if type(h) is not int:
            raise TypeError("h must be an integer")
        elif h > pyxel.height:
            self.__h = pyxel.height
        elif h < -pyxel.height:
            self.__h = -h
        else:
            self.__h = h

    @sprite.setter
    def sprite(self, sprite):
        if type(sprite) is not int:
            raise TypeError("sprite must be an integer")
        elif sprite > pyxel.width:
            self.__sprite = pyxel.width
        elif sprite < 0:
            self.__sprite = 0
        else:
            self.__sprite = sprite
