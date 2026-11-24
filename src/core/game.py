
import pygame

from src.core import settings


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )

        pygame.display.set_caption(settings.SCREEN_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill(settings.BLACK)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(settings.FPS)

        pygame.quit()
