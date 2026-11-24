
from pathlib import Path

import pygame


ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"


class AssetManager:
    def __init__(self):
        self.images = {}

    def load_image(self, name, path):
        image_path = ASSETS_DIR / path

        if name not in self.images:
            self.images[name] = pygame.image.load(image_path).convert_alpha()

        return self.images[name]
