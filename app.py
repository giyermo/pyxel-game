import pyxel
from board import Board
# importar enemigos
WIDTH = 32*td
HEIGHT = 28*td


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Bros", fps=60)
        pyxel.load("assets/assets1.pyxres")
        self.board = Board()

        pyxel.run(self.update, self.draw)

    def update(self):
        self.board.update()

    def draw(self):
        pyxel.cls(0)
        self.board.draw()


App()
