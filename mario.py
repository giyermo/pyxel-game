import pyxel
from character import Character

td = 8  # tile dimension
jump_strength = -16


class Mario(Character):
    def __init__(self) -> None:
        """
        Initialize Mario object.

        Set initial values for various attributes of Mario.
        """
        super().__init__(x=16*td-4, y=pyxel.height-6*td, u=0, v=0,
                         w=16, h=24, terminal_velocity=3, sprite=0)
        self.dx = 0
        self.dy = 0
        self.lifes = 3
        self.direction = 1
        self.is_jumping = False
        self.is_running = False
        self.is_dead = False
        self.is_invincible = False
        self.invincible_time = 0
        self.frame_count = 0
        self.dying_frame_count = 0
        self.running_sprites = [16, 32, 48]
        self.is_transitioning = False

    def calculate_movement(self):
        '''Calculate the differential of x and y according to how much Mario is going to move in each axis'''
        if self.is_dead:
            self.dx = 0
            self.dy = 0
            return
        if pyxel.btn(pyxel.KEY_LEFT):
            self.dx = -1
            self.direction = -1
            self.is_running = True
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.dx = 1
            self.direction = 1
            self.is_running = True
        else:
            self.dx = 0
            self.is_running = False
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.jump()
        if self.is_falling:
            self.fall()

    def update(self):
        '''Update values for the Mario object according to dx and dy and the current position of the character.'''
        self.frame_count += 1
        self.update_animation()
        self.x += self.dx
        if self.x <= 0:
            self.x = pyxel.width - abs(self.w)
        elif self.x + abs(self.w) > pyxel.width:
            self.x = 0
        if self.is_dead and self.dying_frame_count >= 80:
            self.dx = 0
            self.dy = 3
        self.y = self.y + self.dy

    def respawn(self):
        """Respawn Mario at the starting position with initial attributes."""
        self.x = 16*td-4
        self.y = pyxel.height - 6*td
        self.dx = 0
        self.dy = 0
        self.direction = 1
        self.is_jumping = False
        self.is_running = False
        self.is_dead = False
        self.is_invincible = True
        self.invincible_time = 0
        self.frame_count = 0
        self.dying_frame_count = 0
        self.is_transitioning = False

    def jump(self):
        '''Makes mario jump according to the jump strength.'''
        if self.is_falling:
            return
        self.dy = jump_strength
        self.is_falling = True

    def fall(self):
        '''Pushes down mario if he is in the air quicker each time until it reaches a terminal velocity.'''
        self.is_jumping = False
        self.dy += 2
        self.dy = min(self.dy, self.terminal_velocity)

    def update_animation(self):
        """Update Mario's animation based on his state."""
        # Function to create the different Mario animations, this function is put in the update function
        frame_duration = 0.1
        frame_index = int((self.frame_count / 60) /
                          frame_duration) % len(self.running_sprites)

        if self.is_jumping:
            self.u = 64  # Set the sprite coordinates for jumping
            return  # Jump animation doesn't change until the jump is complete

        if self.is_running:
            if self.direction > 0:  # Moving right
                self.u = self.running_sprites[frame_index]
                self.w = abs(self.w)  # Ensure width is positive
            elif self.direction < 0:  # Moving left
                self.u = self.running_sprites[frame_index]
                self.w = -abs(self.w)
        else:
            self.frame_count = 0

    def running_animation(self):
        """Draw Mario's running animation."""
        frame_duration = 0.1
        frame_index = int((self.frame_count / 60) /
                          frame_duration) % len(self.running_sprites)

        if self.direction > 0:  # Moving right
            pyxel.blt(self.x, self.y, self.sprite, self.running_sprites[frame_index], self.v, self.w, self.h,
                      colkey=0)
        elif self.direction < 0:  # Moving left
            # Use left-facing sprites and flip horizontally
            pyxel.blt(self.x, self.y, self.sprite, self.running_sprites[frame_index], self.v, self.w, self.h,
                      colkey=0)

    def falling_animation(self):
        """Draw Mario's falling animation."""
        pyxel.blt(self.x, self.y, self.sprite, 64,
                  self.v, self.w, self.h, colkey=0)

    def dying_animation(self, state):
        """Draw Mario's dying animation based on state."""
        if state == "surprised":
            pyxel.blt(self.x, self.y, self.sprite, 96,
                      self.v, self.w, self.h, colkey=0)
        else:
            pyxel.blt(self.x, self.y, self.sprite, 112,
                      self.v, self.w, self.h, colkey=0)

    def draw(self):
        """Draw Mario based on his state."""
        if self.is_dead:
            if self.dying_frame_count <= 60:
                self.dying_animation("surprised")
            else:
                self.dying_animation("dying")
        elif self.is_falling:
            self.falling_animation()
        elif self.is_running:
            self.running_animation()
        else:
            frame_duration = 0.1  # Time in seconds for each frame
            # Assuming 3 frames for each direction
            frame_index = int((self.frame_count / 60) % frame_duration) % 3

            # Use right-facing sprites for static
            pyxel.blt(self.x, self.y, self.sprite, frame_index *
                      8, self.v, self.w, self.h, colkey=0)

