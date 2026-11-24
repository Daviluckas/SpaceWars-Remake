from src.entities.entity import Entity


class Enemy(Entity):
    def __init__(self, game, image, x, y, health=1):
        super().__init__(game, image, x, y)

        self.health = health

    def take_damage(self, damage=1):
        self.health -= damage

        if self.health <= 0:
            self.kill()