import pyxel


from character import Character
"""from platform import Platforms"""

td = 8  # tile dimension
ground = 39 # floor coordinate
gravity = 0.5# gravity applied to mario
jump = -11 # variacion de y al saltar , falta sumarle la gravedad por eso es 11
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
        self.position = (self.x ,self.y )

    def on_ground(self):
        return self.y + 24 >= ground


    def collides_with_platform(self, platforms):
        for platform in platforms.Platform.platform:
            if self.collides_with_platform(platform):
                return True
        return False


    def update(self):


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
        if pyxel.btnp(pyxel.KEY_SPACE) and not self.is_jumping and self.on_ground():
            self.jump()

        if self.is_jumping and not pyxel.btnp(pyxel.KEY_SPACE) and self.on_ground():
            self.dy += gravity/ 2 # Para que caiga mas lento
        else:
            self.dy += gravity

        self.dy += gravity
        self.y += int(self.dy)

        if self.is_jumping and self.is_falling != True:
            self.dy += 1
            if self.dy > 0:
                self.is_jumping = False
                self.is_falling = True
        elif self.is_falling:
            self.dy += 1
            if self.y + self.h >= ground:
                self.is_falling = False
                self.dy = 0

            else:
                self.dy = 0

        self.x += self.dx
        self.y += int(self.dy) #convert it to int for the setters and for it to work

        if self.x + self.w > pyxel.width:
            self.x = 0
        elif self.x <= 0:
            self.x = pyxel.width - self.w
        if self.y + self.h > pyxel.height-16:
            self.y = pyxel.height - self.h - 16
    def jump(self):
        if not self.is_jumping:
            self.dy = jump
            self.is_jumping = True











    def draw(self):
        # u = (2 if self.is_falling else pyxel.frame_count // 3 % 2) * 8
        # w = 8 if self.direction > 0 else -8
        pyxel.blt(self.x, self.y, self.sprite,
                  self.u, self.v, 16, 24, colkey=0)
        # if self.is_invincible:
        #    pyxel.blt(self.x, self.y, 0, u, 16, w, 8, pyxel.COLOR_RED)

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
# pyxel.run(update, draw)
