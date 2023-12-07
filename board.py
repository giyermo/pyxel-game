import pyxel
from pipe import Pipe
from platforms import Platform
from floor import Floor


td = 8  # tile dimension


class Board:
    def __init__(self):
        self.create_platforms()
        self.create_pipes()

    @staticmethod
    def create_platforms():
        global platforms
        platforms = [
            Platform(0, pyxel.height-20*td, 1, 14),
            Platform(pyxel.width-14*td,
                     pyxel.height-20*td, 1, 14),
            Platform(0, pyxel.height-13*td, 1, 4),
            Platform(pyxel.width-4*td, pyxel.height-13*td, 1, 4),
            Platform(pyxel.width//2-8*td,
                     pyxel.height-14*td, 1, 16),
            Platform(0, pyxel.height-8*td, 1, 10),
            Platform(pyxel.width-10*td, pyxel.height-8*td, 1, 10)
        ]
        floor = Floor
        platforms.append(floor)

    @staticmethod
    def create_pipes():
        global pipes
        pipes = [Pipe("top", "right"),
                 Pipe("top", "left"),
                 Pipe("bottom", "right"),
                 Pipe("bottom", "left")]

    def update(self):
        pass

    def draw(self):
        for platform in platforms:
            platform.draw()
        for pipe in pipes:
            pipe.draw()
