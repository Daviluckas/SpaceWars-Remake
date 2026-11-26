
import random

from src.core import settings
from src.entities.enemies.behaviors.base_behavior import BaseBehavior


class ZigzagBehavior(BaseBehavior):
    def __init__(self):
        self.direction = random.choice([-1, 1])
        self.speed = random.randint(2, 4)
        self.vertical_direction = 1
        self.vertical_speed = random.randint(1, 3)
        self.approach_speed = 0.5
        self.change_direction_timer = 0
        self.change_direction_interval = random.randint(20, 45)

    def update(self, enemy):
        enemy.rect.x += self.speed * enemy.speed_multiplier * self.direction
        enemy.rect.y += self.vertical_speed * enemy.speed_multiplier * self.vertical_direction

        self.change_direction_timer += 1

        if self.change_direction_timer >= self.change_direction_interval:
            self.vertical_direction *= -1
            self.change_direction_timer = 0

        if enemy.rect.right >= settings.SCREEN_WIDTH:
            enemy.rect.right = settings.SCREEN_WIDTH
            self.direction = -1

        elif enemy.rect.left <= 0:
            enemy.rect.left = 0
            self.direction = 1

        self.approach_player(enemy, self.approach_speed * enemy.speed_multiplier)
