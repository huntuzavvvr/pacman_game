from generation_lvl import generation_lvl
import numpy as np
import pygame


scale = 2
pix_size = 8, 8
screen_size = 224, 288
pygame.init()
screen = pygame.display.set_mode((screen_size[0] * scale, screen_size[1] * scale))
all_sprites = pygame.sprite.Group()


def rot90_pix_ar(_pix_ar: pygame.PixelArray, position=1):
    if position % 4 == 1:
        _pix_ar1 = pygame.PixelArray(pygame.Surface([_pix_ar.shape[1], _pix_ar.shape[0]]))
        for _i in range(_pix_ar.shape[1]):
            for j in range(_pix_ar.shape[0]):
                _pix_ar1[_i, j] = _pix_ar[j, _pix_ar.shape[1] - _i - 1]
    elif position % 4 == 2:
        _pix_ar1 = pygame.PixelArray(pygame.Surface([*_pix_ar.shape]))
        for _i in range(_pix_ar.shape[0]):
            for j in range(_pix_ar.shape[1]):
                _pix_ar1[_i, j] = _pix_ar[_pix_ar.shape[0] - _i - 1, _pix_ar.shape[1] - j - 1]
    elif position % 4 == 3:
        _pix_ar1 = pygame.PixelArray(pygame.Surface([_pix_ar.shape[1], _pix_ar.shape[0]]))
        for _i in range(_pix_ar.shape[1]):
            for j in range(_pix_ar.shape[0]):
                _pix_ar1[_i, j] = _pix_ar[_pix_ar.shape[0] - j - 1, _i]
    else:
        _pix_ar1 = _pix_ar

    return _pix_ar1


def change_pix_ar(_neigh_pixels, _pix_arr_cell: pygame.PixelArray, color: pygame.Color = pygame.Color(0, 0, 0, 0)):
    _copy_neigh_pixels = _neigh_pixels == 2

    for position in range(3, -1, -1):
        _copy_neigh_pixels = np.rot90(_copy_neigh_pixels, 1)
        _pix_arr_cell = rot90_pix_ar(_pix_arr_cell, 1)

        if not _copy_neigh_pixels[0, 1]:
            _pix_arr_cell[2, 2] = color
            _pix_arr_cell[2, 3] = color
            _pix_arr_cell[2, 4] = color
            _pix_arr_cell[2, 5] = color

            if _copy_neigh_pixels[0, 0]:
                _pix_arr_cell[2, 0] = color
                _pix_arr_cell[2, 1] = color

            if _copy_neigh_pixels[0, 2]:
                _pix_arr_cell[2, 6] = color
                _pix_arr_cell[2, 7] = color

        else:
            if not _copy_neigh_pixels[0, 0]:
                _pix_arr_cell[2, 2] = color
                _pix_arr_cell[1, 2] = color
                _pix_arr_cell[0, 2] = color
            if not _copy_neigh_pixels[0, 2]:
                _pix_arr_cell[2, 5] = color
                _pix_arr_cell[1, 5] = color
                _pix_arr_cell[0, 5] = color

    return _pix_arr_cell


class Level:
    def __init__(self):
        self.width, self.height = 28, 31
        self.lvl = np.array(np.ones(self.width * self.height).reshape((self.width, self.height)), dtype='int8')
        self.size = 224, 248
        self.lst_color_walls: list[list[pygame.Color]] = []

    def new_lvl(self, view_print=False):
        self.lvl = np.rot90(generation_lvl(view_print=view_print))

    def get_image_walls(self, im_pack=0):

        pix_arr = pygame.PixelArray(pygame.Surface([*self.size]))

        ls_fail_type_pix = []

        for i in range(self.width):
            for j in range(self.height):
                if self.lvl[i, j] == 2:
                    pix_arr_cell = pygame.PixelArray(pygame.Surface(pix_size))

                    neigh_pixels = np.zeros(9).reshape(3, 3)

                    for x in range(3):
                        for y in range(3):
                            if 0 <= i + x - 1 < self.lvl.shape[0] and 0 <= j + y - 1 < self.lvl.shape[1]:
                                neigh_pixels[x, y] = self.lvl[i + x - 1, j + y - 1]

                    pix_arr_cell = change_pix_ar(neigh_pixels, pix_arr_cell, color=self.lst_color_walls[im_pack][0])

                    for x in range(pix_size[0]):
                        for y in range(pix_size[1]):
                            pix_arr[i * pix_size[0] + x, j * pix_size[1] + y] = pix_arr_cell[x, y]
                elif self.lvl[i, j] == 4:
                    for x in range(pix_size[0]):
                        for y in range(2):
                            pix_arr[i * pix_size[0] + x, j * pix_size[1] + y + 3] = self.lst_color_walls[im_pack][1]

        im = pygame.transform.scale(pix_arr.surface, (self.size[0] * scale, self.size[1] * scale))
        im.set_colorkey(pygame.Color('black'))
        return im


if __name__ == '__main__':
    clock = pygame.time.Clock()

    lvl = Level()
    lvl.new_lvl()

    lst_color_walls = [pygame.Color(255, 0, 0, 0), pygame.Color(0, 0, 255, 0)]

    lvl.lst_color_walls.append(lst_color_walls)

    sprite = pygame.sprite.Sprite()

    sprite.image = lvl.get_image_walls()
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 0
    sprite.rect.y = 0
    all_sprites.add(sprite)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(50)
