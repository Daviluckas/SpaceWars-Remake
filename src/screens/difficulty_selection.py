from pathlib import Path

import pygame

from src.core import settings
from src.core.asset_manager import AssetManager
from src.systems.difficulty_button import DifficultyButton


ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"


class DifficultySelection:
    def __init__(self, selected_difficulty="medium"):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.running = True


        self.assets = AssetManager()

        self.background_frames = {}
        self.load_backgrounds()
        self.load_buttons()
        self.create_buttons()


        self.selected_difficulty = selected_difficulty
        self.background_index = 0

        self.frame_duration = 150
        self.last_frame_time = pygame.time.get_ticks()

    def load_backgrounds(self):
        difficulties = ["easy", "medium", "hard"]

        for difficulty in difficulties:
            self.background_frames[difficulty] = []

            for i in range(1, 5):
                frame = self.assets.load_image(
                    f"bg_{difficulty}_frame_{i}",
                    f"sprites/screens/difficulty/backgrounds/{difficulty}/bg_{difficulty}_frame_{i}.png"
                )

                frame = pygame.transform.scale(
                    frame,
                    (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
                )

                self.background_frames[difficulty].append(frame)

    def update_background(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_frame_time >= self.frame_duration:
            self.background_index = (
                self.background_index + 1
            ) % len(self.background_frames[self.selected_difficulty])

            self.last_frame_time = current_time


    def draw_background(self):
        frame = self.background_frames[self.selected_difficulty][
            self.background_index
        ]

        self.screen.blit(frame, (0, 0))


    def load_buttons(self):
        self.button_frames = {}

        difficulties = ["easy", "medium", "hard"]

        for difficulty in difficulties:
            self.button_frames[difficulty] = {
                "base": [],
                "hover": [],
                "press": []
            }

            for state, total_frames in [
                ("base", 4),
                ("hover", 2),
                ("press", 2)
            ]:
                for i in range(1, total_frames + 1):
                    frame = self.assets.load_image(
                        f"btn_{difficulty}_{state}_{i}",
                        f"sprites/screens/difficulty/buttons/{difficulty}/btn_{difficulty}_{state}_{i}.png"
                    )

                    frame = pygame.transform.smoothscale(
                        frame,
                        (
                            int(frame.get_width() * 1.15),
                            int(frame.get_height() * 1.15)
                        )
                    )
                    
                    self.button_frames[difficulty][state].append(frame)

    def create_buttons(self):
        difficulties = ["easy", "medium", "hard"]
        gap = 30

        button_widths = [
            self.button_frames[difficulty]["base"][0].get_width()
            for difficulty in difficulties
        ]

        total_width = sum(button_widths) + gap * 2
        current_x = (settings.SCREEN_WIDTH - total_width) // 2

        button_height = max(
            self.button_frames[difficulty]["base"][0].get_height()
            for difficulty in difficulties
        )

        button_y = (settings.SCREEN_HEIGHT - button_height) // 2

        self.buttons = {}

        for difficulty in difficulties:
            self.buttons[difficulty] = DifficultyButton(
                self.button_frames[difficulty],
                current_x,
                button_y
            )

            current_x += self.button_frames[difficulty]["base"][0].get_width() + gap


    def update_buttons(self):
        for button in self.buttons.values():
            button.update()


    def draw_buttons(self):
        for button in self.buttons.values():
            button.draw(self.screen)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

            for difficulty, button in self.buttons.items():
                if button.handle_event(event):
                    self.selected_difficulty = difficulty
                    self.background_index = 0
                    self.last_frame_time = pygame.time.get_ticks()


    def update(self):
        self.update_background()
        self.update_buttons()


    def draw(self):
        self.draw_background()
        self.draw_buttons()

        pygame.display.flip()   


    def run(self):
      while self.running:
          self.handle_events()
          self.update()
          self.draw()

          self.clock.tick(settings.FPS)