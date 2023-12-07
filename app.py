import pyxel
from board import Board
from mario import Mario

WIDTH = 32*8
HEIGHT = 28*8


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Bros")
        pyxel.load("assets/assets1.pyxres")
        global board
        board = Board()
        global mario
        mario = Mario()
        pyxel.run(self.update, self.draw)

    def update(self):
        board.update()
        mario.update()

    def draw(self):
        pyxel.cls(0)
        board.draw()
        mario.draw()


App()
