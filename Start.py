import pygame
import os
import random
import sys

def terminate():
    pygame.quit()
    sys.exit()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def st_kingdom():
    bac = screen.blit(load_image('Bagr.png'), (0, 0))
    box = load_image('Main bx.png')
    box = screen.blit(box, [1272 / 2 - 500, 807 / 2 - 210])
    ch = box.blit(load_image('Text_b.png'), [1272 / 2 - 250, 807 / 2 - 140])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.QUIT:
                print(event.pos)
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()

pygame.init()
size = width, height = 1272, 807
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
FPS = 50
running = True

background_sprites = pygame.sprite.Group()

st_kingdom()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()