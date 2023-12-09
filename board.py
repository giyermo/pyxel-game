import pyxel
from mario import Mario
from enemy1 import Enemy
from enemy2 import Enemy2
from enemy3 import Enemy3
from pipe import Pipe
from platforms import Platform
from floor import Floor


td = 8  # tile dimension


class Board:
    def __init__(self):
        self.create_platforms()
        self.create_pipes()

        global mario
        mario = Mario()

        global enemy
        enemy = Enemy()

        global enemy2
        enemy2 = Enemy2()

        global enemy3
        enemy3 = Enemy3()

    @staticmethod
    def create_platforms():
        global platforms
        platforms = [
            Platform(0, pyxel.height-20*td, 1, 14*td),
            Platform(pyxel.width-14*td,
                     pyxel.height-20*td, 1, 14*td),
            Platform(0, pyxel.height-13*td, 1, 4*td),
            Platform(pyxel.width-4*td, pyxel.height-13*td, 1, 4*td),
            Platform(pyxel.width//2-8*td,
                     pyxel.height-14*td, 1, 16*td),
            Platform(0, pyxel.height-8*td, 1, 10*td),
            Platform(pyxel.width-10*td, pyxel.height-8*td, 1, 10*td)
        ]
        global floor
        floor = Floor

    @staticmethod
    def create_pipes():
        global pipes
        pipes = [Pipe("top", "right"),
                 Pipe("top", "left"),
                 Pipe("bottom", "right"),
                 Pipe("bottom", "left")]

    def update(self):
        mario.calculate_movement()
        enemy.update()
        enemy2.update()
        enemy3.update()

        print("calculating",
              mario.x, mario.y, mario.dx, mario.dy)
        # for platform in platforms:
        #     values = mario.push_back(
        #         mario.x, mario.y, mario.w, mario.h, mario.dx, mario.dy, platform)

        mario.update()
        print("updating",
              mario.x, mario.y, mario.dx, mario.dy)

    def draw(self):
        for platform in platforms:
            platform.draw()
        for pipe in pipes:
            pipe.draw()
        floor.draw()
        mario.draw()
        enemy.draw()
        enemy2.draw()
        enemy3.draw()
