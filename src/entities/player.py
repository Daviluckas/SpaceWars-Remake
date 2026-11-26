
import pygame

from src.core import settings
from src.entities.entity import Entity
from src.entities.projectile import Projectile
from src.systems.animation import Animation


class Player(Entity):
    def __init__(self, game, x, y, projectile_frames, thruster_frames):
        image = game.assets.load_image(
            "player",
            "sprites/player/player.png"
        )

        image = pygame.transform.scale(
            image,
            (settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT)
        )

        super().__init__(game, image, x, y)

        self.projectiles = pygame.sprite.Group()
        self.projectile_frames = projectile_frames
        self.lives = self.game.difficulty_config["lives"]
        self.destroyed = False

        self.thruster_animation = Animation(
            thruster_frames,
            frame_duration=80
        )

        self.is_moving = False


    def update(self):

        if self.destroyed:
            return
        
        keys = pygame.key.get_pressed()
        previous_position = self.rect.topleft

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= settings.PLAYER_SPEED

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += settings.PLAYER_SPEED

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= settings.PLAYER_SPEED

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += settings.PLAYER_SPEED

        self.rect.clamp_ip(
            pygame.Rect(0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )

        self.is_moving = self.rect.topleft != previous_position

        if self.is_moving:
            self.thruster_image = self.thruster_animation.update()
        else:
            self.thruster_image = None
            self.thruster_animation.current_frame = 0

        self.projectiles.update()


    def shoot(self):
        projectile = Projectile(
            self.game,
            self.rect.centerx - settings.PROJECTILE_WIDTH // 2,
            self.rect.top - settings.PROJECTILE_HEIGHT,
            self.projectile_frames
        )

        self.projectiles.add(projectile)

    def take_damage(self):
        self.lives -= 1

        if self.lives <= 0:
            self.destroyed = True