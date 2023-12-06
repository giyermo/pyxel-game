import pyxel

WIDTH = 256
HEIGHT = 208


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Bros")
        pyxel.load("assets/assets1.pyxres")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 128, 256, 208)


App()
