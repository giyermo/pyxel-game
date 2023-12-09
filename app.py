import pyxel
from enemy2 import Enemy2
from enemy1 import Enemy
from board import Board
from mario import Mario
from enemy3 import Enemy3
#importar enemigos
td = 8  # tile dimension
WIDTH = 32*td
HEIGHT = 28*td


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Bros",fps=60)
        pyxel.load("assets/assets1.pyxres")

        global board
        board = Board()

        global mario
        mario = Mario()

        global enemy
        enemy = Enemy()

        global enemy2
        enemy2 = Enemy2()
        # aqui el global de cada enemigo

        global enemy3
        enemy3 = Enemy3()




        pyxel.run(self.update, self.draw)
    def update(self):
        board.update()
        mario.update()
        enemy.update()
        enemy2.update()
        enemy3.update()
    def draw(self):
        pyxel.cls(0)
        board.draw()
        mario.draw()
        enemy.draw()
        enemy2.draw()
        enemy3.draw()
        # Falta el draw de cada enemigo pero cuando esten terminadas las clases
App()
