import pyxel


from board import Board
from mario import Mario
#importar enemigos
td = 8  # tile dimension
WIDTH = 32*td
HEIGHT = 28*td


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Bros")
        pyxel.load("assets/assets1.pyxres")

        global board
        board = Board()

        global mario
        mario = Mario()

        # aqui el global de cada enemigo




        pyxel.run(self.update, self.draw)
    def update(self):
        board.update()
        mario.update()


    def draw(self):
        pyxel.cls(0)
        board.draw()
        mario.draw()
        # Falta el draw de cada enemigo pero cuando esten terminadas las clases
App()
