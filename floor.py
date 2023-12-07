import pyxel


td = 8  # tile dimension


class Floor:
    def __init__(self):
        pass

    def draw():
        for i in range(pyxel.width//td):
            pyxel.blt(0 + i * 2*td, pyxel.height-2*td, 0, 120, 176, 16, 16, 0)
