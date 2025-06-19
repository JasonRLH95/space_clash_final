
import pygame


class Explosion:
    def __init__(self, x, y, image, duration=300):  # duration in ms
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.spawn_time = pygame.time.get_ticks()
        self.duration = duration

    # Handles the time to display the explosion
    def update(self):
        # Returns True if expired and should be removed
        return pygame.time.get_ticks() - self.spawn_time > self.duration

    # Draw the explosion on screen
    def draw(self, surface):
        surface.blit(self.image, self.rect)
