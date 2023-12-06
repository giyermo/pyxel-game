import pyxel
from mario import Mario

WIDTH = 256
HEIGHT = 208


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Bros")
        pyxel.load("assets/assets1.pyxres")
        global mario
        mario = Mario()
        pyxel.run(self.update, self.draw)

    def update(self):
        mario.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 128, 256, 208)
        mario.draw()


App()
