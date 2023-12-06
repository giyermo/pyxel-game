import pyxel

WIDTH = 320
HEIGHT = 240


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
        pyxel.blt(WIDTH // 2 - 8, HEIGHT // 2 - 12, 0, 0, 0, 16, 24, colkey=0)
        pyxel.rect(self.x, 0, 8, 8, 9)


App()
