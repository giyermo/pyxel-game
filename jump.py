self.position = (self.x, self.y)
self.jumpstrenght = -6.5
self.player_y_v = 8

ground = 39
gravity = 0.2



# para detectar que esta en una plataforma
"""def on_platform(self):
    for platform in platforms:
        if platform['x'] <= self.x <= platform['x'] + platform['width'] and platform['y'] <= self.y <= platform['y'] + \
                platform['height']:
            return True

    return False"""

#detecta que esta en el suelo
def on_ground(self):
    return (0, 39) >= self.position <= (31, 39)


def update(self, ):
    if not self.is_jumping:

        self.player_y_v += gravity
        self.y += int(self.player_y_v)

        if self.y <= 208 or self.on_platform:
            self.is_jumping = False
    """if self.on_ground():
        self.y = ground"""
    if not self.is_jumping and pyxel.btnp(pyxel.KEY_SPACE):
        self.player_y_v = self.jumpstrenght
        self.is_jumping = True

    # Si no esta saltando aplico la gravedad y convierto la velocidad de mario en y a int para que pase los setters
    # Con el segundo if comprobaria si mario a vuelto al suelo pero como no hay nada que lo impida volvera siempre
    # tercer if confirma que ha saltado