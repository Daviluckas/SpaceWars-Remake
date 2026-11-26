
from pathlib import Path

import pygame

from src.core import settings
from src.systems.video_background import VideoBackground


ASSETS_DIR = Path(__file__).resolve().parents[3] / "assets"


class MainMenu:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )

        pygame.display.set_caption(settings.SCREEN_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        self.background = VideoBackground(
            str(ASSETS_DIR / "videos" / "menu" / "background_menu.mp4"),
            settings.SCREEN_WIDTH,
            settings.SCREEN_HEIGHT
        )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        self.background.update()

    def draw(self):
        self.background.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(settings.FPS)

        self.background.stop()
