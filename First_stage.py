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
        for event_start in pygame.event.get():
            if event_start.type == pygame.QUIT:
                return
        mbackground_sprites.draw(screen)
        mbackground_sprites.update()
        background_sprites.draw(screen)
        npc_sprites.draw(screen)
        if npc.rect.x < 407:
            npc_sprites.update()
        else:
            quest()
        pygame.display.flip()
        clock.tick(40)

def quest():
    text = Text(text_sprites)
    go = True
    while go:
        for event_start in pygame.event.get():
            if event_start.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
        mbackground_sprites.draw(screen)
        mbackground_sprites.update()
        background_sprites.draw(screen)
        text_sprites.draw(screen)
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
clock = pygame.time.Clock()
st_sprites = pygame.sprite.Group()
FPS = 50
running = True
gen = 'queen.png'
knd = 'm_f_b.png'
m_b(mbackground_sprites)
background(background_sprites, 'castle.png', 0, -70)
background(background_sprites, gen, 330, -45)
Stats(screen, 'Heart.png', 759, 125, st_sprites)
Stats(screen, 'Leaf.png', 525,128, st_sprites)

for _ in range(50):
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    screen.fill('white')
    mbackground_sprites.draw(screen)
    mbackground_sprites.update()
    background_sprites.draw(screen)
    st_sprites.draw(screen)
    m_sprites.draw(screen)
    m_sprites.update(m_sprites)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()