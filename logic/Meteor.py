

import random
from p2.interfaces.Entity import Entity
from p2.assets.assets import *


class Meteor(Entity):
    def __init__(self):
        x = random.randint(0, SCREEN_WIDTH - METEOR_WIDTH)
        y = 0
        super().__init__(x, y, METEOR_WIDTH, METEOR_HEIGHT)
        # Holds 4 different meteors and randomly generate the image of any new instance of Meteor class
        self.meteors_images = [METEOR_1, METEOR_2, METEOR_3, METEOR_4]
        self.original_image = random.choice(self.meteors_images)
        self.image = self.original_image

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.rotation_angle = 0
        self.speed = random.randint(1, 4)

    # Handles the meteor movements and rotation
    def update(self):
        self.rect.y += self.speed
        self.rotation_angle = (self.rotation_angle + 1) % 360  # Adjust speed here

        # Rotate image around center
        self.image = pygame.transform.rotate(self.original_image, self.rotation_angle)

        # Update rect to new size and re-center it
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)

    # Check if meteor got out of the screen
    def is_off_screen(self):
        return self.rect.top > SCREEN_HEIGHT


# Management class for the meteors instances
class MeteorManager:
    def __init__(self):
        self.meteors = []
        self.spawn_timer = 0
        self.spawn_rate = METEOR_SPAWN_RATE

    # Handles spawning behavior
    def update(self):
        self.spawn_timer += 1

        if self.spawn_timer >= self.spawn_rate:
            self.spawn_timer = 0
            new_meteor = Meteor()
            self.meteors.append(new_meteor)

        for meteor in self.meteors:
            meteor.update()

    # Draw the meteors on screen
    def draw(self, surface):
        for meteor in self.meteors:
            surface.blit(meteor.image, meteor.rect)

    # Removes the meteors the got out of the screen
    def remove_off_screen(self):
        count_removed = 0
        enemies_copy = self.meteors[:]
        for meteor in enemies_copy:
            if meteor.is_off_screen():
                self.meteors.remove(meteor)
                count_removed += 1
        return count_removed

    def get_meteors(self):
        return self.meteors

    # Clear meteors list and initiate spawning time to reset behavior
    def reset(self):
        self.meteors.clear()
        self.spawn_timer = 0
