import pygame

from src.systems.animation import Animation


class Explosion(pygame.sprite.Sprite):
    def __init__(self, frames, x, y):
        super().__init__()

        self.frames = [
            pygame.transform.scale(frame, (105, 105))
            for frame in frames
        ]

        self.animation = Animation(
            self.frames,
            frame_duration=80,
            loop=False
        )

        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(x, y))


    def update(self):
        if self.animation.finished:
            self.kill()
            return

        self.image = self.animation.update()