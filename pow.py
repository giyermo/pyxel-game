import pyxel

td = 8  # Tile dimension (assuming it's a constant value)

class Pow:
    def __init__(self, x=(32 * td // 2 - td), y=(28 * td - 9 * td), phase=1) -> None:
        """Initialize Pow object."""
        self.x = x
        self.y = y
        self.phase = phase
        self.u = 136
        self.v = 176
        self.w = td * 2
        self.h = td * 2

    # Property getters and setters to enforce constraints on attributes
    @property
    def x(self):
        """Getter for x-coordinate."""
        return self.__x

    @property
    def y(self):
        """Getter for y-coordinate."""
        return self.__y

    @property
    def phase(self):
        """Getter for phase."""
        return self.__phase

    @x.setter
    def x(self, x):
        """Setter for x-coordinate with type and value checks."""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """Setter for y-coordinate with type and value checks."""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            self.__y = 0
        else:
            self.__y = y

    @phase.setter
    def phase(self, phase):
        """
        Setter for phase with type and value checks.

        Phase must be an integer between 1-5.
        """
        if isinstance(phase, int) is False:
            raise TypeError("phase must be an int")
        elif phase not in range(1, 6):
            raise ValueError("phase must be between 1-5")
        else:
            self.__phase = phase

    def choose_sprite(self):
        """Choose sprite based on the phase to update u and h attributes."""
        if self.phase == 2 or self.phase == 3:
            self.u = 152
            self.h = 13
        if self.phase == 4 or self.phase == 5:
            self.u = 168
            self.h = 9

    def update(self):

        pass

    def draw(self):
        """Draw the Pow object"""
        self.choose_sprite()
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h, colkey=0)

