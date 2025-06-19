
from p2.interfaces.Entity import Entity
from p2.assets.assets import *


class Bullet(Entity):
    def __init__(self, bullet_x, bullet_y, color):
        super().__init__(bullet_x, bullet_y, BULLET_WIDTH, BULLET_HEIGHT, color)
        self.speed = BULLET_SPEED

    # Update bullet movement
    def update(self):
        self.rect.y -= self.speed

    # Draw the bullet on screen
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    # Checks if bullet is out of screen
    def is_off_screen(self):
        return self.rect.bottom < 0
