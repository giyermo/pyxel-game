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
        global platform_list
        platform_list = []
        floor = Floor
        platform_list.append(floor)
        platform1 = Platform(0, pyxel.height-20*td, 1, 14)
        platform2 = Platform(pyxel.width-14*td, pyxel.height-20*td, 1, 14)
        platform3 = Platform(0, pyxel.height-13*td, 1, 4)
        platform4 = Platform(pyxel.width-4*td, pyxel.height-13*td, 1, 4)
        platform5 = Platform(pyxel.width//2-8*td, pyxel.height-14*td, 1, 16)
        platform6 = Platform(0, pyxel.height-8*td, 1, 10)
        platform7 = Platform(pyxel.width-10*td, pyxel.height-8*td, 1, 10)
        for i in range(7):
            platform_list.append(vars()['platform'+str(i+1)])

    @staticmethod
    def create_pipes():
        global pipe_list
        pipe_list = []
        pipe1 = Pipe("top", "right")
        pipe2 = Pipe("top", "left")
        pipe3 = Pipe("bottom", "right")
        pipe4 = Pipe("bottom", "left")
        for i in range(4):
            pipe_list.append(vars()['pipe'+str(i+1)])

    def update(self):
        pass

    def draw(self):
        for platform in platform_list:
            platform.draw()
        for pipe in pipe_list:
            pipe.draw()
