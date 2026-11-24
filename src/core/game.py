
import pygame

from src.core import settings
from src.core.asset_manager import AssetManager
from src.entities.player import Player
from src.entities.enemies.enemy import Enemy

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
        self.enemies = pygame.sprite.Group()
        
        enemy_image = pygame.Surface((40, 40))
        enemy_image.fill((255, 0, 0))

        enemy = Enemy(self, enemy_image, 380, 100)
        self.enemies.add(enemy)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()


    def update(self):
        self.player.update()
        self.enemies.update()

    def draw(self):
        self.screen.fill(settings.BLACK)
        self.enemies.draw(self.screen)
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
