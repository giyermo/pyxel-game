import pyxel


td = 8  # tile dimension


class Character:
    def __init__(self, x, y, u, v, w, h, terminal_velocity=3, sprite=0):
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.sprite = sprite
        self.terminal_velocity = terminal_velocity
        self.is_falling = False

    def __str__(self) -> str:
        return f"x={self.x} y={self.y} w={self.w} h={self.h}"

    def __repr__(self) -> str:
        return self.__str__()

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

    def check_collision(self, other):
        self_left = self.x + self.dx
        self_right = self.x + self.dx + abs(self.w)

        other_left = other.x + other.dx
        other_right = other.x + other.dx + abs(other.w)

        x_overlap = (self_left < other_left and self_right > other_left) or (
            self_left < other_right and self_right > other_right) or (
                self_left >= other_left and self_right <= other_right)
        y_overlap = not (self.y + self.h + self.dy <=
                         other.y or self.y + self.dy >= other.y + other.h)

        print(x_overlap, y_overlap)
        if x_overlap and y_overlap:
            return True

        return False

    @staticmethod
    def detect_collision(self, object):
        '''Returns if a character is collding with a platform, which direction is the collision.'''
        if self.y + self.h + self.dy < object.y or self.y + self.dy > object.y + td:
            # not under or over it
            return (False, "No collision")
        # or self.x + self.dx > object.x + object.length:
        if self.x + abs(self.w) + self.dx < object.x:
            # not to the side of it
            return (False, "No collision")
        if self.x > object.x + object.length:
            # not to the side of it
            return (False, "No collision")
        if abs(self.dy) >= abs(self.dx):
            # if the character is moving more vertically, the collision should be vertical
            return (True, "vertical")
        else:
            return (True, "horizontal")

        # if self.x + self.w < object.x or self.x > object.x + object.length:
            # self was outside the platform
        # if self.x + self.w + self.dx < object.x or self.x > object.x + object.length:  # not under or over it
        #     return (False, "No collision")
        # elif (self.x + self.w + self.dx > object.x and self.x + self.dx < object.x) or (self.x + self.w + self.dx > object.x + object.length and self.x + self.dx < object.x + object.length):  # between borders
        #     if self.y + self.h + self.dy < object.y or self.y > object.y + td:  # not to the side of it
        #         return (False, "No collision")
        #     # to the side of it in between borders
        #     elif (self.y + self.h + self.dy > object.y + td and self.y + self.dy < object.y):
        #         return (True, "horizontal")
        #     else:
        #         return (True, "vertical")
        #     # elif (self.y + self.h + self.dy > object.y and self.y + self.dy < object.y) or (self.y + self.h + self.dy > object.y + td and self.y + self.dy < object.y + td):
        # else:  # under or over it
        #     if self.y + self.h + self.dy < object.y or self.y + self.dy > object.y + td:  # not to the side of it
        #         return (False, "No collision")
        #     else:  # if (self.y + self.h + self.dy > object.y and self.y + self.dy < object.y) or (self.y + self.h + self.dy > object.y + td and self.y + self.dy < object.y + td) or (self.y + self.h + self.dy > object.y + td and self.y + self.dy < object.y):  # to the side of it
        #         return (True, "vertical")

    def on_platform(self, platform):
        '''Returns if a character is on a platform.'''
        if self.y + self.h + self.dy == platform.y - 1:
            if self.x + abs(self.w) + self.dx < platform.x or self.x > platform.x + platform.length:
                return False
            else:
                return True
        else:
            return False

    def check_falling(self, platforms):
        on_platform = False
        i = 0

        while not on_platform and i < len(platforms):
            if self.on_platform(platforms[i]):
                on_platform = True
            i += 1

        self.is_falling = not on_platform

    def push_back(self, platform):
        '''Push a character back to the platform it is colliding with.'''
        collision, direction = self.detect_collision(self, platform)
        if collision:
            if direction == "horizontal":
                sign = -1 if self.dx > 0 else 1
                while collision:
                    self.dx += sign
                    collision, direction = self.detect_collision(
                        self, platform)
                self.is_falling = True
            else:
                sign = -1 if self.dy > 0 else 1
                if sign == -1:
                    self.is_falling = False
                while collision:
                    self.dy += sign
                    collision, direction = self.detect_collision(
                        self, platform)
        # else:
        #     self.is_falling = True

        # abs_dx = abs(dx)
        # abs_dy = abs(dy)
        # if abs_dx > abs_dy:
        #     print("pushing x")
        #     sign = -1 if dx > 0 else 1
        #     for _ in range(abs_dx):
        #         if self.detect_collision(x + sign, y, w, h, dx, dy, platform):
        #             x += sign
        #             print(x)
        #     sign = -1 if dy > 0 else 1
        #     for _ in range(abs_dy):
        #         if self.detect_collision(x, y + sign, w, h, dx, dy, platform):
        #             y += sign
        #             print(y)
        # else:
        #     print("pushing y")
        #     # sign is negative if charcter is going down and the viceverse
        #     sign = -1 if dy > 0 else 1
        #     for _ in range(abs_dy):
        #         if self.detect_collision(x, y + sign, w, h, dx, dy, platform):
        #             y += sign
        #             print(y, dy)
        #     # sign is negative if charcter is going right and viceverse
        #     sign = -1 if dx > 0 else 1
        #     for _ in range(abs_dx):
        #         if self.detect_collision(x + sign, y, w, h, dx, dy, platform):
        #             x += sign
        #             print(x, dx)
        # return x, y, dx, dy
