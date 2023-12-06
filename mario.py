
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:39:31 2019

@author: Angel Garcia Olaya PLG-UC3M
@version: 1.0
Example of simple use of pyxel. It shows how to write text, how to change its
 color and how to move it
"""

import pyxel

# To use pyxel we need to define two functions, one will do all the
# calculations needed each frame, the other will paint things on the screen
# They can have any name, but the 'standard' ones are update and draw


class Mario:
    def __init__(self, character) -> None:
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.direction = 1
        self.is_falling = False

    def update(self):
        global scroll_x
        last_y = self.y
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.dx = -2
            self.direction = -1
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.dx = 2
            self.direction = 1
        self.dy = min(self.dy + 1, 3)
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.dy = -6
            pyxel.play(3, 8)
        self.x, self.y, self.dx, self.dy = push_back(
            self.x, self.y, self.dx, self.dy)
        if self.x < scroll_x:
            self.x = scroll_x
        if self.y < 0:
            self.y = 0
        self.dx = int(self.dx * 0.8)
        self.is_falling = self.y > last_y

        if self.x > scroll_x + SCROLL_BORDER_X:
            last_scroll_x = scroll_x
            scroll_x = min(self.x - SCROLL_BORDER_X, 240 * 8)
            spawn_enemy(last_scroll_x + 128, scroll_x + 127)
        if self.y >= pyxel.height:
            game_over()

    def draw(self):
        u = (2 if self.is_falling else pyxel.frame_count // 3 % 2) * 8
        w = 8 if self.direction > 0 else -8
        pyxel.blt(self.x, self.y, 0, u, 16, w, 8, TRANSPARENT_COLOR)

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
