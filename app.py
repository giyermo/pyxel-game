import pyxel
from board import Board
# importar enemigos
td = 8  # tile dimension
WIDTH = 32*td
HEIGHT = 28*td


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Bros", fps=60)
        pyxel.load("assets/assets1.pyxres")

        global board
        board = Board()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        board.update()

    def draw(self):
        pyxel.cls(0)
        board.draw()


App()
