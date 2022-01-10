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

def choose_gender():
    screen.fill('black')
    text = 'Are you a king or a queen?'
    font = pygame.font.Font(None, 100)
    text_coord = 50
    string_rendered = font.render(text, 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    screen.blit(string_rendered, intro_rect)
    f = pygame.transform.scale(load_image('Female_06.png'), (400, 609))
    m = pygame.transform.scale(load_image('Male_10.png'), (400, 609))
    r1 = screen.blit(f, (40, 60))
    r2 = screen.blit(m, (500, 60))
    while True:
        for event_start in pygame.event.get():
            if event_start.type == pygame.QUIT:
                terminate()
            if event_start.type == pygame.MOUSEBUTTONDOWN:
                if r1.collidepoint(event_start.pos):
                    return 'f'
                if r2.collidepoint(event_start.pos):
                    return 'm'
        pygame.display.flip()
        clock.tick(FPS)

def choose_knd():
    text = 'Choose your kingdom!'
    font = pygame.font.Font(None, 100)
    text_coord = 50
    string_rendered = font.render(text, 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    screen.blit(string_rendered, intro_rect)
    n = pygame.transform.scale(load_image('Forest.png'), (400, 609))
    r1 = screen.blit(n, (40, 60))
    s = pygame.transform.scale(load_image('Sea.png'), (400, 609))
    r2 = screen.blit(s, (460, 60))
    c = pygame.transform.scale(load_image('candy.png'), (400, 609))
    r3 = screen.blit(c, (690, 60))
    w = pygame.transform.scale(load_image('waste.png'), (400, 609))
    r4 = screen.blit(w, (1290, 60))
    while True:
        for event_start in pygame.event.get():
            if event_start.type == pygame.QUIT:
                terminate()
            if event_start.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if r1.collidepoint(pos):
                    return 'n'
                if r2.collidepoint(pos):
                    return 's'
                if r3.collidepoint(pos):
                    return 'c'
                if r4.collidepoint(pos):
                    return 'w'
        pygame.display.flip()
        clock.tick(FPS)

pygame.init()
size = width, height = 1600, 700
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
FPS = 50
running = True

kind = choose_knd()
gen = choose_gender()

background_sprites = pygame.sprite.Group()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()