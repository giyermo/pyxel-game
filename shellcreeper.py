import pyxel
from character import Character


class Shellcreeper(Character):
    def __init__(self) -> None:
        super().__init__(x=180, y=135, u=0, v=24, w=16, h=16, terminal_velocity=3, sprite=0)
        self.direction = 1  # Start moving to the right
        self.is_alive = True
        self.dy = 0
        self.backwards = False
        self.running_sprites = [0, 16, 32]
        self.frame_count = 0
        self.move_interval = 6  # Move every 0.1 seconds (60 frames per second)
        self.is_moving = True

    def fall(self):
        '''Pushes down mario if he is in the air quicker each time until it reaches a terminal velocity.'''
        self.dy += 2
        self.dy = min(self.dy, self.terminal_velocity)

    def calculate_movement(self):
        self.dy = min(self.dy + 1, 3)
        self.dx = 1
        self.frame_count += 1  # Counts the frames for the animation to be fluid
        # Check if the enemy has moved off-screen to the right

        if self.is_moving:
            self.movement()
        if self.is_falling:
            self.fall()

    def update(self):
        print(self.dx)
        if self.frame_count % self.move_interval == 0:
            self.x += self.dx  # Update the x position based on the direction
        if self.x < 0:
            self.x = pyxel.width - abs(self.w)
        elif self.x + abs(self.w) > pyxel.width:
            self.x = 0
        # min(self.y + self.dy, pyxel.height - 2*td - self.h)
        self.y = self.y + self.dy

    def movement(self):
        # Falta golpe y cuando se enfada pero eso en el update y una funcion nueva
        frame_duration = 0.1
        frame_index = int((self.frame_count / 60) /
                          frame_duration) % len(self.running_sprites)

        if self.direction > 0:  # Moving right
            self.u = self.running_sprites[frame_index]
            self.w = abs(self.w)  # Ensure width is positive
        elif self.direction < 0:  # Moving left
            # Shift to the next set of sprites for left
            self.u = self.running_sprites[frame_index] + 16
            self.w = -abs(self.w)  # Flip the sprite horizontally
        # elif self.backwards:

    def draw(self):
        # Use class attributes to determine the position and appearance
        pyxel.blt(self.x, self.y, self.sprite, self.u,
                  self.v, -self.w, self.h, colkey=0)

    # def hit(self): for mario hitting enemies


"""def __init__(self) -> None:
                        super().__init__(120, 168, 0, 24, 0, 8, 2)
                        self.direction = -1 # tiene que cambiar dependiendo del lado del que salga, si sale de la izquierda positivo si sale de la derecha negativo
                        self.dy = self.direction
                        self.is_alive = True
                    def update(self):
                
                        self.dx = -1
                
                        self.dy = min(self.dy + 1, 3)
                
                
                
                        if self.direction < 0 :and is_wall(self.x - 1, self.y + 4): #cambiar con la condicion de detectar colition
                            self.direction = 1
                        elif self.direction > 0  and is_wall(self.x + 8, self.y + 4):
                            self.direction = -1
                            self.x, self.y, self.dx, self.dy = push_back(self.x, self.y, self.dx, self.dy)
                
                    def draw(self): # cambia dependiendo del enemigo
                
                        pyxel.blt(self.x, self.y, self.sprite, self.u, self.v, self.w, self.h, colkey=0)# mañana ajusto cada pixel para esto y hago las demas clases
                    def draw(self):
                        # Implement enemy-specific drawing logic here 24  a 32 y 0 a  8
                        pyxel.blt(self.x, self.y, self.sprite, self.u, self.v, self.w, self.h, colkey=0)"""

# Add any additional methods or properties specific to the enemy
