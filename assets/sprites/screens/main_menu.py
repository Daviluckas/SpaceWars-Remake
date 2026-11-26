
from pathlib import Path

import pygame
from pygame import event

from src.core import settings
from src.systems.video_background import VideoBackground
from src.core.asset_manager import AssetManager
from src.systems.menu_button import MenuButton
from src.systems.zorg_animation import ZorgAnimation
from src.screens.difficulty_selection import DifficultySelection


ASSETS_DIR = Path(__file__).resolve().parents[3] / "assets"


class MainMenu:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )

        pygame.display.set_caption(settings.SCREEN_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        self.background = VideoBackground(
            str(ASSETS_DIR / "videos" / "menu" / "background_menu.mp4"),
            settings.SCREEN_WIDTH,
            settings.SCREEN_HEIGHT
        )

        self.assets = AssetManager()

        self.load_zorg_frames()
        self.zorg = ZorgAnimation(
            self.zorg_frames,
            settings.SCREEN_WIDTH - 320 - 40,
            400
        )

        self.load_buttons()
        self.create_buttons()

    def handle_events(self):
        for event in pygame.event.get():
            for name, button in self.buttons.items():
                if button.handle_event(event):
                    if name == "opcoes":
                        self.difficulty_selection = DifficultySelection()
                        self.difficulty_selection.run()

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False


    def load_buttons(self):
        buttons_path = "sprites/menu/buttons"

        self.buttons_images = {
            "jogar": {
                "normal": self.assets.load_image(
                    "btn_jogar_normal",
                    f"{buttons_path}/jogar/btn_jogar_normal.png"
                ),
                "hover": self.assets.load_image(
                    "btn_jogar_hover",
                    f"{buttons_path}/jogar/btn_jogar_hover.png"
                ),
                "pressed": self.assets.load_image(
                    "btn_jogar_pressed",
                    f"{buttons_path}/jogar/btn_jogar_pressed.png"
                )
            },
            "opcoes": {
                "normal": self.assets.load_image(
                    "btn_opcoes_normal",
                    f"{buttons_path}/opcoes/btn_opcoes_normal.png"
                ),
                "hover": self.assets.load_image(
                    "btn_opcoes_hover",
                    f"{buttons_path}/opcoes/btn_opcoes_hover.png"
                ),
                "pressed": self.assets.load_image(
                    "btn_opcoes_pressed",
                    f"{buttons_path}/opcoes/btn_opcoes_pressed.png"
                )
            },
            "sobre": {
                "normal": self.assets.load_image(
                    "btn_sobre_normal",
                    f"{buttons_path}/sobre/btn_sobre_normal.png"
                ),
                "hover": self.assets.load_image(
                    "btn_sobre_hover",
                    f"{buttons_path}/sobre/btn_sobre_hover.png"
                ),
                "pressed": self.assets.load_image(
                    "btn_sobre_pressed",
                    f"{buttons_path}/sobre/btn_sobre_pressed.png"
                )
            }
        }


    def create_buttons(self):
            button_x = 80
    
            self.buttons = {
                "jogar": MenuButton(
                    self.buttons_images["jogar"]["normal"],
                    self.buttons_images["jogar"]["hover"],
                    self.buttons_images["jogar"]["pressed"],
                    button_x,
                    330
                ),
                "opcoes": MenuButton(
                    self.buttons_images["opcoes"]["normal"],
                    self.buttons_images["opcoes"]["hover"],
                    self.buttons_images["opcoes"]["pressed"],
                    button_x,
                    410
                ),
                "sobre": MenuButton(
                    self.buttons_images["sobre"]["normal"],
                    self.buttons_images["sobre"]["hover"],
                    self.buttons_images["sobre"]["pressed"],
                    button_x,
                    490
                )
            }


    def load_zorg_frames(self):
        self.zorg_frames = []

        for i in range(1, 9):
            frame = self.assets.load_image(
                f"zorg_panel_frame_{i}",
                f"sprites/menu/zorg-9000/zorg_panel_frame_{i}.png"
            )

            self.zorg_frames.append(frame)


    def update(self):
        self.background.update()

        for button in self.buttons.values():
            button.update()

        self.zorg.update()


    def draw(self):
        self.background.draw(self.screen)

        for button in self.buttons.values():
            button.draw(self.screen)

        self.zorg.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(settings.FPS)

        self.background.stop()
