
import random
import pygame

from src.core import settings
from src.entities.enemies.enemy import Enemy


class EnemySpawner:
    def __init__(self, game, enemies, image):
        self.game = game
        self.enemies = enemies
        self.image = image

        self.spawn_interval = random.randint(
            settings.ENEMY_SPAWN_MIN_INTERVAL,
            settings.ENEMY_SPAWN_MAX_INTERVAL
        )

        self.last_spawn_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_spawn_time >= self.spawn_interval:
            self.spawn_enemy()

            self.last_spawn_time = current_time

            self.spawn_interval = random.randint(
                settings.ENEMY_SPAWN_MIN_INTERVAL,
                settings.ENEMY_SPAWN_MAX_INTERVAL
            )

    def spawn_enemy(self):
        x = random.randint(
            0,
            settings.SCREEN_WIDTH - self.image.get_width()
        )

        y = random.randint(50, 180)

        enemy = Enemy(self.game, self.image, x, y)
        self.enemies.add(enemy)
