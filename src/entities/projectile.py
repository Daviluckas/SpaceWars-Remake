import pygame

from src.core import settings
from src.entities.entity import Entity
from src.systems.animation import Animation


class Projectile(Entity):
    def __init__(self, game, x, y, animation_frames):
        image = pygame.transform.scale(
            animation_frames[0],
            (12, 25)
        )

        super().__init__(game, image, x, y)

        self.animation = Animation([
            pygame.transform.scale(frame, (12, 25))
            for frame in animation_frames
        ])

        self.rect.size = (
            settings.PROJECTILE_WIDTH,
            settings.PROJECTILE_HEIGHT
        )


    def update(self):
        self.image = self.animation.update()

        self.rect.y -= settings.PROJECTILE_SPEED

        if self.rect.bottom < 0:
            self.kill()