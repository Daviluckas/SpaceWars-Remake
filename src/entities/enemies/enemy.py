
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
        animation_frames=None,
        shooting_frames=None
    ):
        super().__init__(game, image, x, y)

        self.health = health
        self.behavior = behavior if behavior is not None else HorizontalBehavior()

        self.movement_frames = animation_frames
        self.shooting_frames = shooting_frames

        self.animation = None
        self.shooting_animation = None
        self.is_shooting = False

        if self.movement_frames:
            self.animation = Animation(self.movement_frames)

    def start_shooting(self):
        if not self.shooting_frames or self.is_shooting:
            return

        self.shooting_animation = Animation(
            self.shooting_frames,
            loop=False
        )

        self.is_shooting = True

    def update(self):
        self.behavior.update(self)

        if self.is_shooting:
            self.image = self.shooting_animation.update()

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
