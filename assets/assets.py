
import os
from p2.utils.Settings import *

pygame.font.init()
pygame.mixer.init()

# Fonts
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
SCORE_FONT = pygame.font.SysFont('comicsans', 30)

# Sounds
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("assets", "sound", "explosion.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("assets", "sound", "plasma_gun.wav"))
GAME_SOUND = pygame.mixer.Sound(os.path.join("assets", "sound", "space_music.mp3"))

# Sound channels
SPACE_CHANNEL = pygame.mixer.Channel(1)
SHOOT_CHANNEL = pygame.mixer.Channel(2)
EXPLOSION_CHANNEL = pygame.mixer.Channel(3)

# Spaceships Images
WHITE_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets", "images", "spaceship_white_2d.png"))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets", "images", "spaceship_red_2d.png"))
BLUE_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets", "images", "spaceship_blue_2d.png"))
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets", "images", "spaceship_yellow_2d.png"))

# Spaceships
WHITE_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(WHITE_SPACESHIP_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0)

RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0)

BLUE_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(BLUE_SPACESHIP_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 90)

YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 270)

# Backgrounds
SPACE_1 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "images", "space_background_1.jpg")), (SCREEN_WIDTH, SCREEN_HEIGHT))
SPACE_2 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "images", "space_background_2.jpg")), (SCREEN_WIDTH, SCREEN_HEIGHT))
SPACE_3 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "images", "space_background_3.jpg")), (SCREEN_WIDTH, SCREEN_HEIGHT))
SPACE_4 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "images", "space_background_4.jpg")), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Meteors
METEOR_1 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "images", "meteor_1.png")), (METEOR_WIDTH, METEOR_HEIGHT))
METEOR_2 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "images", "meteor_2.png")), (METEOR_WIDTH, METEOR_HEIGHT))
METEOR_3 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "images", "meteor_3.png")), (METEOR_WIDTH, METEOR_HEIGHT))
METEOR_4 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "images", "meteor_4.png")), (METEOR_WIDTH, METEOR_HEIGHT))

# Explosion
EXPLOSION_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "images", "explosion_1.png")), (METEOR_WIDTH, METEOR_HEIGHT)
)
