import pyxel
import random
import time
from mario import Mario
from coin import Coin
from shellcreeper import Shellcreeper
from enemy2 import Enemy2
from enemy3 import Enemy3
from pipe import Pipe
from platforms import Platform
from pow import Pow


td = 8  # tile dimension


class Board:
    def __init__(self):
        self.phase = 1
        self.angry_timer = 0
        self.number_of_enemies = 0
        self.collision_list = []
        self.create_platforms()
        self.create_pipes()
        self.phase_1()
        self.mario = Mario()

    def phase0(self):
        pass

    @staticmethod
    def create_platforms():
        global platforms
        platforms = [
            Pow(),
            Platform(0, pyxel.height-2*td, 0, 33*td, td * 2),
            Platform(0, pyxel.height-20*td, 1, 14*td, td),
            Platform(pyxel.width-14*td,
                     pyxel.height-20*td, 1, 14*td, td),
            Platform(0, pyxel.height-13*td, 1, 4*td, td),
            Platform(pyxel.width-4*td, pyxel.height-13*td, 1, 4*td, td),
            Platform(pyxel.width//2-8*td,
                     pyxel.height-14*td, 1, 16*td, td),
            Platform(0, pyxel.height-8*td, 1, 10*td, td),
            Platform(pyxel.width-10*td, pyxel.height-8*td, 1, 10*td, td)
        ]

    @staticmethod
    def create_pipes():
        global pipes
        pipes = [Pipe("top", "right"),
                 Pipe("top", "left"),
                 Pipe("bottom", "right"),
                 Pipe("bottom", "left")]

    def phase_1(self):
        self.number_of_enemies = 3
        self.enemies = []
        self.shellcreepers = []
        self.shellcreeper_spawn_delay = 60
        self.shellcreepers_spawned = 0
        self.max_shellcreepers = 3
        self.coins = []
        self.coin_spawn_delay = 1000
        self.coins_spawned = 0
        self.max_coins = 2

    def spawn_shellcreepers(self):
        if self.phase == 1:
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
                self.shellcreeper_spawn_delay = 240  # Reset counter

    def spawn_coins(self):
        if self.phase == 1:
            self.coin_spawn_delay -= 1
            if self.coin_spawn_delay <= 0:
                # Spawn enemy
                if len(self.coins) < self.max_coins and self.coins_spawned < self.max_coins:  # Check max
                    coin_direction = random.choice([-1, 1])
                    new_coin = Coin(
                        direction=coin_direction)  # Create new instance
                    self.coins.append(new_coin)  # Add to list
                    self.coins_spawned += 1
                    self.enemies.append(new_coin)
                self.coin_spawn_delay = 600  # Reset counter

    def is_in_collision_list(self, enemy1, enemy2, c_list):
        if ((id(enemy1), id(enemy2)) in c_list) or ((id(enemy2), id(enemy1)) in c_list):
            return True
        else:
            return False

    def check_enemies(self, enemy_n):
        enemy1 = self.enemies[enemy_n]
        for enemy2 in self.enemies[enemy_n + 1:]:
            if enemy1.check_collision(enemy2):
                self.collision_list.append((id(enemy1), id(enemy2)))
                if not self.is_in_collision_list(enemy1, enemy2, self.last_collision_list):
                    if isinstance(enemy1, Coin):
                        enemy1.reverse()
                    elif isinstance(enemy2, Coin):
                        enemy2.reverse()
                    else:  # not enemy2.is_backwards:
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
            if not isinstance(enemy, Coin):
                if self.mario.check_collision(enemy) and not enemy.is_backwards:
                    self.mario.is_dead = True
                elif self.mario.check_collision(enemy):
                    self.enemies.remove(enemy)

    def check_if_mario_catches_coin(self):
        for enemy in self.enemies:
            if isinstance(enemy, Coin):
                if self.mario.check_collision(enemy):
                    enemy.catched = True

    def calculate_enemy_movements(self):
        i = len(self.enemies) - 1

        while i >= 0:
            if self.enemies[i].is_alive:
                self.enemies[i].calculate_movement()
            else:
                self.enemies.pop(i)
            i -= 1

    def check_if_mario_hits_platform_with_enemy(self):
        if not self.mario.is_invincible:
            if self.mario.dy < 0:  # mario is going up
                mario_sprite_top = self.mario.y + self.mario.dy
                mario_left = self.mario.x + self.mario.dx
                mario_right = self.mario.x + self.mario.dx + abs(self.mario.w)
                for enemy in self.enemies:
                    enemy_left = enemy.x + enemy.dx
                    enemy_right = enemy.x + enemy.dx + abs(enemy.w)
                    enemy_bottom = enemy.y + enemy.dy + enemy.h
                    x_overlap = (mario_left < enemy_left and mario_right > enemy_left) or (
                        mario_left < enemy_right and mario_right > enemy_right) or (
                        mario_left >= enemy_left and mario_right <= enemy_right)

                    for platform in platforms:
                        if enemy.on_platform(platform):
                            if mario_sprite_top - enemy_bottom < 11 and mario_sprite_top > enemy_bottom:
                                if x_overlap:
                                    enemy.is_backwards = True

    def check_if_mario_hits_pow(self):
        if any(isinstance(x, Pow) for x in platforms):
            mario_left = self.mario.x + self.mario.dx
            mario_right = self.mario.x + self.mario.dx + self.mario.w
            mario_top = self.mario.y
            pow_left = platforms[0].x
            pow_right = platforms[0].x + platforms[0].w
            pow_bottom = platforms[0].y + platforms[0].h

            x_overlap = (mario_left < pow_left and mario_right > pow_left) or (
                mario_left < pow_right and mario_right > pow_right) or (
                mario_left >= pow_left and mario_right <= pow_right)
            y_overlap = mario_top - pow_bottom < 2 and mario_top > pow_bottom

            if x_overlap and y_overlap:
                for enemy in self.enemies:
                    enemy.is_backwards = True
                platforms[0].phase += 1
                if platforms[0].phase >= 5:
                    del platforms[0]

    def turn_enemies_backwards(self):
        for enemy in self.enemies:
            if not isinstance(enemy, Coin):
                if enemy.is_backwards:
                    enemy.is_jumping = True
                    enemy.backwards_timer += 1

    def check_collision_between_enemies(self):
        self.last_collision_list = self.collision_list[:]
        self.collision_list = []
        if len(self.enemies) > 1:
            for i in range(len(self.enemies)):
                self.check_enemies(i)

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update()
            if enemy.catched_count >= 75:
                self.enemies.remove(enemy)

    def make_enemies_angry(self):
        for enemy in self.enemies:
            if not isinstance(enemy, Coin) and self.angry_timer >= 10*60:
                enemy.is_angry = True

    def check_if_mario_wins_phase(self):
        if self.number_of_enemies == 0:
            for enemy in self.enemies:
                if not isinstance(enemy, Coin):
                    return False
            return True
        else:
            return False

    def phase1(self):
        self.spawn_shellcreepers()

        self.spawn_coins()

        self.mario.calculate_movement()

        self.calculate_enemy_movements()

        if not self.mario.is_dead:
            self.push_back_mario_with_platforms()

        self.push_back_enemies_with_platforms()

        if self.mario.is_invincible:
            self.mario.invincible_time += 1
            if self.mario.invincible_time > 180:
                self.mario.is_invincible = False
        elif not self.mario.is_dead:
            self.check_if_mario_dies()
            self.check_if_mario_catches_coin()
        else:
            self.mario.dying_frame_count += 1

        self.check_if_mario_hits_platform_with_enemy()

        self.check_if_mario_hits_pow()

        self.turn_enemies_backwards()

        self.check_collision_between_enemies()

        if self.angry_timer > 30*60:  # seconds if they are angry
            self.make_enemies_angry()
        else:
            self.angry_timer += 1

        self.update_enemies()

        self.mario.update()

        if not self.mario.is_dead:
            self.mario.check_falling(platforms)
        elif self.mario.y > pyxel.height * 2 and self.mario.lifes > 0:
            self.mario.lifes -= 1
            if self.mario.lifes > 0:
                self.mario.respawn()
            else:
                self.end_game()

        print(self.number_of_enemies)

        if self.check_if_mario_wins_phase():
            print("wins")
            self.phase += 1

    def end_game(self):
        pyxel.quit()

    def update(self):
        if self.phase == 0:
            self.phase0()
        elif self.phase == 1:
            self.phase1()

    def draw(self):
        if self.phase == 1:
            for platform in platforms:
                platform.draw()
            for pipe in pipes:
                pipe.draw()
            for enemy in self.enemies:
                enemy.draw()
            self.mario.draw()
