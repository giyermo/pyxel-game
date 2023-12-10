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
        self.stage = 1
        self.create_platforms()
        self.create_pipes()
        self.stage_1()
        self.mario = Mario()

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

    def stage_1(self):
        self.enemies = []
        self.shellcreepers = []
        self.shellcreeper_spawn_delay = 100
        self.shellcreepers_spawned = 0
        self.max_shellcreepers = 3

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

    def check_enemies(self, enemy_n):
        enemy1 = self.enemies[enemy_n]
        for enemy2 in self.enemies[enemy_n + 1:]:
            if enemy1.check_collision(enemy2):
                enemy1.reverse()
                enemy2.reverse()

    def push_back_mario_with_platforms(self):
        for platform in platforms:
            self.mario.push_back(platform)

    def push_back_enemies_with_platforms(self):
        for platform in platforms:
            for enemy in self.enemies:
                enemy.push_back(platform)

    def check_if_mario_dies(self):
        for enemy in self.enemies:
            if self.mario.check_collision(enemy):
                self.mario.die()

    def calculate_enemy_movements(self):
        i = len(self.enemies) - 1

        while i >= 0:
            if self.enemies[i].is_alive:
                self.enemies[i].calculate_movement()
            else:
                self.enemies.pop(i)
            i -= 1

    def check_collision_between_enemies(self):
        if len(self.enemies) > 1:
            for i in range(len(self.enemies)):
                self.check_enemies(i)

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update()

    def update(self):
        if self.stage == 1:
            self.spawn_shellcreepers()

            self.mario.calculate_movement()

            self.calculate_enemy_movements()

            if not self.mario.is_dead:
                self.push_back_mario_with_platforms()

            self.push_back_enemies_with_platforms()

            self.check_if_mario_dies()

            self.check_collision_between_enemies()

            self.update_enemies()

            self.mario.update()

            if not self.mario.is_dead:
                self.mario.check_falling(platforms)
            elif self.mario.y > pyxel.height * 2 and self.mario.lifes > 0:
                self.mario.lifes -= 1
                self.mario.respawn()

    def draw(self):
        for platform in platforms:
            platform.draw()
        for pipe in pipes:
            pipe.draw()
        for enemy in self.enemies:
            enemy.draw()
        self.mario.draw()
