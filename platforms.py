import pyxel

td = 8  # tile dimension


class Platform:
    def __init__(self, x, y, type, w, h):
        self.x = x
        self.y = y
        self.type = type
        self.w = w
        self.h = h
        self.platform_tile_list = []

    def __str__(self) -> str:
        return f"Platform: x={self.x}, y={self.y}, type={self.type}, length={self.w}"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def type(self):
        return self.__type

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            self.__y = 0
        else:
            self.__y = y

    @type.setter
    def type(self, type):
        if isinstance(type, int) is False:
            raise TypeError("type must be an int")
        elif type not in range(0, 6):
            raise ValueError("type must be between 0-5")
        else:
            self.__type = type

    @w.setter
    def w(self, w):
        if type(w) is not int:
            raise TypeError("length must be an integer")
        elif w < 1:
            raise ValueError("length must be greater than 0")
        else:
            self.__w = w

    @h.setter
    def h(self, h):
        if type(h) is not int:
            raise TypeError("height must be an integer")
        elif h < 1:
            raise ValueError("height must be greater than 0")
        else:
            self.__h = h

    def update(self):
        pass

    def draw(self):
        if self.type == 0:
            for i in range(pyxel.width//td):
                pyxel.blt(self.x + i * 2 * td, self.y, 0, 120, 176, 16, 16, 0)
                self.platform_tile_list.append([self.x + i * 2 * td, self.y])
        elif self.type == 1:
            for i in range(self.w//td):
                pyxel.blt(self.x + i * td, self.y, 0, 0, 224, 8, 8, 0)
                self.platform_tile_list.append([self.x + i * td, self.y])
        elif self.type == 2:
            for i in range(self.w//td):
                pyxel.blt(self.x + i * td, self.y, 0, 8, 224, 8, 8, 0)
                self.platform_tile_list.append([self.x + i * td, self.y])
        elif self.type == 3:
            for i in range(self.w//td):
                pyxel.blt(self.x + i * td, self.y, 0, 8, 232, 8, 8, 0)
                self.platform_tile_list.append([self.x + i * td, self.y])
        elif self.type == 4:
            for i in range(self.w//td):
                pyxel.blt(self.x + i * td, self.y, 0, 0, 232, 8, 8, 0)
                self.platform_tile_list.append([self.x + i * td, self.y])
        else:
            for i in range(self.w//td):
                pyxel.blt(self.x + i * td, self.y, 0, 16, 224, 8, 8, 0)
                self.platform_tile_list.append([self.x + i * td, self.y])
