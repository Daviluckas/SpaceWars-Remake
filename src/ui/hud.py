import pygame

from src.core import settings


class HUD:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 28)

    def draw(self):
        lives_text = self.font.render(
            f"Vidas: {self.game.player.lives}",
            True,
            settings.WHITE
        )

        score_text = self.font.render(
            f"Pontuação: {self.game.score}",
            True,
            settings.WHITE
        )

        self.game.screen.blit(lives_text, (20, 15))

        self.game.screen.blit(
            score_text,
            (settings.SCREEN_WIDTH - score_text.get_width() - 20, 15)
        )