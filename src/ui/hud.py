
import pygame

from src.core import settings


class HUD:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 28)

        difficulty = self.game.selected_difficulty

        frame_count = {
            "easy": 6,
            "medium": 4,
            "hard": 2
        }

        self.life_frames = [
            self.game.assets.load_image(
                f"life_{difficulty}_{i}",
                f"sprites/lives/life_{difficulty}_{i}.png"
            )
            for i in range(1, frame_count[difficulty] + 1)
        ]

    def draw(self):
        life_frame = self.life_frames[
            len(self.life_frames) - 1 - self.game.player.lives
        ]

        self.game.screen.blit(life_frame, (20, 15))

        score_text = self.font.render(
            f"Pontuação: {self.game.score}",
            True,
            settings.WHITE
        )

        self.game.screen.blit(
            score_text,
            (settings.SCREEN_WIDTH - score_text.get_width() - 20, 15)
        )
