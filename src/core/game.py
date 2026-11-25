
import pygame

from src.core import settings
from src.core.asset_manager import AssetManager
from src.entities.player import Player
from src.entities.enemies.enemy import Enemy
from src.systems.enemy_formation import EnemyFormation
from src.systems.enemy_spawner import EnemySpawner
from src.ui.hud import HUD
from src.systems.background import Background


class Game:
    def __init__(self):
        pygame.init()

        self.assets = AssetManager()

        self.screen = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )

        background_image = self.assets.load_image(
            "background_space",
            "sprites/backgrounds/background_space.png"
        )

        self.background = Background(
            background_image,
            settings.SCREEN_WIDTH,
            settings.SCREEN_HEIGHT,
            speed=1
        )


        pygame.display.set_caption(settings.SCREEN_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.score = 0
        self.hud = HUD(self)

        self.enemies = pygame.sprite.Group()
        self.enemy_projectiles = pygame.sprite.Group()

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
            ),
            "shooter": self.assets.load_image(
                "enemy_atirador",
                "sprites/enemies/atirador.png"
            )
        }

        blindado_frames = [
            self.assets.load_image(
                f"blindado_{i}",
                f"sprites/enemies/blindado/blindado_{i:02d}.png"
            )
            for i in range(1, 7)
        ]


        zigue_zague_frames = [
            self.assets.load_image(
                f"zigue_zague_{i}",
                f"sprites/enemies/zigue_zague/zigue_zague_{i:02d}.png"
            )
            for i in range(1, 7)
        ]


        perseguidor_frames = [
            self.assets.load_image(
                f"perseguidor_{i}",
                f"sprites/enemies/perseguidor/perseguidor_{i:02d}.png"
            )
            for i in range(1, 9)
        ]


        veloz_frames = [
            self.assets.load_image(
                f"veloz_{i}",
                f"sprites/enemies/veloz/veloz_{i:02d}.png"
            )
            for i in range(1, 7)
        ]


        player_projectile_frames = [
            self.assets.load_image(
                f"player_projectile_{i}",
                f"sprites/projectiles/player/tiro1/tiro_1_{i:02d}.png"
            )
            for i in range(1, 7)
        ]

        self.player = Player(self, 352, 500, player_projectile_frames)


        atirador_movement_frames = [
            self.assets.load_image(
                f"atirador_andar_{i}",
                f"sprites/enemies/atirador/andar/atirador_andar_{i:02d}.png"
            )
            for i in range(1, 7)
        ]

        atirador_shooting_frames = [
            self.assets.load_image(
                f"atirador_atirar_{i}",
                f"sprites/enemies/atirador/atirar/atirador_atirar_{i:02d}.png"
            )
            for i in range(1, 7)
        ]

        atirador_projectile_frames = [
            self.assets.load_image(
                f"atirador_projectile_{i}",
                f"sprites/projectiles/enemy/tiro_atirador/tiro_atirador_{i:02d}.png"
            )
            for i in range(1, 5)
        ]


        for name, image in enemy_images.items():
            scale = min(
                75 / image.get_width(),
                75 / image.get_height()
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
            blindado_frames,
            zigue_zague_frames,
            veloz_frames,
            perseguidor_frames,
            atirador_movement_frames,
            atirador_shooting_frames,
            atirador_projectile_frames
        )

        self.enemy_formation = EnemyFormation(self.enemies)


        for i, frame in enumerate(blindado_frames):
            scale = min(
                75 / frame.get_width(),
                75 / frame.get_height()
            )

            new_size = (
                round(frame.get_width() * scale),
                round(frame.get_height() * scale)
            )

            blindado_frames[i] = pygame.transform.scale(
                frame,
                new_size
            )


        for i, frame in enumerate(zigue_zague_frames):
            scale = min(
                75 / frame.get_width(),
                75 / frame.get_height()
            )

            new_size = (
                round(frame.get_width() * scale),
                round(frame.get_height() * scale)
            )

            zigue_zague_frames[i] = pygame.transform.scale(
                frame,
                new_size
            )


        for i, frame in enumerate(veloz_frames):
            scale = min(
                75 / frame.get_width(),
                75 / frame.get_height()
            )

            new_size = (
                round(frame.get_width() * scale),
                round(frame.get_height() * scale)
            )

            veloz_frames[i] = pygame.transform.scale(
                frame,
                new_size
            )


        for i, frame in enumerate(perseguidor_frames):
            scale = min(
                75 / frame.get_width(),
                75 / frame.get_height()
            )

            new_size = (
                round(frame.get_width() * scale),
                round(frame.get_height() * scale)
            )

            perseguidor_frames[i] = pygame.transform.scale(
                frame,
                new_size
            )


        for i, frame in enumerate(atirador_movement_frames):
            scale = min(
                75 / frame.get_width(),
                75 / frame.get_height()
            )

            new_size = (
                round(frame.get_width() * scale),
                round(frame.get_height() * scale)
            )

            atirador_movement_frames[i] = pygame.transform.scale(
                frame,
                new_size
            )


        for i, frame in enumerate(atirador_shooting_frames):
            scale = min(
                75 / frame.get_width(),
                75 / frame.get_height()
            )

            new_size = (
                round(frame.get_width() * scale),
                round(frame.get_height() * scale)
            )

            atirador_shooting_frames[i] = pygame.transform.scale(
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

        self.background.update()
        self.player.update()
        self.enemy_spawner.update()
        self.enemies.update()
        self.enemy_projectiles.update()
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


        projectile_collision = pygame.sprite.spritecollide(
            self.player,
            self.enemy_projectiles,
            True
        )

        if projectile_collision:
            self.player.take_damage()

    def draw(self):
        self.background.draw(self.screen)
        self.enemies.draw(self.screen)
        self.enemy_projectiles.draw(self.screen)
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
