import pyxel


td = 8  # tile dimension


class Character:
    def __init__(self, x, y, u, v, w, h, terminal_velocity=3, sprite=0):
        """Initialize a Character object."""
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
        """Return a string representation of the Character object."""
        return f"{id(self)} x={self.x} y={self.y} w={self.w} h={self.h}"

    def __repr__(self) -> str:
        """Return a string representation of the Character object."""
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
        """Set the X-coordinate of the character."""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """Set the Y-coordinate of the character."""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            self.__y = 0
        else:
            self.__y = y

    @u.setter
    def u(self, u):
        """Set the sprite X-coordinate for rendering."""
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
        """Set the sprite Y-coordinate for rendering."""
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
        """Set the width of the character."""
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
        """Set the height of the character."""
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
        """Set the sprite index for rendering."""
        if type(sprite) is not int:
            raise TypeError("sprite must be an integer")
        elif sprite > pyxel.width:
            self.__sprite = pyxel.width
        elif sprite < 0:
            self.__sprite = 0
        else:
            self.__sprite = sprite

    def check_collision(self, other):
        """Check collision with another character.

        Args:
            other (Character): Another character object.

        Returns:
            bool: True if a collision occurred, False otherwise.
        """
        self_left = self.x + self.dx
        self_right = self.x + self.dx + abs(self.w)

        other_left = other.x + other.dx
        other_right = other.x + other.dx + abs(other.w)

        x_overlap = (self_left < other_left and self_right > other_left) or (
            self_left < other_right and self_right > other_right) or (
                self_left >= other_left and self_right <= other_right)
        y_overlap = not (self.y + self.h + self.dy <=
                         other.y or self.y + self.dy >= other.y + other.h)

        if x_overlap and y_overlap:
            return True

        return False

    @staticmethod
    def detect_collision(self, object):
        '''Returns if a character is collding with a platform, which direction is the collision.'''
        if self.y + self.h + self.dy < object.y or self.y + self.dy > object.y + object.h:
            # not under or over it
            return (False, "No collision")
        if self.x + abs(self.w) + self.dx < object.x:
            # not to the side of it
            return (False, "No collision")
        if self.x > object.x + object.w:
            # not to the side of it
            return (False, "No collision")
        if abs(self.dy) >= abs(self.dx):
            # if the character is moving more vertically, the collision should be vertical
            return (True, "vertical")
        else:
            return (True, "horizontal")

    def on_platform(self, platform):
        '''Returns if a character is on a platform.'''
        if self.y + self.h + self.dy == platform.y - 1:
            if self.x + abs(self.w) + self.dx < platform.x or self.x > platform.x + platform.w:
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
            return platform, collision, direction
        return None, None, None

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
