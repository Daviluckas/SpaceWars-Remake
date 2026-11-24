from src.core import settings


class EnemyFormation:
    def __init__(self, enemies):
        self.enemies = enemies
        self.direction = 1

    def update(self):
        if not self.enemies:
            return

        for enemy in self.enemies:
            enemy.rect.x += settings.ENEMY_SPEED * self.direction

        formation_right = max(
            enemy.rect.right for enemy in self.enemies
        )

        formation_left = min(
            enemy.rect.left for enemy in self.enemies
        )

        if formation_right >= settings.SCREEN_WIDTH:
            self.direction = -1
            self.move_down()

        elif formation_left <= 0:
            self.direction = 1
            self.move_down()

    def move_down(self):
        for enemy in self.enemies:
            enemy.rect.y += settings.ENEMY_DESCENT