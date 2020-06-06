import pygame
no_of_levels = 12
pygame.init()
screen = pygame.display.set_mode((1200, 650))
background = []
for i in range(no_of_levels):
    background_temp = pygame.image.load(
            "data/backgrounds/background"+str(i)+".png").convert_alpha()
    background.append(background_temp)
redbird = pygame.image.load(
    "data/red-bird.png").convert_alpha()
sling_image = pygame.image.load(
    "data/sling.png").convert_alpha()
full_sprite = pygame.image.load(
    "data/pig.png").convert_alpha()
rect = pygame.Rect(0, 0, 50, 50)
cropped = full_sprite.subsurface(rect).copy()
pig_image = pygame.transform.scale(cropped, (30, 30))
buttons = pygame.image.load(
    "data/use_buttons.png").convert_alpha()
pig_happy = pygame.image.load(
    "data/pig_win.png").convert_alpha()
stars = pygame.image.load(
    "data/stars.png").convert_alpha()
rect = pygame.Rect(0, 0, 200, 200)
star1 = stars.subsurface(rect).copy()
rect = pygame.Rect(204, 0, 200, 200)
star2 = stars.subsurface(rect).copy()
rect = pygame.Rect(426, 0, 200, 200)
star3 = stars.subsurface(rect).copy()
rect = pygame.Rect(164, 10, 60, 60)
pause_button = buttons.subsurface(rect).copy()
rect = pygame.Rect(24, 4, 100, 100)
replay_button = buttons.subsurface(rect).copy()
rect = pygame.Rect(142, 365, 130, 100)
next_button = buttons.subsurface(rect).copy()
rect = pygame.Rect(18, 212, 100, 100)
play_button = buttons.subsurface(rect).copy()


pigs = []
birds = []
balls = []
polys = []
beams = []
columns = []
static_block = []
poly_points = []
ball_number = 0
polys_dict = {}
mouse_distance = 0
rope_lenght = 90
angle = 0
x_mouse = 0
y_mouse = 0
count = 0
mouse_pressed = False
t1 = 0
tick_to_next_circle = 10
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
sling_x, sling_y = 135, 450
sling2_x, sling2_y = 160, 450
score = 0
game_state = 0
bird_path = []
counter = 0
restart_counter = False
bonus_score_once = True
bold_font = pygame.font.SysFont("arial", 30, bold=True)
bold_font2 = pygame.font.SysFont("arial", 40, bold=True)
bold_font3 = pygame.font.SysFont("arial", 50, bold=True)
wall = False