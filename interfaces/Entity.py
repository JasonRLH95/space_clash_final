
from abc import ABC, abstractmethod
import pygame


class Entity(ABC):
    def __init__(self, x, y, width, height, color=None, image=None):
        self.image = image
        self.rect = pygame.Rect(x, y, width, height)
        if image:
            self.mask = pygame.mask.from_surface(self.image)
        self.color = color
        self.speed = 0

    # Main struct for that method signature
    @abstractmethod
    def update(self, *args, **kwargs):
        """Must be implemented by subclasses"""
        pass

    # Main struct of draw method to handle draw actions
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def get_rect(self):
        return self.rect

    # Handles the collision between an instance and another
    def collides_with(self, other):
        if self.image:
            offset = (other.rect.x - self.rect.x, other.rect.y - self.rect.y)
            return self.mask.overlap(other.mask, offset) is not None
        else:
            if hasattr(other, 'rect'):
                return self.rect.colliderect(other.rect)
            elif isinstance(other, pygame.Rect):
                return self.rect.colliderect(other)
            return False
