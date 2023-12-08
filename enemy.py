import pyxel
from character import Character
class Enemy(Character):
    def __init__(self, x, y, u, v, w, h, sprite=0):
        super().__init__(x, y, u, v, w, h, sprite)
        self.direction = -1 # tiene que cambiar dependiendo del lado del que salga, si sale de la izquierda positivo si sale de la derecha negativo
        self.dy = 0
        self.is_alive = True
    def update(self):

        self.dx = self.direction
        self.dy = min(self.dy + 1, 3)
        """if self.direction < 0 :and is_wall(self.x - 1, self.y + 4): #cambiar con la condicion de detectar colition
            self.direction = 1
        elif self.direction > 0  and is_wall(self.x + 8, self.y + 4):
            self.direction = -1
            self.x, self.y, self.dx, self.dy = push_back(self.x, self.y, self.dx, self.dy)"""

    def draw(self): # cambia dependiendo del enemigo

        pyxel.blt(self.x, self.y, 0, 0, 24, 0, 8, 2) # mañana ajusto cada pixel para esto y hago las demas clases
def draw(self):
        # Implement enemy-specific drawing logic here 24  a 32 y 0 a  8
        pyxel.blt(self.x, self.y, self.sprite, self.u, self.v, self.w, self.h, colkey=0)

    # Add any additional methods or properties specific to the enemy