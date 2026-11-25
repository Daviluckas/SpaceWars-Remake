
from src.entities.entity import Entity
from src.entities.enemies.behaviors.horizontal_behavior import HorizontalBehavior
from src.systems.animation import Animation


class Enemy(Entity):
    def __init__(
        self,
        game,
        image,
        x,
        y,
        health=1,
        behavior=None,
        animation_frames=None
    ):
        super().__init__(game, image, x, y)

        self.health = health
        self.behavior = behavior if behavior is not None else HorizontalBehavior()

        self.animation = None

        if animation_frames:
            self.animation = Animation(animation_frames)

    def update(self):
        self.behavior.update(self)

        if self.animation:
            self.image = self.animation.update()

    def take_damage(self, damage=1):
        self.health -= damage

        if self.health <= 0:
            self.kill()
            return True

        return False
