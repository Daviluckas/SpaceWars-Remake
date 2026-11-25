
import math

from src.entities.enemies.behaviors.base_behavior import BaseBehavior


class ChaseBehavior(BaseBehavior):
    def __init__(self):
        self.speed = 2.5

    def update(self, enemy):
        player = enemy.game.player

        dx = player.rect.centerx - enemy.rect.centerx
        dy = player.rect.centery - enemy.rect.centery

        distance = math.hypot(dx, dy)

        if distance == 0:
            return

        enemy.rect.x += round(dx / distance * self.speed)
        enemy.rect.y += round(dy / distance * self.speed)
