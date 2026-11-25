
import random

from src.core import settings
from src.entities.enemies.behaviors.base_behavior import BaseBehavior


class FastBehavior(BaseBehavior):
    def __init__(self):
        self.direction = random.choice([-1, 1])
        self.speed = random.randint(5, 7)
        self.approach_speed = 1.5

    def update(self, enemy):
        enemy.rect.x += self.speed * self.direction

        if enemy.rect.right >= settings.SCREEN_WIDTH:
            enemy.rect.right = settings.SCREEN_WIDTH
            self.direction = -1

        elif enemy.rect.left <= 0:
            enemy.rect.left = 0
            self.direction = 1

        self.approach_player(enemy, self.approach_speed)
