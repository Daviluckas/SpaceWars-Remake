
import pygame

from src.core import settings
from src.core.asset_manager import AssetManager
from src.entities.player import Player
from src.entities.enemies.enemy import Enemy
from src.systems.enemy_formation import EnemyFormation


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

        enemy_width = 40
        enemy_height = 40

        enemy_image = pygame.Surface((enemy_width, enemy_height))
        enemy_image.fill((255, 0, 0))

        formation_width = (
            settings.ENEMY_COLUMNS * enemy_width
            + (settings.ENEMY_COLUMNS - 1)
            * settings.ENEMY_HORIZONTAL_SPACING
        )

        start_x = (settings.SCREEN_WIDTH - formation_width) // 2

        for row in range(settings.ENEMY_ROWS):
            for column in range(settings.ENEMY_COLUMNS):
                x = start_x + column * (
                    enemy_width + settings.ENEMY_HORIZONTAL_SPACING
                )

                y = 80 + row * (
                    enemy_height + settings.ENEMY_VERTICAL_SPACING
                )

                enemy = Enemy(self, enemy_image, x, y)
                self.enemies.add(enemy)

        self.enemy_formation = EnemyFormation(self.enemies)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()

    def update(self):
        self.player.update()
        self.enemy_formation.update()
        self.handle_collisions()

    def handle_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.player.projectiles,
            self.enemies,
            True,
            False
        )

        for enemies_hit in collisions.values():
            for enemy in enemies_hit:
                enemy.take_damage()

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
