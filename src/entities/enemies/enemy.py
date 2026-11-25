
from src.entities.entity import Entity
from src.entities.enemies.behaviors.horizontal_behavior import HorizontalBehavior


class Enemy(Entity):
    def __init__(self, game, image, x, y, health=1, behavior=None):
        super().__init__(game, image, x, y)

        self.health = health
        self.behavior = behavior if behavior is not None else HorizontalBehavior()

    def update(self):
        self.behavior.update(self)

    def take_damage(self, damage=1):
        self.health -= damage

        if self.health <= 0:
            self.kill()
            return True

        return False
