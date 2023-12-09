import pyxel
from character import Character
class Enemy2(Character):

        def __init__(self) -> None:
            super().__init__(x=40, y=10, u=0, v=40, w=16, h=16, sprite=0)
            self.direction = 1  # Start moving to the right
            self.is_alive = True
            self.dy = 0
            self.backwards = False
            self.running_sprites = [0, 16, 32]
            self.frame_count = 0
            self.move_interval = 6  # Move every 0.1 seconds (60 frames per second)
        def update(self):

            self.dy = min(self.dy + 1, 3)
            self.dx = 1
            self.frame_count += 1  # Counts the frames for the animation to be fluid
            # Check if the enemy has moved off-screen to the right
            if self.frame_count % self.move_interval == 0:
                self.x += self.dx  # Update the x position based on the direction
                self.dy = min(self.dy + 1, 3)

            self.movement()
        def movement (self):
            #Falta golpe y cuando se enfada pero eso en el update y una funcion nueva
            frame_duration = 0.1
            frame_index = int((self.frame_count / 60) / frame_duration) % len(self.running_sprites)

            if self.direction > 0:  # Moving right
                self.u = self.running_sprites[frame_index]
                self.w = abs(self.w)  # Ensure width is positive
            elif self.direction < 0:  # Moving left
                self.u = self.running_sprites[frame_index] + 16  # Shift to the next set of sprites for left
                self.w = -abs(self.w)  # Flip the sprite horizontally
            #elif self.backwards:


        def draw(self):
            # Use class attributes to determine the position and appearance
            pyxel.blt(self.x, self.y, self.sprite, self.u, self.v, -self.w, self.h, colkey=0)