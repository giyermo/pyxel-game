import pyxel
from board import Board
# importar enemigos
td = 8
WIDTH = 32*td
HEIGHT = 28*td


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Bros", fps=60)
        pyxel.load("assets/assets1.pyxres")
        self.board = Board()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_0):
            self.board.phase = 0
            self.board.phase_frame_counter = 0
        elif pyxel.btn(pyxel.KEY_1):
            self.board.phase = 1
            self.board.phase_frame_counter = 0
        elif pyxel.btn(pyxel.KEY_2):
            self.board.phase = 2
            self.board.phase_frame_counter = 0
        elif pyxel.btn(pyxel.KEY_3):
            self.board.phase = 3
            self.board.phase_frame_counter = 0
        self.board.update()

    def draw(self):
        pyxel.cls(0)
        self.board.draw()


App()
