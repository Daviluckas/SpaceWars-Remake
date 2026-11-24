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