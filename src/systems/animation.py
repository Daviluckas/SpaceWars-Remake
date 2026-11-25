
import pygame


class Animation:
    def __init__(self, frames, frame_duration=120, loop=True):
        self.frames = frames
        self.frame_duration = frame_duration
        self.loop = loop
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.finished = False

    def update(self):
        if self.finished:
            return self.frames[self.current_frame]

        current_time = pygame.time.get_ticks()

        if current_time - self.last_update >= self.frame_duration:
            self.last_update = current_time

            if self.current_frame < len(self.frames) - 1:
                self.current_frame += 1
            elif self.loop:
                self.current_frame = 0
            else:
                self.finished = True

        return self.frames[self.current_frame]
