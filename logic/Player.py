
from interfaces.Entity import Entity
from utils.Settings import *
from logic.Bullet import Bullet


class Player(Entity):
    def __init__(self, spaceship, bullet_color, is_paused):
        x = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
        y = PLAYER_START_Y
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT, None, spaceship)
        self.is_paused = is_paused
        self.speed = PLAYER_SPEED
        self.spaceship = spaceship
        self.shot_color = bullet_color
        self.bullets = []
        self.last_shot_time = 0
        self.shoot_cooldown = 300

    # Handles the spaceship movement on screen
    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    # Draw the spaceship on screen
    def draw(self, surface):
        surface.blit(self.spaceship, (self.rect.x, self.rect.y))

    # Initiate spaceship position when starts new game
    def reset(self):
        self.bullets = []
        self.rect.x = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
        self.rect.y = PLAYER_START_Y

    # Handles the shooting action
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot_time >= self.shoot_cooldown:
            bullet_x = self.rect.centerx - 5
            bullet_y = self.rect.top
            bullet = Bullet(bullet_x, bullet_y, self.shot_color, self.is_paused)
            self.bullets.append(bullet)
            self.last_shot_time = now

    # Handles the bullets behavior
    def handle_bullets(self, surface):
        for bullet in self.bullets[:]:  # Copy list to allow removal
            bullet.update()
            bullet.draw(surface)
            if bullet.is_off_screen():
                self.bullets.remove(bullet)
