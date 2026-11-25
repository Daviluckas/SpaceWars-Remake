
class BaseBehavior:
    def update(self, enemy):
        raise NotImplementedError(
            "O comportamento precisa implementar o método update()."
        )

    def approach_player(self, enemy, speed):
        player = enemy.game.player

        if enemy.rect.centery < player.rect.centery:
            distance = player.rect.centery - enemy.rect.centery

            self.approach_remainder = (
                getattr(self, "approach_remainder", 0) + speed
            )

            movement = int(self.approach_remainder)
            movement = min(movement, distance)

            enemy.rect.y += movement
            self.approach_remainder -= movement
