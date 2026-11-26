
import cv2
import pygame


class VideoBackground:
    def __init__(self, path, width, height):
        self.width = width
        self.height = height

        self.video = cv2.VideoCapture(path)
        self.fps = self.video.get(cv2.CAP_PROP_FPS) or 30

        self.frame_duration = 1000 / self.fps
        self.last_frame_time = 0

        self.image = None

        self.update_frame()

    def update_frame(self):
        success, frame = self.video.read()

        if not success:
            self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            success, frame = self.video.read()

        if success:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            frame = pygame.surfarray.make_surface(
                frame.swapaxes(0, 1)
            )

            scale = max(
                self.width / frame.get_width(),
                self.height / frame.get_height()
            )

            new_size = (
                round(frame.get_width() * scale),
                round(frame.get_height() * scale)
            )

            frame = pygame.transform.scale(frame, new_size)

            crop_rect = pygame.Rect(
                0,
                0,
                self.width,
                self.height
            )

            crop_rect.center = frame.get_rect().center

            self.image = frame.subsurface(crop_rect).copy()

    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_frame_time >= self.frame_duration:
            self.update_frame()
            self.last_frame_time = current_time

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (0, 0))

    def stop(self):
        self.video.release()
