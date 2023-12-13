import pyxel
from character import Character


td = 8


class Coin(Character):
    def __init__(self, x, y, direction=1):
        super().__init__(x=0, y=4*td, u=0, v=24, w=8, h=16,
                         terminal_velocity=3, sprite=0)
        self.moving_sprites = (
            (0, 208), (8, 208), (16, 208), (24, 208), (32, 208), )
        self.catch_sprites = ((40, 208), (48, 208), (40, 216))
        self.adding_money_sprites = (56, 208)
        self.dollar_sprite = (72, 208)
        self.dx = 0
        self.dy = 0
        self.phase3 = False
        self.frame_count = 0
        self.catched_count = 0
        self.catched = False
        self.direction = direction
        if self.direction == 1:
            self.x = 6 * td
        elif direction == -1:
            self.x = pyxel.width - 6*td - abs(self.w)
        else:
            self.x = x

        self.y = y

        self.is_alive = True

        self.move_interval = 2

        self.dy = 0

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        if type(direction) is not int:
            raise TypeError("Direction must be an integer")
        if direction not in (1, 0, -1):
            raise ValueError("Direction must be 1, -1 or 0")
        self._direction = direction

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

    def update(self):
        if not self.catched:
            self.calculate_movement()
            if self.frame_count % self.move_interval == 0:
                self.x += self.dx  # Update the x position based on the direction
        else:
            self.catched_count += 1

        if self.phase3 == False:
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
        """Function to vary the animation of the coin"""
        frame_duration = 0.1
        u = 0
        x = 0
        y = 0
        v = 24
        w = 8
        h = 16

        if self.catched_count == 0:
            frame_index = int((self.frame_count / 90) /
                              frame_duration) % len(self.moving_sprites)
            u, v = self.moving_sprites[frame_index]
        elif self.catched_count < 10:
            u, v = self.catch_sprites[0]
            w, h = 8, 8
            y = 2
            x = 0
        elif self.catched_count < 20:
            u, v = self.catch_sprites[1]
            w, h = 8, 8
            y = 4
            x = 0
        elif self.catched_count < 30:
            u, v = self.catch_sprites[2]
            w, h = 8, 8
            y = 6
            x = 0
        elif self.catched_count < 55:
            u, v = self.adding_money_sprites
            w, h = 16, 16
            y = 10
            x = 4
        elif self.catched_count < 85:
            u, v = self.dollar_sprite
            w, h = 8, 16
            y = 14
            x = 1
        else:
            x = 500

        return x, y, u, v, w, h

    def draw(self):
        x, y, u, v, w, h = self.choose_animation()
        pyxel.blt(self.x - x, self.y - y, self.sprite, u,
                  v, w, h, colkey=0)
