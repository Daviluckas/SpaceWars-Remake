import pygame

from src.core import settings
from src.entities.entity import Entity


class Projectile(Entity):
    def __init__(self, game, x, y):
        image = pygame.Surface(
            (settings.PROJECTILE_WIDTH, settings.PROJECTILE_HEIGHT)
        )

        image.fill(settings.WHITE)

        super().__init__(game, image, x, y)

    def update(self):
        self.rect.y -= settings.PROJECTILE_SPEED
        
        if self.rect.bottom < 0:
            self.kill()