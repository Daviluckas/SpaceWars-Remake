
import pygame

from src.core import settings
from src.core.asset_manager import AssetManager
from src.entities.player import Player
from src.entities.enemies.enemy import Enemy
from src.systems.enemy_formation import EnemyFormation
from src.systems.enemy_spawner import EnemySpawner
from src.ui.hud import HUD


class Game:
    def __init__(self):
        pygame.init()

        self.assets = AssetManager()

        self.screen = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )

        pygame.display.set_caption(settings.SCREEN_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.score = 0
        self.hud = HUD(self)

        self.player = Player(self, 352, 500)
        self.enemies = pygame.sprite.Group()

        enemy_images = {
            "horizontal": self.assets.load_image(
                "enemy_blindado",
                "sprites/enemies/blindado.png"
            ),
            "zigzag": self.assets.load_image(
                "enemy_zigue_zague",
                "sprites/enemies/zigue_zague.png"
            ),
            "fast": self.assets.load_image(
                "enemy_veloz",
                "sprites/enemies/veloz.png"
            ),
            "chase": self.assets.load_image(
                "enemy_perseguidor",
                "sprites/enemies/perseguidor.png"
            )
        }

        blindado_frames = [
            self.assets.load_image(
                f"blindado_{i}",
                f"sprites/enemies/blindado/blindado_{i:02d}.png"
            )
            for i in range(1, 7)
        ]


        for name, image in enemy_images.items():
            scale = min(
                64 / image.get_width(),
                64 / image.get_height()
            )

            new_size = (
                round(image.get_width() * scale),
                round(image.get_height() * scale)
            )

            enemy_images[name] = pygame.transform.scale(
                image,
                new_size
            )

        self.enemy_spawner = EnemySpawner(
            self,
            self.enemies,
            enemy_images,
            blindado_frames
        )

        self.enemy_formation = EnemyFormation(self.enemies)


        for i, frame in enumerate(blindado_frames):
            scale = min(
                64 / frame.get_width(),
                64 / frame.get_height()
            )

            new_size = (
                round(frame.get_width() * scale),
                round(frame.get_height() * scale)
            )

            blindado_frames[i] = pygame.transform.scale(
                frame,
                new_size
            )


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()

    def update(self):
        if self.game_over:
            return

        self.player.update()
        self.enemy_spawner.update()
        self.enemies.update()
        self.handle_collisions()

        if self.player.lives <= 0:
            self.game_over = True

    def handle_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.player.projectiles,
            self.enemies,
            True,
            False
        )

        for enemies_hit in collisions.values():
            for enemy in enemies_hit:
                if enemy.take_damage():
                    self.score += settings.ENEMY_SCORE

        player_collision = pygame.sprite.spritecollide(
            self.player,
            self.enemies,
            True
        )

        if player_collision:
            self.player.take_damage()

    def draw(self):
        self.screen.fill(settings.BLACK)
        self.enemies.draw(self.screen)
        self.player.projectiles.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        self.hud.draw()

        if self.game_over:
            self.draw_game_over()

        pygame.display.flip()

    def draw_game_over(self):
        font = pygame.font.Font(None, 72)

        game_over_text = font.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )

        text_rect = game_over_text.get_rect(
            center=(
                settings.SCREEN_WIDTH // 2,
                settings.SCREEN_HEIGHT // 2
            )
        )

        self.screen.blit(game_over_text, text_rect)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(settings.FPS)

        pygame.quit()
