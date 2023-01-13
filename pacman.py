import pygame
from math import pi


class Pacman(pygame.sprite.Sprite):
    COLOR = "orange"

    def __init__(self, x, y, height, width, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.way_to = "None"
        self.current_way_to = "RIGHT"
        self.able_move = [1, 1, 1, 1]
        self.angle = 0
        self.delta_angle = 0.05
        self.speed = speed
        self.before_stop = "RIGHT"
        self.surface = pygame.Surface((self.rect.width, self.rect.height))
        self.mask = pygame.mask.from_surface(self.surface)

    def set_direction(self, event):
        if event.key == pygame.K_w:
            self.way_to = "UP"
        elif event.key == pygame.K_a:
            self.way_to = "LEFT"
        elif event.key == pygame.K_s:
            self.way_to = "DOWN"
        elif event.key == pygame.K_d:
            self.way_to = "RIGHT"

    def change_direction(self, field):
        if self.way_to == "UP" and self.able_move[0] == 1:
            self.rect.y -= self.speed * 10
            if not pygame.sprite.collide_mask(self, field):
                self.current_way_to = "UP"
                self.before_stop = "UP"
                self.way_to = 'None'
            self.rect.y += self.speed * 10
        elif self.way_to == "DOWN" and self.able_move[1] == 1:
            self.rect.y += self.speed * 10
            if not pygame.sprite.collide_mask(self, field):
                self.current_way_to = "DOWN"
                self.before_stop = "DOWN"
                self.way_to = 'None'
            self.rect.y -= self.speed * 10
        elif self.way_to == "LEFT" and self.able_move[2] == 1:
            self.rect.x -= self.speed * 10
            if not pygame.sprite.collide_mask(self, field):
                self.current_way_to = "LEFT"
                self.before_stop = "LEFT"
                self.way_to = 'None'
            self.rect.x += self.speed * 10
        elif self.way_to == "RIGHT" and self.able_move[3] == 1:
            self.rect.x += self.speed * 10
            if not pygame.sprite.collide_mask(self, field):
                self.current_way_to = "RIGHT"
                self.before_stop = "RIGHT"
                self.way_to = 'None'
            self.rect.x -= self.speed * 10

    def move(self, field):
        self.change_direction(field)
        if self.current_way_to == "UP":
            if not pygame.sprite.collide_mask(self, field):
                self.rect.y -= self.speed
            else:
                self.current_way_to = "STOP"
                self.before_stop = 'UP'
                self.rect.y += self.speed
        elif self.current_way_to == "DOWN":
            if not pygame.sprite.collide_mask(self, field):
                self.rect.y += self.speed
            else:
                self.current_way_to = "STOP"
                self.before_stop = "DOWN"
                self.rect.y -= self.speed
        elif self.current_way_to == "LEFT":
            if not pygame.sprite.collide_mask(self, field):
                self.rect.x -= self.speed
            else:
                self.current_way_to = 'STOP'
                self.before_stop = "LEFT"
                self.rect.x += self.speed

        elif self.current_way_to == "RIGHT":
            if not pygame.sprite.collide_mask(self, field):
                self.rect.x += self.speed
            else:
                self.current_way_to = "STOP"
                self.before_stop = "RIGHT"
                self.rect.x -= self.speed
        if self.delta_angle > 0 and self.angle >= pi / 3:
            self.delta_angle = -self.delta_angle
        elif self.delta_angle < 0 and self.angle <= 0:
            self.delta_angle = -self.delta_angle
        self.angle += self.delta_angle

    def draw(self, screen):

        if "LEFT" in self.before_stop:
            self.__draw_arc(screen,
                            start_angle=-pi + self.angle,
                            end_angle=pi - self.angle)
        elif "RIGHT" in self.before_stop:
            self.__draw_arc(screen,
                            start_angle=self.angle,
                            end_angle=2 * pi - self.angle)
        elif "UP" in self.before_stop:
            self.__draw_arc(screen,
                            start_angle=pi / 2 + self.angle,
                            end_angle=5 * pi / 2 - self.angle)
        elif "DOWN" in self.before_stop:
            self.__draw_arc(screen,
                            start_angle=-pi / 2 + self.angle,
                            end_angle=3 * pi / 2 - self.angle)

    def __draw_arc(self, screen, start_angle, end_angle):
        pygame.draw.arc(screen,
                        Pacman.COLOR,
                        [self.rect.x,
                         self.rect.y,
                         self.rect.width,
                         self.rect.height],
                        start_angle,
                        end_angle,
                        100)
