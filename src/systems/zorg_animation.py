import pygame


class ZorgAnimation:
    def __init__(self, frames, x, y, frame_duration=150):
        self.frames = frames
        self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.frame_duration = frame_duration
        self.last_frame_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_frame_time >= self.frame_duration:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]
            self.last_frame_time = current_time

    def draw(self, screen):
        screen.blit(self.image, self.rect)