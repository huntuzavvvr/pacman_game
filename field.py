import os
import sys
import pygame
from pacman import Pacman
from view_lvl import Level, pix_size
import numpy as np


pygame.init()
PAC_SIZE = 224, 248
scale = 2
size = width, height = PAC_SIZE[0] * scale, PAC_SIZE[1] * scale + 80
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
angle = 0
pacman = Pacman(208, 316, 24, 24, 1)

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = pygame.Color('black')
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def func_big_orb():
    print('столкновение 1')


def func_small_orb():
    print('столкновение')


class Field(pygame.sprite.Sprite):
    im = load_image("pac_pix.png", colorkey=-1)
    im = im.subsurface(pygame.Rect(228, 0, *PAC_SIZE))
    back_ground = pygame.transform.scale(im, (PAC_SIZE[0] * scale, PAC_SIZE[1] * scale))

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Field.back_ground
        self.mask = pygame.mask.from_surface(self.back_ground)
        self.rect = self.image.get_rect()
        self.rect.top = 48
        self.rect.left = 0


class Orb(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__(all_sprites)
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.top = 48 + x * pix_size[0] * scale
        self.rect.left = 0 + y * pix_size[1] * scale

    def on_touch(self):
        pass

    def set_on_touch(self, func):
        self.on_touch = func

    def update(self):
        if pygame.sprite.collide_mask(self, pacman):
            self.on_touch()
            self.kill()


if __name__ == '__main__':
    clock = pygame.time.Clock()
    lvl = Level()
    field = Field()
    lvl.new_lvl()
    lst_color_walls = [pygame.Color(71, 183, 174, 0), pygame.Color(255, 183, 255, 0)]
    lvl.lst_color_walls.append(lst_color_walls)
    field.image = lvl.get_image_walls()
    field.mask = pygame.mask.from_surface(field.image)

    image_orb = load_image("pac_pix.png", colorkey=-1).subsurface(pygame.Rect(8, 8, *pix_size))
    image_big_orb = load_image("pac_pix.png", colorkey=-1).subsurface(pygame.Rect(8, 24, *pix_size))
    image_orb = pygame.transform.scale(image_orb, (pix_size[0] * scale, pix_size[1] * scale))
    image_big_orb = pygame.transform.scale(image_big_orb, (pix_size[0] * scale, pix_size[1] * scale))

    level = np.rot90(lvl.lvl, -1)

    n = 0

    for i in range(len(level)):
        for j in range(len(level[0])):
            if level[i, j] == 0:
                n += 1
                new_orb = Orb(image_orb, i, j)
                new_orb.set_on_touch(func_small_orb)
            if level[i, j] == 5:
                new_orb = Orb(image_big_orb, i, j)
                new_orb.set_on_touch(func_big_orb)
    print(n)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                pacman.set_direction(event)
        screen.fill((0, 0, 0))
        pacman.move(field)
        pacman.draw(screen)
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(100)