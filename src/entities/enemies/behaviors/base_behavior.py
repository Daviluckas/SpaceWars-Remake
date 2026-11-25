
class BaseBehavior:
    def update(self, enemy):
        raise NotImplementedError(
            "O comportamento precisa implementar o método update()."
        )

    def approach_player(self, enemy, speed):
        player = enemy.game.player

        distance = player.rect.centery - enemy.rect.centery

        if distance == 0:
            return

        direction = 1 if distance > 0 else -1

        remainder = getattr(self, "approach_remainder", 0)

        if remainder * direction < 0:
            remainder = 0

        remainder += speed

        movement = min(int(remainder), abs(distance))

        enemy.rect.y += movement * direction

        self.approach_remainder = remainder - movement
