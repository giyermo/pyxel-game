import pyxel
from character import Character


td = 8  # tile dimension
jump_strength = -16
terminal_velocity = 5


class Mario(Character):
    def __init__(self) -> None:
        super().__init__(x=120, y=184, u=0, v=0, w=16, h=24, sprite=0)
        self.dx = 0
        self.dy = 0
        self.direction = 1
        self.is_jumping = False
        self.is_running = False
        self.is_dead = False
        self.is_invincible = False
        self.invincible_time = 0
        self.frame_count = 0
        self.running_sprites = [16, 32, 48]
        self.is_transitioning = False

    def calculate_movement(self):
        '''Calculate the differential of x and y according to how much Mario is going to move in each axis'''
        if self.is_dead:
            return
        if pyxel.btn(pyxel.KEY_LEFT):
            self.dx = -2
            self.direction = -1
            self.is_running = True
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.dx = 2
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
        print("Update:", self.is_falling, self.x, self.y, self.dx, self.dy)
        self.x += self.dx
        if self.x <= 0:
            self.x = pyxel.width - self.w
        elif self.x + self.w > pyxel.width:
            self.x = 0
        self.y = min(self.y + self.dy, pyxel.height - 2*td - self.h)

    def jump(self):
        '''Makes mario jump according to the jump strength.'''
        if self.is_jumping or self.is_falling:
            return
        self.dy = jump_strength
        self.is_falling = True

    def fall(self):
        '''Pushes down mario if he is in the air quicker each time until it reaches a terminal velocity.'''
        self.is_jumping = False
        self.dy += 2
        self.dy = min(self.dy, terminal_velocity)

    def update_animation(self):
        # Function to create the different mario animations , this function is put in the update function
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
            # Reset animation frame count for non-running states
            self.frame_count = 0

    def draw(self):

        if self.is_jumping:
            pyxel.blt(self.x, self.y, self.sprite, self.u,
                      self.v, self.w, self.h, colkey=0)
        elif self.is_running or (self.is_falling and not self.is_running):
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
        else:
            frame_duration = 0.1  # Time in seconds for each frame
            # Assuming 3 frames for each direction
            frame_index = int((self.frame_count / 60) % frame_duration) % 3

            # Use right-facing sprites for static
            pyxel.blt(self.x, self.y, self.sprite, frame_index *
                      8, self.v, self.w, self.h, colkey=0)

        """ def draw(self):

        # a lo mejor hacer otra condicion para mientras cae que no corra y se quede mirando al lado que toque la flecha

        if self.is_running:
            pyxel.blt(self.x, self.y, self.sprite, self.u, self.v, self.w, self.h, colkey=0)
        if self.is_falling and self.is_running:

            if self.direction > 0:
                pyxel.blt(self.x, self.y, self.sprite, self.u, self.v, self.w, self.h, colkey=0) # poner sprite mirando a la derecha sin correr
            else:
                pyxel.blt(self.x, self.y, self.sprite, self.u, self.v, self.w, self.h, colkey=0) # poner sprite mirando a la izquierda sin correr

        else:
            frame_duration = 0.1  # Time in seconds for each frame
            frame_index = int(
                (self.frame_count / 60) % frame_duration) % 3  # Assuming 3 frames for each direction


            if self.is_jumping:
                self.u = 64  # Set the sprite coordinates for jumping
                pyxel.blt(self.x, self.y, self.sprite, self.u, self.v, self.w, self.h, colkey=0)
            elif self.is_falling:
                self.u = 32  # Set the sprite coordinates for falling
                pyxel.blt(self.x, self.y, self.sprite, self.u, self.v, self.w, self.h, colkey=0)

         pyxel.blt(self.x, self.y, self.sprite, self.u, self.v, self.w, self.h, colkey=0)"""

        # Set sprite coordinates based on direction and animation state
        # if self.is_running:

        #     if self.direction > 0:  # Moving right
        #         self.u = frame_index * 8 + 16
        #     elif self.direction < 0:  # Moving left
        #         self.u = frame_index * 8 + 16  # Use right-facing sprites and flip horizontally
        #         self.w = -self.w  # Flip the sprite horizontally

        # else:

        #     pyxel.blt(self.x, self.y, self.sprite,
        #           self.u, self.v, 16, 24, colkey=0)
        # if self.is_invincible:
        #    pyxel.blt(self.x, self.y, 0, u, 16, w, 8, pyxel.COLOR_RED)
