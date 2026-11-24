
import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, game, image, x, y):
        super().__init__()

        self.game = game
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
