from src.core import settings
from src.entities.entity import Entity


class Enemy(Entity):
    def __init__(self, game, image, x, y, health=1):
        super().__init__(game, image, x, y)

        self.health = health
        self.direction = 1

    def update(self):
        self.rect.x += settings.ENEMY_SPEED * self.direction

        if self.rect.right >= settings.SCREEN_WIDTH:
            self.direction = -1
            self.rect.y += settings.ENEMY_DESCENT

        elif self.rect.left <= 0:
            self.direction = 1
            self.rect.y += settings.ENEMY_DESCENT

    def take_damage(self, damage=1):
        self.health -= damage

        if self.health <= 0:
            self.kill()