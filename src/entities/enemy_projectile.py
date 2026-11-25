import pygame

from src.entities.entity import Entity
from src.systems.animation import Animation


class EnemyProjectile(Entity):
    def __init__(self, game, x, y, animation_frames, target):
        image = pygame.transform.scale(
            animation_frames[0],
            (20, 20)
        )

        super().__init__(game, image, x, y)

        self.animation = Animation([
            pygame.transform.scale(frame, (20, 20))
            for frame in animation_frames
        ])

        direction = pygame.Vector2(
            target.rect.centerx - self.rect.centerx,
            target.rect.centery - self.rect.centery
        )

        if direction.length() > 0:
            self.direction = direction.normalize()
        else:
            self.direction = pygame.Vector2(0, 1)

        self.speed = 4

    def update(self):
        self.image = self.animation.update()

        self.rect.x += round(self.direction.x * self.speed)
        self.rect.y += round(self.direction.y * self.speed)

        if (
            self.rect.top > self.game.screen.get_height()
            or self.rect.right < 0
            or self.rect.left > self.game.screen.get_width()
        ):
            self.kill()