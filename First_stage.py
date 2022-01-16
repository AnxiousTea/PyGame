import pygame
import os
import random
import sys
from b import background
from b import m_b
from b import NPC
from b import Text
from b import Money
from b import Stats

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

def going_out():
    npc = NPC('bunny.png', 0, npc_sprites)
    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        mbackground_sprites.draw(screen)
        mbackground_sprites.update()
        background_sprites.draw(screen)
        st_sprites.draw(screen)
        pink.DrawBar((544, 180), (20, 200), 'black', (106, 154, 145), 0, screen)
        blue.DrawBar((738, 180), (20, 200), 'black', (192, 109, 137), 0, screen)
        m_sprites.draw(screen)
        m_sprites.update(m_sprites)
        npc_sprites.draw(screen)
        if npc.rect.x < 407:
            npc_sprites.update()
        else:
            return
        pygame.display.flip()
        clock.tick(40)

def quest():
    text = Text(text_sprites, 'bdhiwwb')
    ch = 0
    flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y and flag is False:
                    ch = 0.2
                    pink.DrawBar((544, 180), (20, 200), 'black', (106, 154, 145), ch, screen)
                    text = (text_sprites, 'yryryr')
                    flaf = False
                elif event.key == pygame.K_n and flag is False:
                    ch = -0.3
                    text = (text_sprites, 'iejedeu')
                    flag = True
                if event.key == pygame.K_SPACE and flag is True:
                    going_back()
        mbackground_sprites.draw(screen)
        mbackground_sprites.update()
        background_sprites.draw(screen)
        st_sprites.draw(screen)
        pink.DrawBar((544, 180), (20, 200), 'black', (106, 154, 145), 0, screen)
        blue.DrawBar((738, 180), (20, 200), 'black', (192, 109, 137), 0, screen)
        text_sprites.draw(screen)
        npc_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(40)

def going_back():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        mbackground_sprites.draw(screen)
        mbackground_sprites.update()
        background_sprites.draw(screen)
        st_sprites.draw(screen)
        pink.DrawBar((544, 180), (20, 200), 'black', (106, 154, 145), 0, screen)
        blue.DrawBar((738, 180), (20, 200), 'black', (192, 109, 137), 0, screen)
        m_sprites.draw(screen)
        m_sprites.update(m_sprites)
        npc_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(40)


pygame.init()
size = width, height = 1272, 807
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
background_sprites = pygame.sprite.Group()
mbackground_sprites = pygame.sprite.Group()
npc_sprites = pygame.sprite.Group()
text_sprites = pygame.sprite.Group()
m_sprites = pygame.sprite.Group()
st_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
st_sprites = pygame.sprite.Group()
FPS = 50
running = True
gen = 'queen.png'
knd = 'm_f_b.png'
m_b(mbackground_sprites)
background(background_sprites, 'castle.png', 0, -70)
background(background_sprites, gen, 330, -45)
pink = Stats(screen, 'Heart.png', 724, 123, st_sprites)
blue = Stats(screen, 'Leaf.png', 539, 115, st_sprites)

for _ in range(70):
    Money(m_sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.VIDEORESIZE:
            old_surface_saved = screen
            screen = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
            screen.blit(old_surface_saved, (0, 0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                going_out()
                quest()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    screen.fill('white')
    mbackground_sprites.draw(screen)
    mbackground_sprites.update()
    background_sprites.draw(screen)
    st_sprites.draw(screen)
    pink.DrawBar((544, 180), (20, 200), 'black', (106, 154, 145), 0, screen)
    blue.DrawBar((738, 180), (20, 200), 'black', (192, 109, 137), 0, screen)
    m_sprites.draw(screen)
    m_sprites.update(m_sprites)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()