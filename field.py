import os
import sys
import pygame


pygame.init()
PAC_SIZE = 224, 248
scale = 2
size = width, height = PAC_SIZE[0] * scale, PAC_SIZE[1] * scale + 80
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = pygame.Color('black')
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Field(pygame.sprite.Sprite):
    im = load_image("pac_pix.png", color_key=-1)
    im = im.subsurface(pygame.Rect(228, 0, *PAC_SIZE))
    back_ground = pygame.transform.scale(im, (PAC_SIZE[0] * scale, PAC_SIZE[1] * scale))

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Field.back_ground
        self.mask = pygame.mask.from_surface(self.back_ground)
        self.rect = self.image.get_rect()
        self.rect.top = 48
        self.rect.left = 0


if __name__ == '__main__':
    clock = pygame.time.Clock()
    field = Field()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(100)
