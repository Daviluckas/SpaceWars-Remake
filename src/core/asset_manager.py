
from pathlib import Path

import pygame


ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"


class AssetManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.music = {}
        self.fonts = {}

    def load_image(self, name, path):
        image_path = ASSETS_DIR / path

        if name not in self.images:
            self.images[name] = pygame.image.load(image_path).convert_alpha()

        return self.images[name]

    
    def load_sound(self, name, path):
        sound_path = ASSETS_DIR / path

        if name not in self.sounds:
            self.sounds[name] = pygame.mixer.Sound(sound_path)

        return self.sounds[name]


    def load_music(self, name, path):
        music_path = ASSETS_DIR / path

        if name not in self.music:
            self.music[name] = music_path

        return self.music[name]


    def load_font(self, name, path, size):
        font_path = ASSETS_DIR / path
        key = (name, size)

        if key not in self.fonts:
            self.fonts[key] = pygame.font.Font(font_path, size)

        return self.fonts[key]

