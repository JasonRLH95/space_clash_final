
from abc import ABC, abstractmethod
import pygame


class Entity(ABC):
    def __init__(self, x, y, width, height, color=None):
        self.rect = pygame.Rect(x, y, width, height)
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
        if hasattr(other, 'rect'):
            return self.rect.colliderect(other.rect)
        elif isinstance(other, pygame.Rect):
            return self.rect.colliderect(other)
        return False
