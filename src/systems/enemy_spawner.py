
import random
import pygame

from src.core import settings
from src.entities.enemies.enemy import Enemy
from src.entities.enemies.behaviors.horizontal_behavior import HorizontalBehavior
from src.entities.enemies.behaviors.zigzag_behavior import ZigzagBehavior
from src.entities.enemies.behaviors.chase_behavior import ChaseBehavior
from src.entities.enemies.behaviors.fast_behavior import FastBehavior


class EnemySpawner:
    def __init__(self, game, enemies, images, blindado_frames, zigue_zague_frames, veloz_frames, perseguidor_frames, atirador_movement_frames, atirador_shooting_frames, atirador_projectile_frames):
        self.game = game
        self.enemies = enemies
        self.images = images
        self.blindado_frames = blindado_frames
        self.zigue_zague_frames = zigue_zague_frames
        self.veloz_frames = veloz_frames
        self.perseguidor_frames = perseguidor_frames 
        self.atirador_movement_frames = atirador_movement_frames
        self.atirador_shooting_frames = atirador_shooting_frames
        self.atirador_projectile_frames = atirador_projectile_frames


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
        behavior, image, behavior_name = self.choose_behavior()

        x = random.randint(
            0,
            settings.SCREEN_WIDTH - image.get_width()
        )

        y = random.randint(50, 180)

        animation_frames = None
        shooting_frames = None

        if behavior_name == "horizontal":
            animation_frames = self.blindado_frames

        elif behavior_name == "zigzag":
            animation_frames = self.zigue_zague_frames

        elif behavior_name == "fast":
            animation_frames = self.veloz_frames

        elif behavior_name == "chase":
            animation_frames = self.perseguidor_frames

        elif behavior_name == "shooter":
            animation_frames = self.atirador_movement_frames
            shooting_frames = self.atirador_shooting_frames


        enemy = Enemy(
            self.game,
            image,
            x,
            y,
            behavior=behavior,
            animation_frames=animation_frames,
            shooting_frames=shooting_frames,
            projectile_frames=self.atirador_projectile_frames
        )

        self.enemies.add(enemy)

    def choose_behavior(self):
        behaviors = {
            "horizontal": HorizontalBehavior,
            "zigzag": ZigzagBehavior,
            "chase": ChaseBehavior,
            "fast": FastBehavior,
            "shooter": lambda: HorizontalBehavior(3, 4)
        }

        behavior_name = random.choice(list(behaviors.keys()))

        behavior = behaviors[behavior_name]()
        image = self.images[behavior_name]

        return behavior, image, behavior_name
