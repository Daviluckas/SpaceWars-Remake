
import pygame

from src.core import settings


class HUD:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 16)
        self.score_medal = self.game.assets.load_image("score_medal", "sprites/score_medal.png")

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
            str(self.game.score),
            True,
            (252, 211, 77)
        )

        medal = pygame.transform.scale(
            self.score_medal,
            (36, 36)
        )

        score_x = settings.SCREEN_WIDTH - score_text.get_width() - 65

        self.game.screen.blit(medal, (score_x, 10))
        self.game.screen.blit(score_text, (score_x + 36, 21))
