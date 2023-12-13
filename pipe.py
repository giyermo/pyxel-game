import pyxel

td = 8  # tile dimension


class Pipe:
    def __init__(self, type, direction):
        """
        Initialize Pipe object.
        """
        self.type = type
        self.direction = direction

    # Property getters and setters to enforce constraints on attributes
    @property
    def type(self):

        return self.__type

    @property
    def direction(self):

        return self.__direction

    @type.setter
    def type(self, type):
        """
        Setter for pipe type with value checks.
        """
        if type not in ["top", "bottom"]:
            raise ValueError("type must be either top or bottom")
        else:
            self.__type = type

    @direction.setter
    def direction(self, direction):
        """
        Setter for pipe direction with value checks.
        """
        if direction not in ["left", "right"]:
            raise ValueError("direction must be either left or right")
        else:
            self.__direction = direction

    def draw(self):
        """
        Draw the pipe on the screen
        """
        if self.type == "top":
            pyxel.blt(
                0 if self.direction == "right" else pyxel.width - 48,
                pyxel.height - 24 * td,
                0,
                64,
                176,
                48 if self.direction == "right" else -48,
                32,
                0,
            )
        else:
            pyxel.blt(
                0 if self.direction == "right" else pyxel.width - 32,
                pyxel.height - 5 * td,
                0,
                48,
                184,
                32 if self.direction == "right" else -32,
                24,
                0,
            )

