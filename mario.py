import pyxel
from character import Character


td = 8  # tile dimension


class Mario(Character):
    def __init__(self) -> None:
        super().__init__(x=120, y=168, u=0, v=0, w=16, h=24, sprite=0)
        self.dx = 0
        self.dy = 0
        self.direction = 1
        self.is_falling = False
        self.is_jumping = False
        self.is_running = False
        self.is_dead = False
        self.is_invincible = False
        self.invincible_time = 0
        self.frame_count = 0
        self.running_sprites = [16, 32, 48]
        self.is_transitioning = False

    def update(self):


        self.frame_count += 1 # Counts the frames for the animation to be fluid
        self.update_animation()
        if self.is_dead:
            return
        if pyxel.btn(pyxel.KEY_LEFT):
            self.dx = -2
            self.direction = -1
            self.is_running = True
            self.is_transitioning = True
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.dx = 2
            self.direction = 1
            self.is_running = True
            self.is_transitioning = True
        else:
            self.dx = 0
            self.is_running = False
            self.is_transitioning = False
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.jump()
        if self.is_jumping and self.is_falling != True:
            self.dy += 1
            if self.dy > 0:
                self.is_jumping = False
                self.dy = 0
                self.is_falling = True
        elif self.is_falling:
            self.dy += 1
            if self.dy > 3:
                self.dy = 3
                self.is_falling = False
        else:
            self.dy = 0
        self.x += self.dx
        self.y += self.dy
        if self.x + self.w > pyxel.width:
            self.x = 0
        elif self.x <= 0:
            self.x = pyxel.width - self.w
        if self.y + self.h > pyxel.height-16:
            self.y = pyxel.height - self.h - 16

    def jump(self):
        # Configures the jump of mario and confirms that is jumping
        if self.is_jumping:
            return
        self.dy = -10
        self.is_jumping = True

    def update_animation(self):
        #Function to create the different mario animations , this function is put in the update function
        frame_duration = 0.1
        frame_index = int((self.frame_count / 60) / frame_duration) % len(self.running_sprites)

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
            pyxel.blt(self.x, self.y, self.sprite, self.u, self.v, self.w, self.h, colkey=0)
        elif self.is_running or (self.is_falling and not self.is_running):
            frame_duration = 0.1
            frame_index = int((self.frame_count / 60) / frame_duration) % len(self.running_sprites)

            if self.direction > 0:  # Moving right
                pyxel.blt(self.x, self.y, self.sprite, self.running_sprites[frame_index], self.v, self.w, self.h,
                          colkey=0)
            elif self.direction < 0:  # Moving left
                # Use left-facing sprites and flip horizontally
                pyxel.blt(self.x, self.y, self.sprite, self.running_sprites[frame_index], self.v, self.w, self.h,
                          colkey=0)
        else:
            frame_duration = 0.1  # Time in seconds for each frame
            frame_index = int((self.frame_count / 60) % frame_duration) % 3  # Assuming 3 frames for each direction

            # Use right-facing sprites for static
            pyxel.blt(self.x, self.y, self.sprite, frame_index * 8, self.v, self.w, self.h, colkey=0)



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

        #Set sprite coordinates based on direction and animation state
        """if self.is_running:

            if self.direction > 0:  # Moving right
                self.u = frame_index * 8 + 16
            elif self.direction < 0:  # Moving left
                self.u = frame_index * 8 + 16  # Use right-facing sprites and flip horizontally
                self.w = -self.w  # Flip the sprite horizontally

        else:

            pyxel.blt(self.x, self.y, self.sprite,
                  self.u, self.v, 16, 24, colkey=0)
        # if self.is_invincible:
                #    pyxel.blt(self.x, self.y, 0, u, 16, w, 8, pyxel.COLOR_RED)"""

                # def update():
                    #     ''' This function is executed every frame. Now it only checks if the
                    #     Escape key or Q are pressed to finish the program'''
                    #     if pyxel.btnp(pyxel.KEY_Q):
                    #         pyxel.quit()


                    # def draw():
                    #     ''' This function puts things on the screen every turn. Now only text '''
                    #     # We set the background color, anything on the screen is erased
                    #     # See pyxel documentation for available colors (16)
                    #     # 0 is black
                    #     pyxel.cls(0)
                    #     # with .text(x:int,y:int,text:str,color:int) we draw a text in the screen
                    #     pyxel.text(0, 0, "Hello, welcome to pyxel", 2)
                    #     # we use pyxel.frame_count to do things every frame (here changing color)
                    #     pyxel.text(0, 10, "Changing color every frame", pyxel.frame_count % 16)
                    #     # this is done every frame... moving a text until it reaches the end
                    #     # we can know the width and height of the screen using pyxel.width or
                    #     # pyxel.height
                    #     x = pyxel.frame_count % pyxel.width
                    #     pyxel.text(x, 20, "Moving text", 3)


                    # ################## main program ##################


                        # # Creating constants so it is easier to modify values
                        # # Maximum width and height are 256
                        # WIDTH = 256
                        # HEIGHT = 256
                        # CAPTION = "This is the first pyxel example"

                        # # The first thing to do is to create the screen, see API for more parameters
                        # pyxel.init(WIDTH, HEIGHT, title=CAPTION)

                             # # To start the game we invoke the run method with the update and draw functions
                        # pyxel.run(update, draw)"""

