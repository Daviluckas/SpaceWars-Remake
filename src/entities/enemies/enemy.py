
import pygame

from src.entities.entity import Entity
from src.entities.enemies.behaviors.horizontal_behavior import HorizontalBehavior
from src.systems.animation import Animation
from src.entities.enemy_projectile import EnemyProjectile


class Enemy(Entity):
    def __init__(
        self,
        game,
        image,
        x,
        y,
        health=1,
        behavior=None,
        animation_frames=None,
        shooting_frames=None,
        projectile_frames=None
    ):
        super().__init__(game, image, x, y)

        self.health = health
        self.behavior = behavior if behavior is not None else HorizontalBehavior()

        self.movement_frames = animation_frames
        self.shooting_frames = shooting_frames
        self.projectile_frames = projectile_frames

        self.animation = None
        self.shooting_animation = None
        self.is_shooting = False
        self.has_shot = False
        self.projectile_timer = pygame.time.get_ticks()
        self.projectile_interval = 2500

        if self.movement_frames:
            self.animation = Animation(self.movement_frames)

    def start_shooting(self):
        if not self.shooting_frames or self.is_shooting:
            return

        self.shooting_animation = Animation(
            self.shooting_frames,
            loop=False
        )
        self.has_shot = False
        self.is_shooting = True


    def shoot(self):
        if not self.projectile_frames:
            return

        projectile = EnemyProjectile(
            self.game,
            self.rect.centerx,
            self.rect.centery,
            self.projectile_frames,
            self.game.player
        )

        self.game.enemy_projectiles.add(projectile)

    def update(self):
        self.behavior.update(self)

        current_time = pygame.time.get_ticks()

        if (
            self.shooting_frames
            and not self.is_shooting
            and current_time - self.projectile_timer >= self.projectile_interval
        ):
            self.start_shooting()
            self.projectile_timer = current_time

        if self.is_shooting:
            self.image = self.shooting_animation.update()

            if self.shooting_animation.current_frame == 2 and not self.has_shot:
                self.shoot()
                self.has_shot = True

            if self.shooting_animation.finished:
                self.is_shooting = False
                self.shooting_animation = None
                self.animation = Animation(self.movement_frames)

        elif self.animation:
            self.image = self.animation.update()

    def take_damage(self, damage=1):
        self.health -= damage

        if self.health <= 0:
            self.kill()
            return True

        return False
