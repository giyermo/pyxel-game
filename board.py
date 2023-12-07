import pyxel
from pipe import Pipe
from platforms import Platform
from floor import Floor


class Board:
    def __init__(self):
        global floor
        floor = Floor
        global pipe1
        pipe1 = Pipe("top", "right")
        global pipe2
        pipe2 = Pipe("top", "left")
        global pipe3
        pipe3 = Pipe("bottom", "right")
        global pipe4
        pipe4 = Pipe("bottom", "left")
        global platform1
        platform1 = Platform(0, pyxel.height-20*8, 1, 14)
        global platform2
        platform2 = Platform(pyxel.width-14*8, pyxel.height-20*8, 1, 14)
        global platform3
        platform3 = Platform(0, pyxel.height-13*8, 1, 4)
        global platform4
        platform4 = Platform(pyxel.width-4*8, pyxel.height-13*8, 1, 4)
        global platform5
        platform5 = Platform(8*8, pyxel.height-14*8, 1, 16)
        global platform6
        platform6 = Platform(0, pyxel.height-8*8, 1, 10)
        global platform7
        platform7 = Platform(pyxel.width-10*8, pyxel.height-8*8, 1, 10)

    def update(self):
        pass

    def draw(self):
        floor.draw()
        pipe1.draw()
        pipe2.draw()
        pipe3.draw()
        pipe4.draw()
        platform1.draw()
        platform2.draw()
        platform3.draw()
        platform4.draw()
        platform5.draw()
        platform6.draw()
        platform7.draw()
