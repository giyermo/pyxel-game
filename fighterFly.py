import pyxel
from character import Character  # Assuming the Character class is defined in character module

td = 8

class FighterFly(Character):
    def __init__(self, direction=1) -> None:
        """Initialize the FighterFly object.

        Args:
            direction (int, optional): The initial direction of movement (1 for right, -1 for left). Defaults to 1.
        """
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
        self.catched_count = 0
        self.is_angry = False
        self.very_angry = False
        self.is_on_platform = False
        # Move every 0.1 seconds (60 frames per second)
        self.move_interval = 5
        self.is_moving = True
        self.jump_timer = 0

    def calculate_movement(self):
        """Calculate the movement of the FighterFly."""
        self.dy = min(self.dy + 1, 3)
        self.dx = self.direction
        self.frame_count += 1  # Counts the frames for the animation to be fluid
        # Check if the enemy has moved off-screen to the right
        self.dy = 0   # Update the x position based on the direction

    def reverse(self):
        """Reverse the direction of the FighterFly."""
        self.dx *= 1
        self.direction *= 1  # Flip direction

    def check_enemy_collision(self, enemies):
        """Check for collisions with other enemies.
        """
        for other in enemies:
            if self != other and self.check_collision(other):
                return (True, other)
        return (False, None)

    def jump(self):
        """Make the FighterFly jump."""
        self.dy = -5
        self.is_jumping = False

    def turn_backwards(self):
        """Turn the FighterFly backwards."""
        if self.is_jumping and self.backwards_timer == 1:
            self.jump()
        elif self.backwards_timer < self.time_backwards:
            self.dx = 0
        else:
            self.is_backwards = False
            self.backwards_timer = 0
            self.is_angry = True

    def update(self):
        """Update the FighterFly's position and state."""
        if not self.is_backwards:
            if self.is_on_platform == True and self.jump_timer > 200:
                self.jump_timer = 0
            elif self.jump_timer > 100:
                if self.frame_count % self.move_interval == 0:
                    self.x += self.dx   # Update the x
                if self.frame_count % self.move_interval == 0:
                    self.dy = 1   # Update the x
            elif self.jump_timer > 60:
                if self.frame_count % self.move_interval == 0:
                    self.x += self.dx   # Update the x
                if self.frame_count % self.move_interval == 0:
                    self.dy = -1   # Update the x
        else:
            self.turn_backwards()
        if self.very_angry:
            self.jump_timer += 2
        elif self.is_angry:
            self.jump_timer += 1

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
        """Choose the animation for the FighterFly."""
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
        if self.is_angry or self.very_angry:
            self.v = 128
        else:
            self.v = 24

    def draw(self):
        """Draw the FighterFly on the screen."""
        self.jump_timer += 1
        # Use class attributes to determine the position and appearance
        self.choose_animation()
        pyxel.blt(self.x, self.y, self.sprite, self.u,
                  self.v, self.w, self.h, colkey=0)

