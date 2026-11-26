
import pygame

from assets.sprites.screens.main_menu import MainMenu


def main():
    pygame.init()

    menu = MainMenu()
    menu.run()

    pygame.quit()


if __name__ == "__main__":
    main()
