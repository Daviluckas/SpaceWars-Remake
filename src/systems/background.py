import pygame


class Background:
    def __init__(self, image, screen_width, screen_height, speed=1):
        self.image = pygame.transform.scale(
            image,
            (screen_width, screen_width * image.get_height() // image.get_width())
        )

        self.screen_height = screen_height
        self.speed = speed
        self.y = 0

    def update(self):
        self.y += self.speed

        if self.y >= self.image.get_height():
            self.y = 0

    def draw(self, screen):
        screen.blit(self.image, (0, self.y))
        screen.blit(
            self.image,
            (0, self.y - self.image.get_height())
        )