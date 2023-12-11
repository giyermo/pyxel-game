import pyxel
from character import Character

td = 8


class Shellcreeper(Character):
    def __init__(self, direction=1) -> None:
        super().__init__(x=0, y=4*td, u=0, v=24, w=16, h=16,
                         terminal_velocity=3, sprite=0)  # Start moving to the right
        self.direction = direction
        if self.direction == 1:
            self.x = 6 * td
        else:
            self.x = pyxel.width - 6*td - abs(self.w)
        self.is_alive = True
        self.dy = 0
        self.is_backwards = False
        self.backwards_timer = 0
        self.time_backwards = 500
        self.is_jumping = False
        self.running_sprites = [0, 16, 32]
        self.frame_count = 0
        self.is_angry = False
        # Move every 0.1 seconds (60 frames per second)
        self.move_interval = 3
        self.is_moving = True

    def fall(self):
        '''Pushes down mario if he is in the air quicker each time until it reaches a terminal velocity.'''
        self.dy += 2
        self.dy = min(self.dy, self.terminal_velocity)

    def calculate_movement(self):
        self.dy = min(self.dy + 1, 3)
        self.dx = self.direction
        self.frame_count += 1  # Counts the frames for the animation to be fluid
        # Check if the enemy has moved off-screen to the right
        if self.is_falling:
            self.fall()

    def reverse(self):
        self.dx *= -1
        self.direction *= -1  # Flip direction

    def check_enemy_collision(self, enemies):
        for other in enemies:
            if self != other and self.check_collision(other):
                return (True, other)
        return (False, None)

    def jump(self):
        self.dy = -5
        self.is_jumping = False

    def turn_backwards(self):
        if self.is_jumping and self.backwards_timer == 1:
            self.jump()
        elif self.backwards_timer < self.time_backwards:
            self.dx = 0
        else:
            self.is_backwards = False
            self.backwards_timer = 0
            self.is_angry = True

    def update(self):
        if not self.is_backwards:
            if self.frame_count % self.move_interval == 0:
                self.x += self.dx  # Update the x position based on the direction
        else:
            self.turn_backwards()
            if self.is_falling:
                self.dy -= 1
        if self.is_angry:
            self.move_interval = 2

        self.y += self.dy

        if self.y + self.h >= pyxel.height - 2*td - 1:
            if self.x + abs(self.w) > pyxel.width - 4 * td:
                self.x = 6 * td
                self.y = 4 * td
            elif self.x < 4 * td:
                self.x = pyxel.width - (6 * td) - abs(self.w)
                self.y = 4 * td
        if self.x <= 0:
            self.x = pyxel.width - abs(self.w)
        elif self.x + abs(self.w) > pyxel.width:
            self.x = 1

    def choose_animation(self):
        frame_duration = 0.1
        frame_index = int((self.frame_count / 60) /
                          frame_duration) % len(self.running_sprites)

        if self.direction > 0:  # Moving right
            self.w = -abs(self.w)  # Ensure width is negative
        else:  # Moving left
            self.w = abs(self.w)  # Flip the sprite horizontally

        if not self.is_backwards:
            self.u = self.running_sprites[frame_index]
        elif self.backwards_timer > 1 and self.backwards_timer < 30:
            self.u = 80
        elif self.backwards_timer >= 30:
            if frame_index % 2 == 0:
                self.u = 96
            else:
                self.u = 112
        if not self.is_angry:
            self.v = 24
        elif self.is_angry:
            self.v = 128

    def draw(self):
        # Use class attributes to determine the position and appearance
        self.choose_animation()
        pyxel.blt(self.x, self.y, self.sprite, self.u,
                  self.v, self.w, self.h, colkey=0)
