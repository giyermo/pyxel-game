import pyxel
import random
import time
from mario import Mario
from shellcreeper import Shellcreeper
from enemy2 import Enemy2
from enemy3 import Enemy3
from pipe import Pipe
from platforms import Platform


td = 8  # tile dimension


class Board:
    def __init__(self):
        self.shellcreeper_spawn_delay = 100
        self.shellcreepers_spawned = 0
        self.max_shellcreepers = 3
        self.stage = 1
        self.create_platforms()
        self.create_pipes()

        self.enemies = []

        self.shellcreepers = []

        global mario
        mario = Mario()
        mario.x = 10
        mario.y = 90

        global enemy2
        enemy2 = Enemy2()

        global enemy3
        enemy3 = Enemy3()

    @staticmethod
    def create_platforms():
        global platforms
        platforms = [
            Platform(0, pyxel.height-2*td, 0, 33*td),
            Platform(0, pyxel.height-20*td, 1, 14*td),
            Platform(pyxel.width-14*td,
                     pyxel.height-20*td, 1, 14*td),
            Platform(0, pyxel.height-13*td, 1, 4*td),
            Platform(pyxel.width-4*td, pyxel.height-13*td, 1, 4*td),
            Platform(pyxel.width//2-8*td,
                     pyxel.height-14*td, 1, 16*td),
            Platform(0, pyxel.height-8*td, 1, 10*td),
            Platform(pyxel.width-10*td, pyxel.height-8*td, 1, 10*td)
        ]

    @staticmethod
    def create_pipes():
        global pipes
        pipes = [Pipe("top", "right"),
                 Pipe("top", "left"),
                 Pipe("bottom", "right"),
                 Pipe("bottom", "left")]

    def spawn_shellcreepers(self):
        self.shellcreeper_spawn_delay -= 1
        if self.shellcreeper_spawn_delay <= 0:
            # Spawn enemy
            if len(self.shellcreepers) < self.max_shellcreepers and self.shellcreepers_spawned < self.max_shellcreepers:  # Check max
                shellcreeper_direction = random.choice([-1, 1])
                new_shellcreeper = Shellcreeper(
                    direction=shellcreeper_direction)  # Create new instance
                self.shellcreepers.append(new_shellcreeper)  # Add to list
                self.shellcreepers_spawned += 1
                self.enemies.append(new_shellcreeper)
            self.shellcreeper_spawn_delay = 300  # Reset counter

    def update(self):
        if self.stage == 1:
            self.spawn_shellcreepers()
            mario.calculate_movement()

            i = len(self.enemies) - 1

            while i >= 0:
                if self.enemies[i].is_alive:
                    self.enemies[i].calculate_movement()
                else:
                    self.enemies.pop(i)
                i -= 1

            enemy2.update()
            enemy3.update()

            for platform in platforms:
                mario.push_back(platform)
                for enemy in self.enemies:
                    enemy.push_back(platform)

            for enemy in self.enemies:
                collision, other_enemy = enemy.check_enemy_collision(
                    self.enemies)
                if collision:
                    enemy.reverse()
                    other_enemy.reverse()

                enemy.update()  # Move normally
            mario.update()

            mario.check_falling(platforms)

    def draw(self):
        for platform in platforms:
            platform.draw()
        for pipe in pipes:
            pipe.draw()
        for enemy in self.enemies:
            enemy.draw()
        mario.draw()
        enemy2.draw()
        enemy3.draw()
