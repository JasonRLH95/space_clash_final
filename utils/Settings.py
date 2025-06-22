"""
Global settings and constants for the Falling Blocks Game
"""

import pygame

# Initialize pygame fonts
pygame.init()

# --- Screen settings ---
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60
WINDOW_TITLE = "Space Clash"

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_RED = (180, 30, 30)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (30, 180, 30)
BLUE = (0, 0, 255)
LIGHT_SKY_BLUE = (173, 216, 230)
AQUA = (0, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
INDIGO = (75, 0, 130)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
DARK_YELLOW = (220, 220, 20)

# --- Player settings ---
PLAYER_WIDTH = 70
PLAYER_HEIGHT = 70
PLAYER_SPEED = 8
PLAYER_START_Y = SCREEN_HEIGHT - 60

# --- Meteor settings ---
METEOR_WIDTH = 60
METEOR_HEIGHT = 60
METEOR_SPAWN_RATE = 60

# Bullet settings
BULLET_WIDTH = 10
BULLET_HEIGHT = 40
BULLET_SPEED = 5

# --- Events ---
PLAYER_HIT = pygame.USEREVENT + 1
ENEMY_HIT = pygame.USEREVENT + 2

# --- Game rules ---
SCORE_PER_DODGE = 5
SCORE_PER_HIT = 25
MAX_NAME_LENGTH = 20
TOP_SCORES_DISPLAY = 15

# --- File paths ---
RECORDS_FILE_PATH = "game_records.json"

# --- Fonts ---
FONT_SMALL_SMALL = pygame.font.Font(None, 24)
FONT_SMALL = pygame.font.Font(None, 36)
FONT_SMALL_MEDIUM = pygame.font.Font(None, 42)
FONT_MEDIUM = pygame.font.Font(None, 56)
FONT_SMALL_LARGE = pygame.font.Font(None, 72)
FONT_LARGE = pygame.font.Font(None, 90)
FONT_HUGH = pygame.font.Font(None, 120)

FONT_BUTTON = pygame.font.Font(None, 50)

# --- Screen identifiers ---
SCREEN_MENU = "menu"
SCREEN_CHOOSE_PLAYER = "choose_player"
SCREEN_GAME = "game"
SCREEN_GAME_OVER = "game_over"
SCREEN_HIGH_SCORES = "high_scores"
