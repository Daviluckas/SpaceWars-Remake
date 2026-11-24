
import pygame

from src.core import settings
from src.core.asset_manager import AssetManager
from src.entities.player import Player

class Game:
    def __init__(self):
        pygame.init()

        self.assets = AssetManager()

        self.screen = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )

        pygame.display.set_caption(settings.SCREEN_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(self, 352, 500)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()


    def update(self):
        self.player.update()

    def draw(self):
        self.screen.fill(settings.BLACK)
        self.player.projectiles.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(settings.FPS)

        pygame.quit()
