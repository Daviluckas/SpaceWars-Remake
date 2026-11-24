
from src.entities.entity import Entity


class Player(Entity):
    def __init__(self, game, x, y):
        image = game.assets.load_image(
            "player",
            "sprites/player/player.png"
        )

        super().__init__(game, image, x, y)
