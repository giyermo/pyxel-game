import pyxel
import random
from mario import Mario
from coin import Coin
from shellcreeper import Shellcreeper
from sidestepper import Sidestepper
from fighterFly import FighterFly
from pipe import Pipe
from platforms import Platform
from pow import Pow


td = 8  # tile dimension


class Board:
    def __init__(self):
        self.phase = 0
        self.phase_frame_counter = 0
        self.angry_timer = 0
        self.collision_list = []
        self.create_platforms()
        self.create_pipes()
        self.phase_6()
        self.phase_5()
        self.phase_4()
        self.phase_3()
        self.phase_2()
        self.phase_1()
        self.mario = Mario()
        self.score = 0
        self.catched = 0

    def phase0(self):
        message = "PRESS ENTER TO START"
        message_x = (pyxel.width - len(message) * pyxel.FONT_WIDTH) // 2
        message_y = pyxel.height // 2 - pyxel.FONT_HEIGHT // 2
        pyxel.text(message_x, message_y, message, pyxel.COLOR_WHITE)

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
        self.shellcreepers_spawned = 0
        self.max_shellcreepers = 3
        self.coins = []
        self.coins_spawned = 0
        self.max_coins = 2

    def phase_2(self):
        self.number_of_enemies = 5
        self.enemies = []
        self.shellcreepers = []
        self.shellcreepers_spawned = 0
        self.max_shellcreepers = 5
        self.coins = []
        self.coins_spawned = 0
        self.max_coins = 3

    def phase_3(self):
        self.seconds_left = 0
        self.phase3_duration = 20 * 60  # 20 seconds
        self.number_of_enemies = 10
        self.enemies = []
        self.coins = []
        self.coins_spawned = 0
        self.max_coins = 10

    def phase_4(self):
        self.number_of_enemies = 6
        self.enemies = []
        self.sidesteppers = []
        self.sidesteppers_spawned = 0
        self.max_sidesteppers = 6
        self.coins = []
        self.coins_spawned = 0
        self.max_coins = 3

    def phase_5(self):
        self.number_of_enemies = 9
        self.enemies = []
        self.shellcreepers = []
        self.shellcreepers_spawned = 0
        self.max_shellcreepers = 3
        self.sidesteppers = []
        self.sidesteppers_spawned = 0
        self.max_sidesteppers = 6
        self.coins = []
        self.coins_spawned = 0
        self.max_coins = 3

    def phase_6(self):
        self.number_of_enemies = 4
        self.enemies = []
        self.fighterFlys = []
        self.fighterFlys_spawned = 0
        self.max_fighterFlys = 4
        self.coins = []
        self.coins_spawned = 0
        self.max_coins = 3

    def spawn_shellcreeper(self):
        # Spawn enemy
        if len(self.shellcreepers) < self.max_shellcreepers and self.shellcreepers_spawned < self.max_shellcreepers:  # Check max
            shellcreeper_direction = random.choice([-1, 1])
            new_shellcreeper = Shellcreeper(
                direction=shellcreeper_direction)  # Create new instance
            self.shellcreepers.append(new_shellcreeper)  # Add to list
            self.shellcreepers_spawned += 1
            self.enemies.append(new_shellcreeper)

    def spawn_sidestepper(self):
        # Spawn enemy
        if len(self.sidesteppers) < self.max_sidesteppers and self.sidesteppers_spawned < self.max_sidesteppers:  # Check max
            sidestepper_direction = random.choice([-1, 1])
            new_sidestepper = Sidestepper(
                direction=sidestepper_direction)  # Create new instance
            self.sidesteppers.append(new_sidestepper)  # Add to list
            self.sidesteppers_spawned += 1
            self.enemies.append(new_sidestepper)

    def spawn_fighterFly(self):
        # Spawn enemy
        if len(self.fighterFlys) < self.max_fighterFlys and self.fighterFlys_spawned < self.max_fighterFlys:  # Check max
            fighterFly_direction = random.choice([-1, 1])
            new_fighterFly = FighterFly(
                direction=fighterFly_direction)  # Create new instance
            self.fighterFlys.append(new_fighterFly)  # Add to list
            self.fighterFlys_spawned += 1
            self.enemies.append(new_fighterFly)

    def spawn_coin(self, x=6 * td, y=4 * td):
        if not self.phase == 3:
            # Spawn coin
            if len(self.coins) < self.max_coins and self.coins_spawned < self.max_coins:  # Check max
                coin_direction = random.choice([-1, 1])
                new_coin = Coin(
                    direction=coin_direction, x=x, y=y)  # Create new instance
                self.coins.append(new_coin)  # Add to list
                self.coins_spawned += 1
                self.enemies.append(new_coin)

        else:
            new_coin = Coin(
                direction=0, x=x, y=y)  # Create new instance
            self.coins_spawned += 1
            self.enemies.append(new_coin)

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
                    self.number_of_enemies -= 1
                    self.score += 800
                    self.enemies.remove(enemy)

    def check_if_mario_catches_coin(self):
        for enemy in self.enemies:
            if isinstance(enemy, Coin):
                if self.mario.check_collision(enemy):
                    if not enemy.catched:
                        self.score += 800
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
                                    if not isinstance(enemy, Sidestepper):
                                        enemy.is_backwards = True
                                    else:
                                        enemy.hitted += 1
                                        if enemy.hitted == 1:
                                            enemy.is_angry = True
                                        elif enemy.hitted >= 2:
                                            enemy.is_backwards = True
                                            enemy.hitted = 0

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
            if isinstance(enemy, FighterFly):
                for platform in platforms:
                    if enemy.on_platform(platform):
                        enemy.is_on_platform = True
                    else:
                        enemy.is_on_platform = False
            if enemy.is_alive:
                enemy.update()
            else:
                enemy.catched_count += 1

                print("Enemy caught")
            if enemy.catched_count >= 75:
                self.enemies.remove(enemy)

    def make_enemies_very_angry(self):
        for enemy in self.enemies:
            if not isinstance(enemy, Coin):
                enemy.very_angry = True

    def check_if_mario_wins_phase(self):
        if self.phase == 3:
            if len(self.enemies) == 0:
                return True
        elif self.number_of_enemies == 0:
            for enemy in self.enemies:
                if not isinstance(enemy, Coin):
                    return False
            return True
        else:
            return False

    def interface(self):

        for i in range(self.mario.lifes):
            x = 239 - i * 15
            score = str(self.score)
            pyxel.blt(x, 5, 0, 0, 0, 16, 12)

        score = str(int(self.score))
        score_x = 5
        pyxel.text(score_x, 5, "SCORE:", pyxel.COLOR_LIGHT_BLUE)
        pyxel.text(score_x + 25, 5,   score, pyxel.COLOR_WHITE)
        pyxel.text(
            14*td+2, 5, f"PHASE {str(self.phase)}", pyxel.COLOR_LIGHT_BLUE)

    def phase1(self):
        if self.phase_frame_counter == 4*60:
            self.spawn_shellcreeper()
        elif self.phase_frame_counter == 8*60:
            self.spawn_shellcreeper()
        elif self.phase_frame_counter == 14*60:
            self.spawn_shellcreeper()

        if self.phase_frame_counter == 14*60:
            self.spawn_coin()
        elif self.phase_frame_counter == 23*60:
            self.spawn_coin()

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

        if self.number_of_enemies == 1:  # seconds if they are angry
            self.make_enemies_very_angry()

        self.update_enemies()

        self.mario.update()

        if not self.mario.is_dead:
            self.mario.check_falling(platforms)
        elif self.mario.y > pyxel.height * 2 and self.mario.lifes > 0:
            self.mario.lifes -= 1
            if self.mario.lifes > 0:
                self.mario.respawn()
            else:
                pyxel.quit()

        if self.check_if_mario_wins_phase():
            self.phase_2()
            self.phase += 1
            self.phase_frame_counter = 0

    def phase2(self):
        if self.phase_frame_counter == 1*60:
            self.spawn_shellcreeper()
        elif self.phase_frame_counter == 4*60:
            self.spawn_shellcreeper()
        elif self.phase_frame_counter == 9*60:
            self.spawn_shellcreeper()
        elif self.phase_frame_counter == 14*60:
            self.spawn_shellcreeper()
        elif self.phase_frame_counter == 20*60:
            self.spawn_shellcreeper()

        if self.phase_frame_counter == 14*60:
            self.spawn_coin()
        elif self.phase_frame_counter == 15*60:
            self.spawn_coin()
        elif self.phase_frame_counter == 16*60:
            self.spawn_coin()
        elif self.phase_frame_counter == 31*60:
            self.spawn_coin()

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

        if self.number_of_enemies == 1:  # seconds if they are angry
            self.make_enemies_very_angry()

        self.update_enemies()

        self.mario.update()

        if not self.mario.is_dead:
            self.mario.check_falling(platforms)
        elif self.mario.y > pyxel.height * 2 and self.mario.lifes > 0:
            self.mario.lifes -= 1
            if self.mario.lifes > 0:
                self.mario.respawn()
            else:
                pyxel.quit()

        if self.check_if_mario_wins_phase():
            self.phase_3()
            self.phase += 1
            self.phase_frame_counter = 0

    def phase3(self):
        self.seconds_left = (self.phase3_duration -
                             self.phase_frame_counter) / 60
        if self.phase_frame_counter == 1:
            self.spawn_coin(5*td, pyxel.height - 7*td)
            self.spawn_coin(pyxel.width-6*td, pyxel.height - 7*td)
            self.spawn_coin(11*td, pyxel.height - 12*td)
            self.spawn_coin(pyxel.width-12*td, pyxel.height - 12*td)
            self.spawn_coin(3*td, pyxel.height - 19*td)
            self.spawn_coin(pyxel.width-4*td, pyxel.height - 19*td)
            self.spawn_coin(6*td, pyxel.height - 19*td)
            self.spawn_coin(pyxel.width-7*td, pyxel.height - 19*td)
            self.spawn_coin(8*td, pyxel.height - 24*td)
            self.spawn_coin(pyxel.width-9*td, pyxel.height - 24*td)

        self.mario.calculate_movement()

        if not self.mario.is_dead:
            self.push_back_mario_with_platforms()

        if self.mario.is_invincible:
            self.mario.invincible_time += 1
            if self.mario.invincible_time > 180:
                self.mario.is_invincible = False
        elif not self.mario.is_dead:
            self.check_if_mario_dies()
            self.check_if_mario_catches_coin()
        else:
            self.mario.dying_frame_count += 1

        for enemy in self.enemies:
            enemy.phase3 = True

        self.update_enemies()

        self.mario.update()

        if not self.mario.is_dead:
            self.mario.check_falling(platforms)
        elif self.mario.y > pyxel.height * 2 and self.mario.lifes > 0:
            self.mario.lifes -= 1
            if self.mario.lifes > 0:
                self.mario.respawn()
            else:
                pyxel.quit()

        if self.seconds_left <= 0 or self.check_if_mario_wins_phase():
            self.phase_4()
            self.phase += 1
            self.phase_frame_counter = 0

    def phase4(self):
        if self.phase_frame_counter == 1*60:
            self.spawn_sidestepper()
        elif self.phase_frame_counter == 3*60:
            self.spawn_sidestepper()
        elif self.phase_frame_counter == 11*60:
            self.spawn_sidestepper()
        elif self.phase_frame_counter == 13*60:
            self.spawn_sidestepper()
        elif self.phase_frame_counter == 19*60:
            self.spawn_sidestepper()
        elif self.phase_frame_counter == 32*60:
            self.spawn_sidestepper()

        if self.phase_frame_counter == 11*60:
            self.spawn_coin()
        elif self.phase_frame_counter == 22*60:
            self.spawn_coin()
        elif self.phase_frame_counter == 34*60:
            self.spawn_coin()

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

        if self.number_of_enemies == 1:  # seconds if they are angry
            self.make_enemies_very_angry()

        self.update_enemies()

        self.mario.update()

        if not self.mario.is_dead:
            self.mario.check_falling(platforms)
        elif self.mario.y > pyxel.height * 2 and self.mario.lifes > 0:
            self.mario.lifes -= 1
            if self.mario.lifes > 0:
                self.mario.respawn()
            else:
                pyxel.quit()

        if self.check_if_mario_wins_phase():
            self.phase_5()
            self.phase += 1
            self.phase_frame_counter = 0

    def phase5(self):
        if self.phase_frame_counter == 11*60:
            self.spawn_shellcreeper()
        elif self.phase_frame_counter == 12*60:
            self.spawn_shellcreeper()

        if self.phase_frame_counter == 1*60:
            self.spawn_sidestepper()
        elif self.phase_frame_counter == 3*60:
            self.spawn_sidestepper()
        elif self.phase_frame_counter == 18*60:
            self.spawn_sidestepper()
        elif self.phase_frame_counter == 27*60:
            self.spawn_sidestepper()
        elif self.phase_frame_counter == 30*60:
            self.spawn_sidestepper()
        elif self.phase_frame_counter == 34*60:
            self.spawn_sidestepper()
        elif self.phase_frame_counter == 43*60:
            self.spawn_sidestepper()

        if self.phase_frame_counter == 11*60:
            self.spawn_coin()
        elif self.phase_frame_counter == 22*60:
            self.spawn_coin()
        elif self.phase_frame_counter == 55*60:
            self.spawn_coin()
        elif self.phase_frame_counter == 56*60:
            self.spawn_coin()

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

        if self.number_of_enemies == 1:  # seconds if they are angry
            self.make_enemies_very_angry()

        self.update_enemies()

        self.mario.update()

        if not self.mario.is_dead:
            self.mario.check_falling(platforms)
        elif self.mario.y > pyxel.height * 2 and self.mario.lifes > 0:
            self.mario.lifes -= 1
            if self.mario.lifes > 0:
                self.mario.respawn()
            else:
                pyxel.quit()

        if self.check_if_mario_wins_phase():
            self.phase_6()
            self.phase += 1
            self.phase_frame_counter = 0

    def phase6(self):
        if self.phase_frame_counter == 1*60:
            self.spawn_fighterFly()
        elif self.phase_frame_counter == 3*60:
            self.spawn_fighterFly()
        elif self.phase_frame_counter == 18*60:
            self.spawn_fighterFly()
        elif self.phase_frame_counter == 27*60:
            self.spawn_fighterFly()

        if self.phase_frame_counter == 11*60:
            self.spawn_coin()
        elif self.phase_frame_counter == 22*60:
            self.spawn_coin()
        elif self.phase_frame_counter == 55*60:
            self.spawn_coin()
        elif self.phase_frame_counter == 56*60:
            self.spawn_coin()

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

        if self.number_of_enemies == 1:  # seconds if they are angry
            self.make_enemies_very_angry()

        self.update_enemies()

        self.mario.update()

        if not self.mario.is_dead:
            self.mario.check_falling(platforms)
        elif self.mario.y > pyxel.height * 2 and self.mario.lifes > 0:
            self.mario.lifes -= 1
            if self.mario.lifes > 0:
                self.mario.respawn()
            else:
                pyxel.quit()

        if self.check_if_mario_wins_phase():
            self.phase_6()
            self.phase += 1
            self.phase_frame_counter = 0

    def update(self):
        self.phase_frame_counter += 1
        if self.phase == 0:
            if pyxel.btnp(13):  # ENTER KEY
                self.phase += 1
                self.phase_frame_counter = 0
        elif self.phase == 1:
            if self.phase_frame_counter == 1:
                self.phase_1
            self.phase1()
        elif self.phase == 2:
            if self.phase_frame_counter == 1:
                self.phase_2()
            self.phase2()
        elif self.phase == 3:
            if self.phase_frame_counter == 1:
                self.phase_3()
            self.phase3()
        elif self.phase == 4:
            if self.phase_frame_counter == 1:
                self.phase_4()
            self.phase4()
        elif self.phase == 5:
            if self.phase_frame_counter == 1:
                self.phase_5()
            self.phase5()
        elif self.phase == 6:
            if self.phase_frame_counter == 1:
                self.phase_6()
            self.phase6()

    def draw(self):
        if not self.phase in (0, 7):
            self.interface()  # prints the lifes and the score
        if self.phase == 0:
            self.phase0()
        elif self.phase in (1, 2):
            for platform in platforms:
                if isinstance(platform, Platform):
                    if platform.type != 0:
                        platform.type = 1
                platform.draw()
            for pipe in pipes:
                pipe.draw()
            for enemy in self.enemies:
                enemy.draw()
            self.mario.draw()
        elif self.phase == 3:
            pyxel.text(
                15*td, 15,   "{:.1f}".format(self.seconds_left), pyxel.COLOR_WHITE)  # timer
            for platform in platforms:
                if isinstance(platform, Platform):
                    if platform.type != 0:
                        platform.type = 2
                    platform.draw()
            for pipe in pipes:
                pipe.draw()
            for enemy in self.enemies:
                enemy.draw()
            self.mario.draw()
        elif self.phase in (4, 5):
            for platform in platforms:
                if isinstance(platform, Platform):
                    if platform.type != 0:
                        platform.type = 3
                platform.draw()
            for pipe in pipes:
                pipe.draw()
            for enemy in self.enemies:
                enemy.draw()
            self.mario.draw()
        elif self.phase == 6:
            for platform in platforms:
                if isinstance(platform, Platform):
                    if platform.type != 0:
                        platform.type = 5
                platform.draw()
            for pipe in pipes:
                pipe.draw()
            for enemy in self.enemies:
                enemy.draw()
            self.mario.draw()
        else:
            message = "GAME OVER, YOU WON!"
            message_x = (pyxel.width - len(message) * pyxel.FONT_WIDTH) // 2
            message_y = pyxel.height // 2 - pyxel.FONT_HEIGHT // 2
            pyxel.text(message_x, message_y, message, pyxel.COLOR_WHITE)
