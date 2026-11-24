import pygame

from src.core import settings
from src.entities.entity import Entity


class Player(Entity):
    def __init__(self, game, x, y):
        image = game.assets.load_image(
            "player",
            "sprites/player/player.png"
        )

        image = pygame.transform.scale(
            image,
            (settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT)
        )

        super().__init__(game, image, x, y)


    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= settings.PLAYER_SPEED

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += settings.PLAYER_SPEED

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= settings.PLAYER_SPEED

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += settings.PLAYER_SPEED

        self.rect.clamp_ip(
            pygame.Rect(0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))