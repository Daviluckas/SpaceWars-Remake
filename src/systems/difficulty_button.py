import pygame


class DifficultyButton:
    def __init__(self, frames, x, y, frame_duration=150):
        self.frames = frames

        self.state = "base"
        self.frame_index = 0
        self.image = self.frames[self.state][0]

        self.rect = self.image.get_rect(topleft=(x, y))

        self.frame_duration = frame_duration
        self.last_frame_time = pygame.time.get_ticks()

        self.hovered = False
        self.pressed = False
        self.press_animation = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.pressed = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            clicked = self.pressed and self.rect.collidepoint(event.pos)

            if clicked:
                self.state = "press"
                self.frame_index = 0
                self.image = self.frames["press"][0]
                self.press_animation = True
                self.last_frame_time = pygame.time.get_ticks()

            self.pressed = False
            return clicked

        return False

    def update(self):
        current_time = pygame.time.get_ticks()

        if self.press_animation:
            if current_time - self.last_frame_time >= self.frame_duration:
                if self.frame_index < len(self.frames["press"]) - 1:
                    self.frame_index += 1
                    self.image = self.frames["press"][self.frame_index]
                    self.last_frame_time = current_time
                else:
                    self.press_animation = False

                    self.state = "hover" if self.hovered else "base"
                    self.frame_index = 0
                    self.image = self.frames[self.state][0]
                    self.last_frame_time = current_time

            return

        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())

        if self.pressed and self.hovered:
            new_state = "press"
        elif self.hovered:
            new_state = "hover"
        else:
            new_state = "base"

        if new_state != self.state:
            self.state = new_state
            self.frame_index = 0
            self.image = self.frames[self.state][0]
            self.last_frame_time = current_time

        if current_time - self.last_frame_time >= self.frame_duration:
            total_frames = len(self.frames[self.state])

            self.frame_index = (self.frame_index + 1) % total_frames
            self.image = self.frames[self.state][self.frame_index]

            self.last_frame_time = current_time

    def draw(self, screen):
        screen.blit(self.image, self.rect)