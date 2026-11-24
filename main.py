
import pygame

from src.core import settings


def main():
    pygame.init()

    screen = pygame.display.set_mode(
        (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
    )

    pygame.display.set_caption(settings.SCREEN_TITLE)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(settings.BLACK)

        pygame.display.flip()
        clock.tick(settings.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
