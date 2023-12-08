import pyxel

td = 8  # tile dimension


class Platform:


    platform = []

    def __init__(self, x, y, type, length):
        self.x = x
        self.y = y
        self.type = type
        self.length = length
        self.platform_tile_list = []
        Platform.platform.append(self)

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


#3º intento xd
    def draw(self):
        for i in range(self.length):
            tile_x = self.x + i * td
            tile_y = self.y

            if self.type == 1:
                pyxel.blt(tile_x, tile_y, 0, 0, 224, 8, 8, 0)
            elif self.type == 2:
                pyxel.blt(tile_x, tile_y, 0, 0, 8, 8, 8, 0)
            elif self.type == 3:
                pyxel.blt(tile_x, tile_y, 0, 0, 16, 8, 8, 0)
            elif self.type == 4:
                pyxel.blt(tile_x, tile_y, 0, 0, 24, 8, 8, 0)
            else:
                pyxel.blt(tile_x, tile_y, 0, 0, 8, 8, 8, 0)

            self.platform_tile_list.append((self.type, tile_x, tile_y))

        for platform in Platform.platform:
                print(f"Platform at X: {platform.x}, Y: {platform.y}")

        """def draw(self):
                   print("This works")
                   for i in range(self.length):
                       tile_x = self.x + i * td
                       tile_y = self.y

                       if self.type == 1:
                           pyxel.blt(tile_x, tile_y, 0, 0, 224, 8, 8, 0)
                       elif self.type == 2:
                           pyxel.blt(tile_x, tile_y, 0, 0, 8, 8, 8, 0)
                       elif self.type == 3:
                           pyxel.blt(tile_x, tile_y, 0, 0, 16, 8, 8, 0)
                       elif self.type == 4:
                           pyxel.blt(tile_x, tile_y, 0, 0, 24, 8, 8, 0)
                       else:
                           pyxel.blt(tile_x, tile_y, 0, 0, 8, 8, 8, 0)

                       # Append a tuple with type and coordinates to the list
                       self.platform_tile_list.append((self.type, tile_x, tile_y))
                   for tile_info in self.platform_tile_list:
               print(f"    Type: {tile_info[0]}, X: {tile_info[1]}, Y: {tile_info[2]}")"""






        """def draw(self):
        if self.type == 1:
            for i in range(self.length):
                tile_x = self.x + i * td # separando en cada coordenada para guardarlo en la lista
                tile_y = self.y
                pyxel.blt(self.x + i * td, self.y, 0, 0, 224, 8, 8, 0)

                self.platform_tile_list.append((self.type, tile_x, tile_y)) #guardarlo en una lista

                self.platform_tile_list.append([self.x + i * td, self.y])
        elif self.type == 2:
            for i in range(self.length):
                tile_x = self.x + i * td  # separando en cada coordenada para guardarlo en la lista
                tile_y = self.y

                pyxel.blt(self.x + i * td, self.y, 0, 0, 8, 8, 8, 0)
                self.platform_tile_list.append([self.x + i * td, self.y])

                self.platform_tile_list.append((self.type, tile_x, tile_y))  # guardarlo en una lista

        elif self.type == 3:
            for i in range(self.length):
                tile_x = self.x + i * td  # separando en cada coordenada para guardarlo en la lista
                tile_y = self.y

                pyxel.blt(self.x + i * td, self.y, 0, 0, 16, 8, 8, 0)
                self.platform_tile_list.append([self.x + i * td, self.y])

                self.platform_tile_list.append((self.type, tile_x, tile_y))  # guardarlo en una lista
        elif self.type == 4:
            for i in range(self.length):
                tile_x = self.x + i * td  # separando en cada coordenada para guardarlo en la lista
                tile_y = self.y

                pyxel.blt(self.x + i * td, self.y, 0, 0, 24, 8, 8, 0)
                self.platform_tile_list.append([self.x + i * td, self.y])

                self.platform_tile_list.append((self.type, tile_x, tile_y))  # guardarlo en una lista
        else:
            for i in range(self.length):
                tile_x = self.x + i * td  # separando en cada coordenada para guardarlo en la lista
                tile_y = self.y

                pyxel.blt(self.x + i * td, self.y, 0, 0, 8, 8, 8, 0)
                self.platform_tile_list.append([self.x + i * td, self.y])



        for tile_info in self.platform_tile_list:
            print(f"Type: {tile_info[0]}, X: {tile_info[1]}, Y: {tile_info[2]}")
"""

