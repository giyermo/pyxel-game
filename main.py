import pyxel

WIDTH = 160
HEIGHT = 120


class App:
    def __init__(self):
        pyxel.init(160, 120, title="Mario Bros")
        pyxel.load("assets/assets1.pyxres")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(WIDTH // 2, HEIGHT // 2, 0, 0, 0, 16, 24, colkey=0)
        pyxel.rect(self.x, 0, 8, 8, 9)


App()
