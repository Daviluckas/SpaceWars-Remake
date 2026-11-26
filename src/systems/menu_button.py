
import pygame


class MenuButton:
    def __init__(self, normal, hover, pressed, x, y):
        self.images = {
            "normal": normal,
            "hover": hover,
            "pressed": pressed
        }

        self.image = self.images["normal"]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.hovered = False
        self.pressed = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.pressed = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            clicked = self.pressed and self.rect.collidepoint(event.pos)
            self.pressed = False
            return clicked

        return False

    def update(self):
        self.hovered = self.rect.collidepoint(
            pygame.mouse.get_pos()
        )

        if self.pressed and self.hovered:
            self.image = self.images["pressed"]
        elif self.hovered:
            self.image = self.images["hover"]
        else:
            self.image = self.images["normal"]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
