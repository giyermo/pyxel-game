import pyxel
from board import Board
# importar enemigos
td = 8
WIDTH = 32*td
HEIGHT = 28*td


class App:
    '''This class is where the board is loaded , the title and the dimensions of the game are given too'''
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Bros", fps=60)
        pyxel.load("assets/assets1.pyxres")
        self.board = Board()

        pyxel.run(self.update, self.draw)

    def update(self):  # Some shortcuts to different phases of the game
        if pyxel.btn(pyxel.KEY_0):
            self.board.phase = 0
            self.board.phase_frame_counter = 0
        elif pyxel.btn(pyxel.KEY_1):
            for enemy in self.board.enemies:
                self.board.enemies.remove(enemy)
            self.board.phase = 1
            self.board.phase_frame_counter = 0
        elif pyxel.btn(pyxel.KEY_2):
            for enemy in self.board.enemies:
                self.board.enemies.remove(enemy)
            self.board.phase = 2
            self.board.phase_frame_counter = 0
        elif pyxel.btn(pyxel.KEY_3):
            for enemy in self.board.enemies:
                self.board.enemies.remove(enemy)
            self.board.phase = 3
            self.board.phase_frame_counter = 0
        elif pyxel.btn(pyxel.KEY_4):
            for enemy in self.board.enemies:
                self.board.enemies.remove(enemy)
            self.board.phase = 4
            self.board.phase_frame_counter = 0
        elif pyxel.btn(pyxel.KEY_5):
            for enemy in self.board.enemies:
                self.board.enemies.remove(enemy)
            self.board.phase = 5
            self.board.phase_frame_counter = 0
        elif pyxel.btn(pyxel.KEY_6):
            for enemy in self.board.enemies:
                self.board.enemies.remove(enemy)
            self.board.phase = 6
            self.board.phase_frame_counter = 0
        elif pyxel.btn(pyxel.KEY_7):
            for enemy in self.board.enemies:
                self.board.enemies.remove(enemy)
            self.board.phase = 7
            self.board.phase_frame_counter = 0
        self.board.update()

    def draw(self): # Draws the board
        pyxel.cls(0)
        self.board.draw()


App()
