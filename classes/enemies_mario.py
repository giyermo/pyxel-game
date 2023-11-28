



class Enemies :
#this class represents the basic characteristics of any moving character (enemies or mario), there are three total enemies and one bullet spawned somwhere and directed to the player

# At least 30
# enemies of all types must appear throughout the game.
# Intento crear una clase con las cosas comunes de los personajes que se mueven, para luego hacer lo de inheritance
# cosas comunes : posicion en el mapa, movimiento,
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.direction = 1
        self.is_falling = False
    @property
    def x(self) :
        return self.__x
    #@x.setter





