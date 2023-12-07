import pyxel


WIDTH = 256
HEIGHT = 200


class Platform:
    def __init__(self, x, y, type, length):
        self.x = x
        self.y = y
        self.type = type
        self.length = length

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
    def length(self):
        return self.__length

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
        elif type not in range(1, 6):
            raise ValueError("type must be between 1-5")
        else:
            self.__type = type

    @length.setter
    def length(self, length):
        if type(length) is not int:
            raise TypeError("length must be an integer")
        elif length < 1:
            raise ValueError("length must be greater than 0")
        else:
            self.__length = length

    def update(self):
        pass

    def draw(self):
        if self.type == 1:
            for i in range(self.length):
                pyxel.blt(self.x + i * 8, self.y, 0, 0, 224, 8, 8, 0)
        elif self.type == 2:
            for i in range(self.length):
                pyxel.blt(self.x + i * 8, self.y, 0, 0, 8, 8, 8, 0)
        elif self.type == 3:
            for i in range(self.length):
                pyxel.blt(self.x + i * 8, self.y, 0, 0, 16, 8, 8, 0)
        elif self.type == 4:
            for i in range(self.length):
                pyxel.blt(self.x + i * 8, self.y, 0, 0, 24, 8, 8, 0)
        else:
            for i in range(self.length):
                pyxel.blt(self.x + i * 8, self.y, 0, 0, 8, 8, 8, 0)
