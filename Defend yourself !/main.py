import pygame
import math
import _thread
import time
import random
import csv

# --- constants --- (UPPER_CASE_NAMES)

# - Maps -
MAPS = [
    {
        'path': (
            ((600, 300), 'start'),
            ((500, 300), 'u'),
            ((500, 200), 'u'),
            ((500, 100), 'l'),
            ((400, 100), 'l'),
            ((300, 100), 'd'),
            ((300, 200), 'd'),
            ((300, 300), 'd'),
            ((300, 400), 'd'),
            ((300, 500), 'l'),
            ((200, 500), 'l'),
            ((100, 500), 'u'),
            ((100, 400), 'u'),
            ((100, 300), 'l'),
            ((000, 300), 'end')),
        'screen': (700, 700),
        'box': 100
    },
    {
        'path': (
            ((650, 450), 'start'),
            ((600, 450), 'u'),
            ((600, 400), 'u'),
            ((600, 350), 'u'),
            ((600, 300), 'u'),
            ((600, 250), 'u'),
            ((600, 200), 'u'),
            ((600, 150), 'l'),
            ((550, 150), 'l'),
            ((500, 150), 'd'),
            ((500, 200), 'd'),
            ((500, 250), 'd'),
            ((500, 300), 'd'),
            ((500, 350), 'l'),
            ((450, 350), 'l'),
            ((400, 350), 'u'),
            ((400, 300), 'u'),
            ((400, 250), 'u'),
            ((400, 200), 'u'),
            ((400, 150), 'u'),
            ((400, 100), 'u'),
            ((400, 50), 'l'),
            ((350, 50), 'l'),
            ((300, 50), 'l'),
            ((250, 50), 'l'),
            ((200, 50), 'd'),
            ((200, 100), 'd'),
            ((200, 150), 'd'),
            ((200, 200), 'd'),
            ((200, 250), 'l'),
            ((150, 250), 'l'),
            ((100, 250), 'd'),
            ((100, 300), 'd'),
            ((100, 350), 'r'),
            ((150, 350), 'r'),
            ((200, 350), 'd'),
            ((200, 400), 'd'),
            ((200, 450), 'r'),
            ((250, 450), 'r'),
            ((300, 450), 'r'),
            ((350, 450), 'r'),
            ((400, 450), 'r'),
            ((450, 450), 'r'),
            ((500, 450), 'd'),
            ((500, 500), 'd'),
            ((500, 550), 'l'),
            ((500, 550), 'l'),
            ((450, 550), 'l'),
            ((400, 550), 'l'),
            ((350, 550), 'l'),
            ((300, 550), 'l'),
            ((250, 550), 'l'),
            ((200, 550), 'l'),
            ((150, 550), 'l'),
            ((100, 550), 'l'),
            ((50, 550), 'l'),
            ((0, 550), 'end')),
        'screen': (700, 700),
        'box': 50
    }
]

WAVES = [
    [
        ('goblin', 1),
        ('goblin', 1),
        ('goblin', 2),
        ('goblin', 1),
        ('goblin', 1),
        ('goblin', 3),
        ('goblin', 3),
        ('goblin', 0.5),
        ('goblin', 0.5),
        ('goblin', 0)
    ],
    [
        ('giant', 2),
        ('giant', 2),
        ('goblin', 0.5),
        ('goblin', 0.5),
        ('goblin', 2),
        ('giant', 2),
        ('giant', 5),
        ('goblin', 1),
        ('giant', 1),
        ('giant', 0)
    ],
    [
        ('giant', 2),
        ('witch', 1),
        ('witch', 1),
        ('witch', 1),
        ('giant', 2),
        ('witch', 1),
        ('witch', 1),
        ('goblin', 1),
        ('goblin', 1),
        ('goblin', 1),
        ('goblin', 1),
        ('goblin', 1),
        ('witch', 2),
        ('witch', 2),
        ('goblin', 0.5),
        ('goblin', 0.5),
        ('goblin', 0.5),
        ('witch', 1),
        ('witch', 0)
    ],
    [
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 2),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0),
    ],
    [
        ('giant', 2),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.5),
        ('goblin', 0.5),
        ('goblin', 0.5),
        ('goblin', 0.1),
        ('goblin', 0.5),
        ('goblin', 0.5),
        ('giant', 1),
        ('giant', 0.5),
        ('witch', 0.5),
        ('witch', 0)
    ],
    [
        ('giant', 1),
        ('giant', 1),
        ('giant', 1),
        ('giant', 1),
        ('giant', 3),
        ('griffin', 1.5),
        ('griffin', 1.5),
        ('griffin', 3),
        ('griffin', 1.5),
        ('griffin', 1.5),
        ('griffin', 0)
    ],
    [
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 0.2),
        ('goblin', 2),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0.1),
        ('goblin', 0),
    ],
    [
        ('giant', 0, True)
    ]
]

# CSV reading
things = ['towers', 'monsters']
CSV_SPECS = {}
for thing in things:
    CSV_SPECS[thing] = []
    with open(f'{thing}.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            for key, value in row.items():
                if key != 'Name':
                    row[key] = int(value)
            CSV_SPECS[thing].append(row)


# --- Menu ---
def menu(game_over_background=None):
    in_game = False
    map_choosed = False
    text = pygame.font.SysFont('arial black', 20)

    play = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
    pygame.draw.rect(play, (0, 170, 210, 170), (0, 0, SCREEN_SIZE[0], round(SCREEN_SIZE[1] / 3)))
    texted_play = text.render('PLAY', True, (255, 255, 255))

    settings = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
    pygame.draw.rect(settings, (0, 200, 0, 170), (0, 0, SCREEN_SIZE[0], round(SCREEN_SIZE[1] / 3)))
    texted_settings = text.render('SETTINGS', True, (255, 255, 255))

    stop = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
    pygame.draw.rect(stop, (0, 0, 170, 170), (0, 0, SCREEN_SIZE[0], round(SCREEN_SIZE[1] / 3)))
    texted_stop = text.render('STOP', True, (255, 255, 255))

    map1 = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
    pygame.draw.rect(map1, (0, 240, 150, 170), (0, 0, round(SCREEN_SIZE[0] / 2), SCREEN_SIZE[1]))
    texted_map1 = text.render('Small map', True, (255, 255, 255))

    map2 = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
    pygame.draw.rect(map2, (220, 20, 70, 170), (0, 0, round(SCREEN_SIZE[0] / 2), SCREEN_SIZE[1]))
    texted_map2 = text.render('Big map', True, (255, 255, 255))

    while not in_game:
        if game_over_background != None:
            screen.blit(game_over_background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if not map_choosed:
                    if mouse_pos[1] <= SCREEN_SIZE[1] / 3:
                        map_choosed = True
                    elif SCREEN_SIZE[1] / 3 < mouse_pos[1] <= SCREEN_SIZE[1] / 3 * 2:
                        print('soon...')
                    elif SCREEN_SIZE[1] / 3 * 2 < mouse_pos[1] <= SCREEN_SIZE[1]:
                        pygame.quit()
                else:
                    if mouse_pos[0] <= SCREEN_SIZE[0] / 2:
                        return 0
                    else:
                        return 1

        if not map_choosed:
            screen.blit(play, (0, 0))
            screen.blit(settings, (0, round(SCREEN_SIZE[1] / 3)))
            screen.blit(stop, (0, round(2 * SCREEN_SIZE[1] / 3)))

            screen.blit(texted_play, (round(SCREEN_SIZE[0] / 2 - texted_play.get_width() / 2),
                                      round(SCREEN_SIZE[1] / 6 - texted_play.get_height() / 2)))
            screen.blit(texted_settings, (round(SCREEN_SIZE[0] / 2 - texted_settings.get_width() / 2),
                                          round(3 * SCREEN_SIZE[1] / 6 - texted_settings.get_height() / 2)))
            screen.blit(texted_stop, (round(SCREEN_SIZE[0] / 2 - texted_stop.get_width() / 2),
                                      round(5 * SCREEN_SIZE[1] / 6 - texted_stop.get_height() / 2)))

        else:
            screen.blit(map1, (0, 0))
            screen.blit(map2, (round(SCREEN_SIZE[0] / 2), 0))

            screen.blit(texted_map1, (round(SCREEN_SIZE[0] / 4 - texted_map1.get_width() / 2),
                                      round(SCREEN_SIZE[1] / 2 - texted_map1.get_height() / 2)))
            screen.blit(texted_map2, (round(SCREEN_SIZE[0] / 4 * 3 - texted_map2.get_width() / 2),
                                      round(SCREEN_SIZE[1] / 2 - texted_map2.get_height() / 2)))

        pygame.display.flip()


# --- functions --- (lower_case_names)


# --- main --- (lower_case_names)
def main(MAP):
    global SPAWN_POS
    global SCREEN_SIZE
    global BOX_SIZE
    global BOX_SURFACE
    global SMALL_BOX_SIZE
    global SMALL_BOX_SURFACE
    global BUTTON_SIZE
    global SMALL_BUTTON_SIZE
    global player
    global speed_up
    global monsters
    global Monster
    global playing

    # --- classes ---- (CamelCaseNames)

    class Player:

        def __init__(self, start_money, max_health):
            self.alignment = 10

            # --- Health ---
            self.max_health = max_health
            self.current_health = self.max_health

            # - Health bar back -
            self.hb_back_height = 40
            self.hb_back_width = 200

            self.hb_back = pygame.Surface((self.hb_back_width, self.hb_back_height), pygame.SRCALPHA)
            self.hb_back.fill((255, 255, 255, 200))
            self.hb_back_rect = self.hb_back.get_rect()
            self.hb_back_rect.x = self.alignment
            self.hb_back_rect.y = SCREEN_SIZE[1] - self.alignment - self.hb_back_height

            # - Current health bar -
            self.hb_border = 2 * 5
            self.current_hb_height = self.hb_back_height - self.hb_border
            self.current_hb_width = self.hb_back_width - self.hb_border

            self.texted_current_health = pygame.font.SysFont('rubikbold', round(BUTTON_SIZE[0] / 4))

            self.max_life_color = (58, 181, 75, 170)
            self.intermediate_life_color = (250, 175, 58, 170)
            self.min_life_color = (192, 40, 45, 170)

            # --- Money ---
            self.money = start_money
            self.dynamic_money = self.money
            self.coin = pygame.transform.scale(pygame.image.load('assets/coin.png'),
                                               SMALL_BUTTON_SIZE)
            self.coin_rect = self.coin.get_rect()
            self.coin_rect.x, self.coin_rect.y = self.alignment, self.alignment

            # --- Tower placement ---
            self.editor_mode = False
            self.selection_mode = False

            self.in_wave = False
            self.current_wave = -1
            self.texted_wave = pygame.font.SysFont('arial black', 34)
            self.texted_m_left = pygame.font.SysFont('arial black', 20)
            self.m_left = 0

            self.game_over = False

        def update(self):
            self.update_health()
            self.update_money()
            self.show_wave()
            self.show_monsters_left()

        def update_health(self):
            if self.current_health <= 0:
                self.game_over = True
                playing = False
                pygame.mixer.music.stop()
                sounds['lose'].play()
                self.current_health = 0

            # health bar back
            screen.blit(self.hb_back, self.hb_back_rect)

            # current health
            if self.current_health == 0:
                self.current_hb_width = self.hb_back_width - self.hb_border
            else:
                self.current_hb_width = round(
                    (self.hb_back_width - self.hb_border) * (self.current_health / self.max_health))
            health_bar = pygame.Surface((self.current_hb_width, self.current_hb_height), pygame.SRCALPHA)

            if self.current_health >= self.max_health / 2:
                health_bar_color = linear_interpolation(self.max_health, self.max_health / 2, self.current_health,
                                                        self.max_life_color, self.intermediate_life_color)
            else:
                health_bar_color = linear_interpolation(self.max_health / 2, 1, self.current_health,
                                                        self.intermediate_life_color, self.min_life_color)
            health_bar.fill(health_bar_color)
            screen.blit(health_bar, (self.alignment + self.hb_border / 2,
                                     -self.alignment + self.hb_border / 2 + SCREEN_SIZE[1] - self.hb_back_height))

            # texted current health
            imaged_text_ch_shad = self.texted_current_health.render(str(self.current_health), True, (0, 0, 0))

            imaged_text_ch = self.texted_current_health.render(str(self.current_health), True, (250, 0, 0))
            imaged_text_ch_rect = imaged_text_ch.get_rect()
            imaged_text_ch_rect.x = -1 + self.hb_border / 2 + self.alignment + self.current_hb_width / 2 - \
                                    self.texted_current_health.size(str(self.current_health))[0] / 2
            imaged_text_ch_rect.y = self.hb_border / 2 - self.alignment + SCREEN_SIZE[1] - self.hb_back_height
            screen.blit(imaged_text_ch_shad, (imaged_text_ch_rect.x+2, imaged_text_ch_rect.y+1))
            screen.blit(imaged_text_ch, (imaged_text_ch_rect.x, imaged_text_ch_rect.y))

            # icon
            life_icon_border_rect.y = -life_icon_border_rect.height / 2 + self.hb_back_rect.height / 2 + self.hb_back_rect.y
            life_icon_rect.y = -life_icon_rect.height / 2 + self.hb_back_rect.height / 2 + self.hb_back_rect.y

            blit_alpha(screen, life_icon, life_icon_rect.x, life_icon_rect.y,
                       (255 * self.current_health) / self.max_health)
            screen.blit(life_icon_border, life_icon_border_rect)

        def update_money(self):
            if abs(self.money - self.dynamic_money) < 5*speed_up[2]:
                self.dynamic_money = self.money
            elif self.dynamic_money < self.money:
                self.dynamic_money += round(1 + (self.money - self.dynamic_money)/(10/(speed_up[2]/3)))
            elif self.dynamic_money > self.money:
                self.dynamic_money -= round(1 - (self.money - self.dynamic_money)/(10/(speed_up[2]/3)))

            font_size = round(23 + self.dynamic_money / 100)
            if font_size > 70:
                font_size = 70
            elif font_size < 24:
                font_size = 24

            # texted money
            texted_money = pygame.font.SysFont('impact', font_size)
            imaged_text_money = texted_money.render(str(self.dynamic_money), True, (0, 0, 0))
            imaged_text_money_rect = imaged_text_money.get_rect()
            imaged_text_money_rect.x = self.alignment + self.coin_rect.width + 5
            imaged_text_money_rect.width += 5
            imaged_text_money_rect.y = self.alignment * 2

            s = pygame.Surface((imaged_text_money_rect.width + self.coin_rect.width + 10,
                                max(imaged_text_money_rect.height, self.coin_rect.height) + 10), pygame.SRCALPHA)
            s.fill((255, 255, 0, 150))
            screen.blit(s, (self.coin_rect.x - 5,
                            min(imaged_text_money_rect.y, self.coin_rect.y) - 5))

            screen.blit(imaged_text_money, imaged_text_money_rect)

            # coin
            self.coin_rect.x = imaged_text_money_rect.x - self.coin_rect.width - 5
            self.coin_rect.y = imaged_text_money_rect.height / 2 - self.coin_rect.height / 2 + imaged_text_money_rect.y
            screen.blit(self.coin, self.coin_rect)

        def show_wave(self):

            pos_x = SCREEN_SIZE[0] - BUTTON_SIZE[0] - 75
            pos_y = SCREEN_SIZE[1] - BUTTON_SIZE[0] - 70

            # level text
            # shadow
            imaged_text_wave_shadow = self.texted_wave.render('wave : ' + str(self.current_wave + 1), True, (0, 0, 0))
            blit_alpha(screen, imaged_text_wave_shadow, pos_x + 2, pos_y + 2, 200)
            # text
            imaged_text_wave = self.texted_wave.render('wave : ' + str(self.current_wave + 1), True, (255, 100, 100))
            screen.blit(imaged_text_wave, (pos_x, pos_y))

        def show_monsters_left(self):

            pos_x = SCREEN_SIZE[0] - BUTTON_SIZE[0] - 95
            pos_y = SCREEN_SIZE[1] - BUTTON_SIZE[0] - 95

            m_left = str(self.m_left)

            # level text
            # shadow
            imaged_text_m_left_shadow = self.texted_m_left.render('monsters left : ' + m_left, True, (0, 0, 0))
            blit_alpha(screen, imaged_text_m_left_shadow, pos_x + 2, pos_y + 2, 200)
            # text
            imaged_text_m_left = self.texted_m_left.render('monsters left : ' + m_left, True, (255, 100, 100))
            screen.blit(imaged_text_m_left, (pos_x, pos_y))

    class Tower(pygame.sprite.Sprite):

        def __init__(self, name, pos):
            super().__init__()
            for tow in CSV_SPECS['towers']:
                if name == tow['Name']:
                    self.stable_specs = tow
                    self.skin_load = pygame.image.load(f'assets/towers/{name}.png')

                    size = (round(BOX_SIZE / 2), round(BOX_SIZE / 2))

#                    if name == 'normal':
#                        size = (round(BOX_SIZE / 4), round(BOX_SIZE / 4))
#                    else:
#                        size = (round(BOX_SIZE / 2), round(BOX_SIZE / 2))
                    self.skin_projectile = pygame.transform.smoothscale(
                        pygame.image.load(f'assets/projectiles/{name}.png'), size)

            # range color :
            # rapid = (170,240,170,140);
            # normal = (210,183,215,140);
            # long = (180,180,180,140);
            # fire = (255,170,100,140);
            self.range_color = (180, 180, 180, 140)
            self.t_range = self.stable_specs['Range']
            self.attack = self.stable_specs['Attack_damage']
            self.attack_speed = self.stable_specs['Attack_speed']
            self.proj_velocity = self.stable_specs['Projectile_velocity']

            a = '''

            self.skin_load = 'assets/no-image.png'

            if tower_type == 'rapid':
                self.attack = 5
                self.attack_speed = 4
                self.t_range = 1
                self.range_color = (170, 240, 170, 140)
                self.proj_velocity = 8
                self.skin_load = pygame.image.load(f'assets/towers/{tower_type}.png')
                self.skin_projectile = pygame.transform.smoothscale(
                    pygame.image.load(f'assets/projectiles/{tower_type}.png'),
                    (round(BOX_SIZE / 2), round(BOX_SIZE / 2)))
                self.skin_projectile = pygame.transform.rotate(self.skin_projectile, -225)
            elif tower_type == 'long':
                self.attack = 30
                self.attack_speed = 0.4
                self.t_range = 3
                self.range_color = (180, 180, 180, 140)
                self.proj_velocity = 5
                self.skin_load = pygame.image.load(f'assets/towers/{tower_type}.png')
                self.skin_projectile = pygame.transform.smoothscale(
                    pygame.image.load(f'assets/projectiles/{tower_type}.png'),
                    (round(BOX_SIZE / 2), round(BOX_SIZE / 2)))
            elif tower_type == 'fire':
                self.attack = 0.05
                self.attack_speed = 1
                self.t_range = 1
                self.range_color = (255, 170, 100, 140)
                self.proj_velocity = 1
                self.skin_load = pygame.image.load(f'assets/towers/{tower_type}.png')
            elif tower_type == 'normal':
                self.attack = 8
                self.attack_speed = 2
                self.t_range = 2
                self.range_color = (210, 183, 215, 140)
                self.proj_velocity = 7
                self.skin_load = pygame.image.load(f'assets/towers/{tower_type}.png')
                self.skin_projectile = pygame.transform.smoothscale(
                    pygame.image.load(f'assets/projectiles/{tower_type}.png'),
                    (round(BOX_SIZE / 4), round(BOX_SIZE / 4)))
            '''

            self.name = name
            self.pos = pos
            self.skin = pygame.transform.smoothscale(self.skin_load, BOX_SURFACE)
            self.rect = self.skin.get_rect()
            self.shoot_cooldown = 0

            self.value = tower_cost
            self.level_up_cost = round(tower_cost / 5)

            self.level = 1

            self.range_surface = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
            pygame.draw.rect(self.range_surface, self.range_color, (self.rect.x, self.rect.y,
                                                                    self.rect.width * 2 * self.t_range + BOX_SIZE,
                                                                    self.rect.height * 2 * self.t_range + BOX_SIZE))

        def shoot(self, spawn, enemy, velocity):
            projectiles.add(Projectile(spawn, enemy, self.attack, self.skin_projectile, self.name,
                                       velocity=velocity))

        def level_up(self):
            sounds['level_up'].play()
            self.level_up_cost = round(20 + self.level_up_cost * 1.5)
            self.attack *= 1.18
            self.attack += round(self.attack / 10)
            self.attack_speed *= 1.04
            self.proj_velocity *= 1.05
            self.level += 1
            if self.level%10 == 0:
                self.t_range += 1
                self.range_surface = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
                pygame.draw.rect(self.range_surface, self.range_color, (self.rect.x, self.rect.y,
                                                                        self.rect.width * 2 * self.t_range + BOX_SIZE,
                                                                        self.rect.height * 2 * self.t_range + BOX_SIZE))

        def show_level(self, box_mouse_x, box_mouse_y):

            texted_level = pygame.font.SysFont('impact', round(0.20 * BOX_SIZE))
            texted_level_cost = pygame.font.SysFont('calibri', round(0.22 * BOX_SIZE), bold=True)

            align = {'circle': {'x': round(0.05 * BOX_SIZE), 'y': round(0.13 * BOX_SIZE)},
                     'level': {'x': round(0.01 * BOX_SIZE) - 1, 'y': round(0.01 * BOX_SIZE) - 1},
                     'level_cost': {'x': round(BOX_SIZE / 2 - texted_level_cost.size(str(self.level_up_cost))[0] / 2),
                                    'y': round(BOX_SIZE / 2 - texted_level_cost.size(str(self.level_up_cost))[1] / 2)}}
            if self.level >= 10:
                align['level']['x'] -= round(0.20 * BOX_SIZE / 5)

            circle = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA, 32)
            pygame.draw.circle(circle, (250, 250, 250, 230),
                               (self.pos[0] + align['circle']['x'], self.pos[1] + align['circle']['y']),
                               round(0.15 * BOX_SIZE))
            color = (10, 70, 250, 170)
            if box_mouse_x == self.pos[0] and box_mouse_y == self.pos[1] and player.editor_mode:

                if self.level_up_cost <= player.money:
                    color = (10, 250, 100, 170)
                else:
                    color = (250, 20, 100, 170)

                # shadow
                imaged_text_level_cost_shadow = texted_level_cost.render(str(self.level_up_cost), True, (0, 0, 0))
                blit_alpha(screen, imaged_text_level_cost_shadow, self.pos[0] + align['level_cost']['x'] + 1,
                           self.pos[1] + align['level_cost']['y'] + 1, 150)
                # level cost
                imaged_text_level_cost = texted_level_cost.render(str(self.level_up_cost), True, color)
                blit_alpha(screen, imaged_text_level_cost, self.pos[0] + align['level_cost']['x'],
                           self.pos[1] + align['level_cost']['y'], 220)

            # level box
            pygame.draw.circle(circle, color, (self.pos[0] + align['circle']['x'], self.pos[1] + align['circle']['y']),
                               round(0.13 * BOX_SIZE))
            screen.blit(circle, (0, 0))

            # level text
            # shadow
            imaged_text_level_shadow = texted_level.render(str(self.level), True, (0, 0, 0))
            blit_alpha(screen, imaged_text_level_shadow, self.pos[0] + align['level']['x'] + 1,
                       self.pos[1] + align['level']['y'] + 1, 220)

            imaged_text_level = texted_level.render(str(self.level), True, (250, 250, 10))
            blit_alpha(screen, imaged_text_level, self.pos[0] + align['level']['x'], self.pos[1] + align['level']['y'],
                       215)

        def show_range(self):
            if round(SCREEN_SIZE[0] / BOX_SIZE) >= 1 + self.t_range*2:
                screen.blit(self.range_surface,
                            (self.pos[0] - self.t_range * BOX_SIZE, self.pos[1] - self.t_range * BOX_SIZE))
            else:
                self.t_range = 20
                screen.blit(self.range_surface, (0, 0))

    class Projectile(pygame.sprite.Sprite):
        def __init__(self, spawn_pos, enemy, attack, skin, name, velocity=8):
            super().__init__()
            self.pos = spawn_pos
            self.enemy = enemy
            self.attack = attack
            self.skin = skin
            self.skin_rect = skin.get_rect()
            self.skin_rect.x = self.pos[0]
            self.skin_rect.y = self.pos[1]
            self.velocity = velocity
            self.distance = None
            self.name = name

            enemy_pos = self.enemy.get_pos()
            enemy_pos = (enemy_pos[0] + BOX_SIZE / 4, enemy_pos[1] + BOX_SIZE / 4)
            self.pos = self.skin_rect
            self.delta_x = enemy_pos[0] - self.pos[0]
            self.delta_y = enemy_pos[1] - self.pos[1]

        def show(self):
            enemy_pos = self.enemy.get_pos()
            enemy_pos = (enemy_pos[0] + BOX_SIZE / 4, enemy_pos[1] + BOX_SIZE / 4)
            self.pos = self.skin_rect
            self.delta_x = enemy_pos[0] - self.pos[0]
            self.delta_y = enemy_pos[1] - self.pos[1]
            self.distance = round((self.delta_x ** 2 + self.delta_y ** 2) ** 0.5)

            if self.distance < BOX_SIZE:
                self.skin = pygame.transform.scale(self.skin, get_size_from_distance(self.distance))

            if self.distance != 0:
                if self.delta_x < 0:
                    angle = math.degrees(math.asin(self.delta_y / self.distance))
                else:
                    angle = -math.degrees(math.asin(self.delta_y / self.distance)) + 180

                rot_image = pygame.transform.rotate(self.skin, angle)
                rot_rect = rot_image.get_rect(center=self.skin_rect.center)
                screen.blit(rot_image, rot_rect)
            else:
                screen.blit(self.skin, self.skin_rect)

        def move(self):
            velocity = self.velocity * BOX_SIZE * speed_up[2] / 50
            if abs(self.delta_x) >= velocity:
                self.skin_rect.x += ((abs(self.delta_x/100) + velocity) * self.delta_x) / abs(self.delta_x)
            else:
                self.skin_rect.x += self.delta_x
            if abs(self.delta_y) >= velocity:
                self.skin_rect.y += ((abs(self.delta_y/100) + velocity) * self.delta_y) / abs(self.delta_y)
            else:
                self.skin_rect.y += self.delta_y

    class Monster(pygame.sprite.Sprite):

        def __init__(self, name, spawn_pos, giant=False):
            super().__init__()  # La class hérite de la super class Sprite de pygame
            for monst in CSV_SPECS['monsters']:
                if name == monst['Name']:
                    self.stable_specs = monst.copy()

            self.max_health = self.stable_specs['Max_health'] * life_amplificator
            self.name = self.stable_specs['Name']
            self.value = self.stable_specs['Money_value']
            self.image = self.stable_specs['Image']
            self.boss = giant

            if giant:
                self.image = self.stable_specs['Giant_image']
                self.max_health *= 8
                self.value *= 4
                self.stable_specs['Speed'] = round(self.stable_specs['Speed']/1.5)
            if self.stable_specs['Speed'] <= 0:
                self.stable_specs['Speed'] = 1

            self.size = self.image.get_width()
            self.health = self.max_health

            # - Position -
            self.random_shift = random.randint(-round(BOX_SIZE / 5), round(BOX_SIZE / 5))
            self.to_center = (self.size - BOX_SIZE) / 2 + self.random_shift
            self.spawn_pos = (spawn_pos[0] - self.to_center, spawn_pos[1] - self.to_center)
            self.rect = self.image.get_rect()
            self.rect.x = self.spawn_pos[0]  # on change la position du monstre dans le rect
            self.rect.y = self.spawn_pos[1] - self.rect.height/2.5

            # - Health -
            self.hb_border = 2 * 2
            self.hb_back = pygame.transform.scale(pygame.image.load('assets/pixels/gray.jpg'),
                                                  (self.size, round(self.size / 5)))
            self.hb_back_rect = self.hb_back.get_rect()

            self.current_hb = pygame.transform.scale(pygame.image.load('assets/pixels/red.jpg'), (
                self.size - self.hb_border, round(self.size / 5) - self.hb_border))
            self.current_hb_rect = self.current_hb.get_rect()

            self.transition_health = self.health

            # - Move -
            self.static_move_cooldown = round(150 / self.stable_specs['Speed'])
            self.dynamic_move_cooldown = self.static_move_cooldown

            self.current_box = [spawn_pos[0], spawn_pos[1]]

            self.direction = -1
            self.axe = 0

        def spawn(self):
            screen.blit(self.image, self.spawn_pos)

        def get_pos(self):
            return round(self.rect.x + self.to_center), round(self.rect.y + self.to_center)

        def move(self):
            animation_smoothness = 3
            for path in MAP['path']:
                if path[0][0] == self.current_box[0] and path[0][1] == self.current_box[1]:
                    if path[1] == 'l' or path[1] == 'start' or path[1] == 'end':
                        self.axe, self.direction = 0, -1
                    elif path[1] == 'u':
                        self.axe, self.direction = 1, -1
                    elif path[1] == 'd':
                        self.axe, self.direction = 1, 1
                    elif path[1] == 'r':
                        self.axe, self.direction = 0, 1

            if self.dynamic_move_cooldown > 0:
                self.dynamic_move_cooldown -= 1 * speed_up[2]
                if self.dynamic_move_cooldown != 0:
                    if abs(round(BOX_SIZE / self.static_move_cooldown * speed_up[2] * self.direction)
                           - BOX_SIZE / self.static_move_cooldown * speed_up[2] * self.direction) > 0.3:
                        if self.dynamic_move_cooldown % animation_smoothness == 0:
                            self.rect[self.axe] += BOX_SIZE / self.static_move_cooldown * speed_up[2] * self.direction * \
                                                   animation_smoothness
                    else:
                        self.rect[self.axe] += BOX_SIZE / self.static_move_cooldown * speed_up[2] * self.direction

            else:
                self.rect[self.axe] = self.current_box[self.axe] - self.to_center + BOX_SIZE * self.direction

                self.current_box[self.axe] += BOX_SIZE * self.direction
                self.dynamic_move_cooldown = self.static_move_cooldown

        def show_health(self):
            self.hb_back_rect.x = self.rect.x
            self.hb_back_rect.y = self.rect.y + self.size + 10

            self.current_hb_rect.x = self.rect.x + self.hb_border / 2
            self.current_hb_rect.y = self.rect.y + self.size + 10 + self.hb_border / 2

            # back
            screen.blit(self.hb_back, self.hb_back_rect)

            # transition

            if self.transition_health > self.health:
                self.transition_health -= 0.02 + ((self.transition_health - self.health) / 10) * speed_up[2]
                transition_color = (255, 255, 0)
                transition_width = round(
                    (self.size - self.hb_border) * (self.transition_health / self.max_health))
                transition_bar_rect = pygame.Rect(self.current_hb_rect.x, self.current_hb_rect.y, transition_width,
                                                  self.current_hb_rect.height)

                pygame.draw.rect(screen, transition_color, transition_bar_rect)

            # current
            self.current_hb = pygame.transform.scale(self.current_hb, (
                round((self.size - self.hb_border) * (self.health / self.max_health)),
                round(self.size / 5) - self.hb_border))
            screen.blit(self.current_hb, self.current_hb_rect)

        def change_health(self, value):
            if value < 0 and self.transition_health == self.health:
                self.transition_health = self.health
            if self.health + value > self.max_health:
                self.health = self.max_health
            else:
                self.health += value

    # --- INIT ---
    # spawn position
    SPAWN_POS = (MAP['path'][0][0][0], MAP['path'][0][0][1])

    SCREEN_SIZE = MAP['screen']
    BOX_SIZE = MAP['box']
    BOX_SURFACE = (BOX_SIZE, BOX_SIZE)

    SMALL_BOX_SIZE = round(BOX_SIZE / 4)
    SMALL_BOX_SURFACE = (SMALL_BOX_SIZE, SMALL_BOX_SIZE)

    BUTTON_SIZE = (100, 100)
    SMALL_BUTTON_SIZE = (50, 50)

    # - Init pygame -
    pygame.init()
    pygame.mouse.set_visible(True)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("The Best Tower-Defense")

    # - Clocks -
    clock = pygame.time.Clock()
    dc_clock = pygame.time.Clock()

    # - Background  and buildable boxes -
    MAP['buildable_squares'], background = get_background(MAP)

    # - Selector -
    selector = pygame.transform.smoothscale(pygame.image.load('assets/selector.png').convert_alpha(),
                                            (BOX_SIZE - round(BOX_SIZE / 8), BOX_SIZE - round(BOX_SIZE / 8)))
    rect_selector = selector.get_rect()

    # - Towers -
    choosing_tower_pos = ((0, 0), (BOX_SIZE / 2, 0), (0, BOX_SIZE / 2), (BOX_SIZE / 2, BOX_SIZE / 2))
    choosing_tower = {}

    tower_types = ['rapid', 'long', 'fire', 'normal']
    for i in range(len(tower_types)):
        choosing_tower[tower_types[i]] = (
            (pygame.transform.smoothscale(pygame.image.load(f'assets/towers/{tower_types[i]}.png').convert_alpha(),
                                          (round(BOX_SIZE / 2), round(BOX_SIZE / 2))), choosing_tower_pos[i]))

    selected_tower_yes_image = pygame.Surface((round(BOX_SIZE / 2), round(BOX_SIZE / 2)), pygame.SRCALPHA)
    selected_tower_yes_image.fill((10, 250, 10, 160))
    selected_tower_no_image = pygame.Surface((round(BOX_SIZE / 2), round(BOX_SIZE / 2)), pygame.SRCALPHA)
    selected_tower_no_image.fill((250, 10, 10, 140))

    towers = pygame.sprite.Group()

    tower_cost = 100
    can_buy = False

    # - Monsters -
    monsters = pygame.sprite.Group()

    burning = pygame.image.load('assets/projectiles/fire.png')

    monsters_killed = []

    # - Player -
    player = Player(start_money=round(tower_cost * 2.5), max_health=20)

    # - Menu -
    play_img = pygame.transform.smoothscale(pygame.image.load('assets/buttons/play.png').convert_alpha(), BUTTON_SIZE)
    play_img_rect = play_img.get_rect()
    play_img_rect.x = SCREEN_SIZE[0] - play_img_rect.width - 20
    play_img_rect.y = SCREEN_SIZE[1] - play_img_rect.height - 20

    pause_img = pygame.transform.smoothscale(pygame.image.load('assets/buttons/pause.png').convert_alpha(), BUTTON_SIZE)
    pause_img_rect = play_img.get_rect()
    pause_img_rect.x = SCREEN_SIZE[0] - pause_img_rect.width - 20
    pause_img_rect.y = SCREEN_SIZE[1] - pause_img_rect.height - 20

    resume_img = pygame.transform.smoothscale(pygame.image.load('assets/buttons/resume.png').convert_alpha(),
                                              BUTTON_SIZE)
    resume_img_rect = play_img.get_rect()
    resume_img_rect.x = SCREEN_SIZE[0] - resume_img_rect.width - 20
    resume_img_rect.y = SCREEN_SIZE[1] - resume_img_rect.height - 20

    auto_play_on_img = pygame.transform.smoothscale(
        pygame.image.load('assets/buttons/auto_play_on.png').convert_alpha(),
        SMALL_BUTTON_SIZE)
    auto_play_on_img_rect = auto_play_on_img.get_rect()
    auto_play_on_img_rect.x = - auto_play_on_img_rect.width + SCREEN_SIZE[0] - play_img_rect.width - 30
    auto_play_on_img_rect.y = SCREEN_SIZE[1] - play_img_rect.height - 20
    auto_play_off_img = pygame.transform.smoothscale(
        pygame.image.load('assets/buttons/auto_play_off.png').convert_alpha(),
        SMALL_BUTTON_SIZE)
    auto_play_off_img_rect = auto_play_off_img.get_rect()
    auto_play_off_img_rect.x = - auto_play_off_img_rect.width + SCREEN_SIZE[0] - play_img_rect.width - 30
    auto_play_off_img_rect.y = SCREEN_SIZE[1] - play_img_rect.height - 20

    speed_up = [False, 10, 1]
    speed_up_on_img = pygame.transform.smoothscale(pygame.image.load('assets/buttons/speed_on.png').convert_alpha(),
                                                   SMALL_BUTTON_SIZE)
    speed_up_on_img_rect = speed_up_on_img.get_rect()
    speed_up_on_img_rect.x = - speed_up_on_img_rect.width + SCREEN_SIZE[0] - play_img_rect.width - 30
    speed_up_on_img_rect.y = SCREEN_SIZE[1] - play_img_rect.height - 20 + auto_play_on_img_rect.height + 10
    speed_up_off_img = pygame.transform.smoothscale(pygame.image.load('assets/buttons/speed_off.png').convert_alpha(),
                                                    SMALL_BUTTON_SIZE)
    speed_up_off_img_rect = speed_up_off_img.get_rect()
    speed_up_off_img_rect.x = - speed_up_off_img_rect.width + SCREEN_SIZE[0] - play_img_rect.width - 30
    speed_up_off_img_rect.y = SCREEN_SIZE[1] - play_img_rect.height - 20 + auto_play_on_img_rect.height + 10

    life_icon = pygame.transform.smoothscale(pygame.image.load('assets/life.png').convert_alpha(), SMALL_BUTTON_SIZE)
    life_icon_rect = life_icon.get_rect()
    life_icon_rect.x = 20 + player.hb_back_width
    life_icon_rect.y = SCREEN_SIZE[1] - life_icon_rect.height - 5

    life_icon_border = pygame.transform.smoothscale(pygame.image.load('assets/life_border.png').convert_alpha(),
                                                    SMALL_BUTTON_SIZE)
    life_icon_border_rect = life_icon_border.get_rect()
    life_icon_border_rect.x = 20 + player.hb_back_width
    life_icon_border_rect.y = SCREEN_SIZE[1] - life_icon_border_rect.height - 5

    # - Projectile -
    projectiles = pygame.sprite.Group()

    started = False
    playing = False
    auto_play = False

    # - Music -
    pygame.mixer.music.load('assets/sounds/music.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    sounds = {}
    sounds_name_volume = [('place_tower.mp3', 0.3), ('destroy_tower.mp3', 0.2), ('life_lost.wav', 0.3),
                          ('monster_killed.mp3', 0.6), ('spawn_monster.mp3', 0.3), ('new_wave.wav', 0.2),
                          ('selection_mode_switch.mp3', 0.3), ('tower_selected.wav', 0.2), ('win.wav', 0.4),
                          ('lose.wav', 0.4), ('level_up.mp3', 0.2)]

    for name in sounds_name_volume:
        sounds[name[0][:-4]] = pygame.mixer.Sound(f'assets/sounds/{name[0]}')
        sounds[name[0][:-4]].set_volume(name[1])

    # --- Load images ---

    for monster_type in CSV_SPECS['monsters']:
        size = round(BOX_SIZE / 2 + 2 * monster_type['Size'])
        monster_type['Image'] = pygame.transform.smoothscale(
            pygame.image.load(f'assets/mobs/monsters/5 pixels/{monster_type["Name"]}.png'), (size, size))

        giant_size = size * 2
        monster_type['Giant_image'] = pygame.transform.smoothscale(
            pygame.image.load(f'assets/mobs/monsters/5 pixels/{monster_type["Name"]}.png'), (giant_size, giant_size))

    # - Random waves -
    life_amplificator = 1

    # - Others -

    # my_list = []

    # - mainloop -f

    # first_monster = None

    running = True
    while running:
        if player.game_over:
            print('GAME OVER LA')
            game_over_background = screen.copy()
            main(MAPS[menu(game_over_background)])

        # - Screen update -
        pygame.display.flip()

        clock.tick(60)

        # - background -
        screen.blit(background, (0, 0))

        # --- Mouse position ---
        mouse_x, mouse_y = pygame.mouse.get_pos()
        box_mouse_x = round((mouse_x - BOX_SIZE / 2) / BOX_SIZE) * BOX_SIZE
        box_mouse_y = round((mouse_y - BOX_SIZE / 2) / BOX_SIZE) * BOX_SIZE

        # --- End of the wave ---
        if started and not player.in_wave and player.m_left <= 0 and not auto_play:
            playing = False
            started = False
            player.money += tower_cost * life_amplificator

        if player.current_wave >= len(WAVES) - 1:
            pass
            #print("Dernière vague/terminé  !!!")

        # --- Events ---
        for event in pygame.event.get():

            # - Quit -
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # - Selection_mode -
            if player.editor_mode and event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                player.selection_mode = True
                last_tower_type = None

            if event.type == pygame.KEYDOWN:

                # - Show menu (restart game) -
                if event.key == pygame.K_ESCAPE:
                    player.game_over = True

                # - Spawn monsters with keys -
                if event.key == pygame.K_g:
                    new_monster = Monster(name='echidna', spawn_pos=SPAWN_POS, giant=True)
                    new_monster.spawn()
                    monsters.add(new_monster)

                if event.key == pygame.K_f:
                    new_monster = Monster(name='griffin', spawn_pos=SPAWN_POS, giant=True)
                    new_monster.spawn()
                    monsters.add(new_monster)

                if event.key == pygame.K_q:
                    new_monster = Monster(name='goblin', spawn_pos=SPAWN_POS, giant=True)
                    new_monster.spawn()
                    monsters.add(new_monster)

                if event.key == pygame.K_s:
                    new_monster = Monster(name='giant', spawn_pos=SPAWN_POS, giant=True)
                    new_monster.spawn()
                    monsters.add(new_monster)

                if event.key == pygame.K_d:
                    new_monster = Monster(name='witch', spawn_pos=SPAWN_POS, giant=True)
                    new_monster.spawn()
                    monsters.add(new_monster)

                # - Remove/destroy tower -
                if event.key == pygame.K_BACKSPACE:
                    for tower in towers:
                        if tower.pos[0] == box_mouse_x and tower.pos[1] == box_mouse_y:
                            towers.remove(tower)
                            sounds['destroy_tower'].play()
                            MAP['buildable_squares'][tower.pos] = True
                            player.money += round(tower.value / 2)
                            break

            # - Menu -
            if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 and
                (play_img_rect.x <= mouse_x <= play_img_rect.x + play_img_rect.width and
                 play_img_rect.y <= mouse_y <= play_img_rect.y + play_img_rect.height)) or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                if not playing and not started:
                    started = True
                    playing = True
                else:
                    playing = switcher(playing)

            if event.type == pygame.MOUSEBUTTONUP:

                # - Editor mode -
                if event.button == 1:  # left click
                    if dc_clock.tick() < 200:  # double click
                        sounds['selection_mode_switch'].play()
                        player.editor_mode = switcher(player.editor_mode)

                    if auto_play_on_img_rect.x <= mouse_x <= auto_play_on_img_rect.x + auto_play_on_img_rect.width and \
                            auto_play_on_img_rect.y <= mouse_y <= auto_play_on_img_rect.y + auto_play_on_img_rect.height:
                        auto_play = switcher(auto_play)

                    if speed_up_on_img_rect.x <= mouse_x <= speed_up_on_img_rect.x + speed_up_on_img_rect.width and \
                            speed_up_on_img_rect.y <= mouse_y <= speed_up_on_img_rect.y + speed_up_on_img_rect.height:
                        speed_up[0] = switcher(speed_up[0])

                if event.button == 3:
                    player.selection_mode = False
                    if player.editor_mode:
                        if mouse_on_buildable and can_buy:
                            # - Tower placement -
                            sounds['place_tower'].play()
                            towers.add(Tower(tower_type, (box_mouse_x, box_mouse_y)))
                            MAP['buildable_squares'][(box_mouse_x, box_mouse_y)] = False
                            player.money -= tower_cost
                            break
                        else:
                            for tower in towers:
                                if tower.pos[0] == box_mouse_x and tower.pos[1] == box_mouse_y:
                                    if player.money >= tower.level_up_cost:
                                        tower.value += tower.level_up_cost / 2
                                        player.money -= tower.level_up_cost
                                        tower.level_up()
                                    break

        if playing:
            if not player.in_wave and len(monsters) == 0:
                player.current_wave += 1
                if player.current_wave < len(WAVES):
                    _thread.start_new_thread(new_wave, (WAVES[player.current_wave], sounds,))
                else:
                    _thread.start_new_thread(new_wave, (generate_random_wave(player.current_wave, life_amplificator), sounds,))
                player.in_wave = True
                life_amplificator *= 1.08
                print(life_amplificator)
                if player.current_health < player.max_health:
                    player.current_health += 1

            # --- Monsters ---

            # - TRY TO : First mob to target -
            a = '''
            if first_monster is not None:
                for monster in monsters:
                    if monster.get_pos() == first_monster.get_pos():
                        monsters.remove(monster)
                        monsters_copy = monsters.copy()
                        monsters.empty()
                        monsters.add(monster)
                        for monster_copy in monsters_copy:
                            monsters.add(monster_copy)
            else:
                if len(monsters) > 0:
                    for monster in monsters:
                        first_monster = monster
                        break'''
            # print(pygame.sprite.LayeredUpdates.sprites(monsters))

            for monster in monsters:
                monster_pos = monster.get_pos()

                if monster.name == 'witch':
                    for monster_heal in monsters:
                        near_monster = monster_heal.get_pos()
                        if near_monster[0] - (1.5 * BOX_SIZE) <= monster_pos[0] <= near_monster[0] + (1.5 * BOX_SIZE) \
                                and near_monster[1] - BOX_SIZE <= monster_pos[1] <= near_monster[1] + BOX_SIZE:
                            monster.change_health(monster.max_health/500 * speed_up[2])

                # - Move monsters -
                monster.move()

                # - TRY TO : First mob to target -
                a = '''
                first_monster_pos = first_monster.get_pos()
                for i in range(len(MAP['path'])-2, -1, -1):
                    if monster_pos[0] == MAP['path'][i][0][0]:
                        if MAP['path'][i][1] == 'd':
                            if MAP['path'][i][0][1] <= monster_pos[1] <= MAP['path'][i + 1][0][1]:
                                if monster_pos[1] > first_monster_pos[1]:
                                    first_monster = monster
                        elif MAP['path'][i][1] == 'u':
                            if MAP['path'][i][0][1] >= monster_pos[1] >= MAP['path'][i + 1][0][1]:
                                if monster_pos[1] < first_monster_pos[1]:
                                    first_monster = monster
    
                    if monster_pos[1] == MAP['path'][i][0][1]:
                        if MAP['path'][i][1] == 'l' or MAP['path'][i][1] == 'start':
                            if MAP['path'][i][0][0] >= monster_pos[0] >= MAP['path'][i + 1][0][0]:
                                if monster_pos[0] < first_monster_pos[0]:
                                    first_monster = monster
                        elif MAP['path'][i][1] == 'r':
                            if MAP['path'][i][0][0] <= monster_pos[0] <= MAP['path'][i + 1][0][0]:
                                if monster_pos[0] > first_monster_pos[0]:
                                    first_monster = monster'''

                for tower in towers:
                    # - Tower shoot -
                    dist_x = monster_pos[0] - tower.pos[0]
                    dist_y = monster_pos[1] - tower.pos[1]
                    t_range = tower.t_range * BOX_SIZE
                    if -t_range <= dist_x <= t_range and -t_range <= dist_y <= t_range and tower.shoot_cooldown <= 0:
                        if tower.name == 'fire':
                            blit_alpha(screen,
                                       pygame.transform.smoothscale(burning, (monster.rect.width, monster.rect.height)),
                                       monster.rect.x, monster.rect.y, 180)
                            monster.change_health(-(tower.attack * tower.attack_speed**2)/10 * speed_up[2])

                        else:
                            tower.shoot((tower.pos[0] + BOX_SIZE / 4, tower.pos[1] + BOX_SIZE / 4), monster,
                                        velocity=tower.proj_velocity)
                            tower.shoot_cooldown = round(1000 / tower.attack_speed)

            # - move projectiles -
            for projectile in projectiles:
                projectile.move()

            for tower in towers:
                # - Tower cooldown -
                if tower.name != 'fire':
                    if tower.shoot_cooldown > 0:
                        tower.shoot_cooldown -= 1 * speed_up[2]

        for monster in monsters:

            # - kill monsters -
            if monster.get_pos()[0] <= 0:
                sounds['life_lost'].play()
                if monster.boss == True:
                    player.current_health -= 5
                else:
                    player.current_health -= 1
                monster.health = 0
                player.money -= round(monster.value * life_amplificator)
            # kill monster
            if monster.health <= 0:
                monsters_killed.append({'x': monster.rect.x, 'y': monster.rect.y, 'image': monster.image, 'alpha': 255})
                monsters.remove(monster)
                sounds['monster_killed'].play()
                player.money += round(monster.value * life_amplificator)
                player.m_left -= 1
                continue

            # - Show health -
            monster.show_health()

        # - Draw towers and tower level -
        for tower in towers:
            screen.blit(tower.skin, tower.pos)

            # - Level -
            tower.show_level(box_mouse_x, box_mouse_y)

        # - Draw projectiles -
        for projectile in projectiles:
            projectile.show()

        # - Draw Monsters -
        # killed monsters
        monsters_to_depop = 0
        for i in range(len(monsters_killed)):
            if monsters_killed[i]['alpha'] <= 3:
                monsters_to_depop += 1
            blit_alpha(screen, monsters_killed[i]['image'], monsters_killed[i]['x'], monsters_killed[i]['y'],
                       round(monsters_killed[i]['alpha']))
            if speed_up[0]:
                monsters_killed[i]['alpha'] **= 1 / 1.05
            else:
                monsters_killed[i]['alpha'] **= 1 / 1.02
        for i in range(monsters_to_depop):
            del monsters_killed[0]


        # alive monsters
        monsters.draw(screen)

        # - Tower show range -
        for tower in towers:
            if box_mouse_x == tower.pos[0] and box_mouse_y == tower.pos[1] and player.editor_mode:
                tower.show_range()

        # --- Projectiles ---
        for proj in projectiles:
            if proj.distance <= 7 * speed_up[2]:
                if proj.name == 'long':
                    for monster in monsters:
                        monster_pos = monster.get_pos()
                        if proj.skin_rect.x - BOX_SIZE <= monster_pos[0] <= proj.skin_rect.x + BOX_SIZE \
                                and proj.skin_rect.y - BOX_SIZE <= monster_pos[1] <= proj.skin_rect.y + BOX_SIZE:
                            monster.change_health(-proj.attack)
                else:
                    proj.enemy.change_health(-proj.attack)
                projectiles.remove(proj)
            elif str(proj.enemy) == '<Monster Sprite(in 0 groups)>' or not (
                    0 <= proj.skin_rect.x <= SCREEN_SIZE[0]) or not (0 <= proj.skin_rect.y <= SCREEN_SIZE[1]):
                projectiles.remove(proj)

        # --- Towers ---
        # - Is the mouse on buildable ? -
        mouse_on_buildable = False
        for buildable in MAP['buildable_squares']:
            if MAP['buildable_squares'][(box_mouse_x, box_mouse_y)]:
                mouse_on_buildable = True

        if player.editor_mode:
            blit_alpha(screen, selector, box_mouse_x + BOX_SIZE / 16, box_mouse_y + BOX_SIZE / 16, 90)

        # - Show selector and tower choosing -
        if player.editor_mode and mouse_on_buildable:

            if player.selection_mode:
                # Blit 4 towers images
                for type in tower_types:
                    screen.blit(choosing_tower[type][0],
                                (box_mouse_x + choosing_tower[type][1][0], box_mouse_y + choosing_tower[type][1][1]))

                # selected tower highlight
                tower_type = selected_tower((mouse_x - box_mouse_x, mouse_y - box_mouse_y))
                if last_tower_type != tower_type:
                    sounds['tower_selected'].play()
                last_tower_type = tower_type

                if player.money >= tower_cost:
                    screen.blit(selected_tower_yes_image, (box_mouse_x + choosing_tower[tower_type][1][0],
                                                           box_mouse_y + choosing_tower[tower_type][1][1]))
                    can_buy = True
                else:
                    screen.blit(selected_tower_no_image, (box_mouse_x + choosing_tower[tower_type][1][0],
                                                          box_mouse_y + choosing_tower[tower_type][1][1]))
                    can_buy = False
            else:
                screen.blit(selector, (box_mouse_x + BOX_SIZE / 16, box_mouse_y + BOX_SIZE / 16))

        # - player health -
        player.update()

        # --- Menu ---
        if not started and not playing:
            screen.blit(play_img, play_img_rect)
        elif not playing:
            screen.blit(resume_img, resume_img_rect)
        else:
            screen.blit(pause_img, pause_img_rect)

        if speed_up[0]:
            screen.blit(speed_up_on_img, speed_up_on_img_rect)
            speed_up[2] = speed_up[1]
        else:
            screen.blit(speed_up_off_img, speed_up_off_img_rect)
            speed_up[2] = 1

        if auto_play:
            screen.blit(auto_play_on_img, auto_play_on_img_rect)
        else:
            screen.blit(auto_play_off_img, auto_play_off_img_rect)


def linear_interpolation(max_value, min_value, wanted_value, max_color, min_color):
    new_color = []
    for i in range(len(max_color)):
        new_color.append(round(max_color[i] * ((wanted_value - min_value) / (max_value - min_value)) +
                               min_color[i] * ((max_value - wanted_value) / (max_value - min_value))))
    return new_color


def switcher(boolean):
    if boolean:
        return False
    else:
        return True


def path_switcher(dir):
    if dir == 'l':
        return 'r'
    elif dir == 'r':
        return 'l'
    elif dir == 'u':
        return 'd'
    elif dir == 'd':
        return 'u'
    elif dir == 'start':
        return 'r'


def selected_tower(mouse_pos):
    global BOX_SIZE
    if mouse_pos[0] <= BOX_SIZE / 2:
        if mouse_pos[1] <= BOX_SIZE / 2:
            t_type = 'rapid'
        else:
            t_type = 'fire'
    else:
        if mouse_pos[1] <= BOX_SIZE / 2:
            t_type = 'long'
        else:
            t_type = 'normal'
    return t_type


def new_wave(wave, sounds):
    sounds['new_wave'].play()
    player.m_left = len(wave)
    for mob in wave:
        if not playing:
            wait_until_playing()
        # - Spawn monster -
        is_giant = False
        if len(mob) == 3:
            is_giant = mob[2]
        new_monster = Monster(name=mob[0], spawn_pos=SPAWN_POS, giant=is_giant)
        new_monster.spawn()
        monsters.add(new_monster)
        sounds['spawn_monster'].play()
        time.sleep(mob[1] / speed_up[2])
    player.in_wave = False


def wait_until_playing():
    global playing
    while True:
        if playing:
            return
        else:
            time.sleep(0.1)


def blit_alpha(target, source, x, y, opacity):
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, (x, y))


def choose_path(path_indice, MAP):
    current_path = MAP['path'][path_indice][1]
    previous_path = MAP['path'][path_indice - 1][1]
    if current_path == 'start':
        current_path = 'l'
    elif current_path == 'end':
        current_path = 'l'
    if previous_path == 'start':
        previous_path = 'l'
    elif previous_path == 'end':
        previous_path = 'l'

    directions = previous_path + current_path

    if directions == 'ur':
        directions = 'ld'
    elif directions == 'rd':
        directions = 'ul'
    elif directions == 'dl':
        directions = 'ru'
    elif directions == 'lu':
        directions = 'dr'
    a = random.randint(1, 1)

    # print(directions, f'assets/paths/{random.randint(0, 0)}_{directions}')
    return pygame.transform.smoothscale(pygame.image.load(f'assets/paths/{4}_{directions}.png')
                                        .convert_alpha(), BOX_SURFACE)


def get_background(MAP):
    tower_buildable_boxes = {}
    all_grass_names = (
        ('grass_square_swamp', 'farm', 'ruins', 'windmill'),
        ('grass_square1', 'grass_square2', 'grass_square3', 'grass_square4'))

    all_grass = [[pygame.transform.smoothscale(pygame.image.load(f'assets/grass/{name}.jpg'), BOX_SURFACE)
                  for name in all_grass_names[i]] for i in range(2)]

    for x in range(0, SCREEN_SIZE[0], BOX_SIZE):
        for y in range(0, SCREEN_SIZE[1], BOX_SIZE):
            # buildable squares
            tower_buildable_boxes[(x, y)] = True

            # background
            is_buildable = random.choices((0, 1), (0.15, 0.85))
            if is_buildable[0]:
                random_weight = (0.7, 0.1, 0.1, 0.1)
            else:
                random_weight = (0.4, 0.2, 0.2, 0.2)
                tower_buildable_boxes[(x, y)] = False

            grass = random.choices(all_grass[is_buildable[0]], random_weight)
            screen.blit(grass[0], (x, y))
            for i in range(len(MAP['path'])):
                if x == MAP['path'][i][0][0] and y == MAP['path'][i][0][1]:
                    tower_buildable_boxes[(x, y)] = False
                    screen.blit(choose_path(i, MAP), (x, y))
                    break

    return tower_buildable_boxes, screen.copy()


def get_size_from_distance(dist):
    size = 100 * dist / BOX_SIZE
    size = size**(1/1.5) * 4.6
    size = BOX_SIZE/2 * size / 100
    size = round(size)
    size = (size, size)
    return size


def generate_random_wave(wave_number, amplificator):
    monsters_names = []
    monsters_spawn_chance = []
    for monster in CSV_SPECS['monsters']:
        monsters_names.append(monster['Name'])
        monsters_spawn_chance.append(monster['Spawn_chance']/100)
    monster_wave = []
    giant_spawn_chance = 0.01 * amplificator
    if giant_spawn_chance > 1:
        giant_spawn_chance = 1
    for i in range(round(wave_number/4), random.randint(round(wave_number/1.5), wave_number*2)):
        monster_wave.append((random.choices(monsters_names, monsters_spawn_chance)[0],  # Monster type
                             random.randint(10, 100)/(wave_number+(i/2)),  # Time to wait
                             random.choices((True, False), (giant_spawn_chance, 1-giant_spawn_chance))[0]))  # Is giant
    return monster_wave


# - Init pygame -
pygame.init()
pygame.mouse.set_visible(True)
SCREEN_SIZE = (250, 250)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("The Best Tower-Defense")

main(MAPS[menu()])
