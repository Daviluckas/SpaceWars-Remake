
import random
import pygame

from src.core import settings
from src.entities.enemies.enemy import Enemy
from src.entities.enemies.behaviors.horizontal_behavior import HorizontalBehavior
from src.entities.enemies.behaviors.zigzag_behavior import ZigzagBehavior
from src.entities.enemies.behaviors.chase_behavior import ChaseBehavior


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

        behavior = self.choose_behavior()

        enemy = Enemy(self.game, self.image, x, y, behavior=behavior)
        self.enemies.add(enemy)


    def choose_behavior(self):
        behaviors = [
            HorizontalBehavior,
            ZigzagBehavior,
            ChaseBehavior
        ]

        behavior_class = random.choice(behaviors)

        return behavior_class()