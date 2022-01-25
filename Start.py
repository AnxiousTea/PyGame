import pygame
import os
import sys
import sqlite3
from b import background, m_b, NPC, Text, Money, Stats

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
    box1 = load_image('Main bx.png')
    box = screen.blit(box1, [1272 / 2 - 550, 807 / 2 - 231])
    x = load_image('Text_b.png')
    ch_s = screen.blit(x, [428, 357])
    ch_w = screen.blit(x, [652, 357])
    ch_n = screen.blit(x, [230, 470])
    ch_c = screen.blit(x, [855, 470])
    font = pygame.font.Font("data/planet benson 2.ttf", 60)
    text = font.render("Choose your kingdom!", 1, [11, 32, 225])
    screen.blit(text, [339, 264])
    font = pygame.font.Font("data/planet benson 2.ttf", 40)
    text = font.render("Nature", 1, [12, 188, 33])
    screen.blit(text, [267, 506])
    text = font.render("Ocean", 1, [13, 86, 221])
    screen.blit(text, [476, 394])
    text = font.render("Sweets", 1, [221, 32, 225])
    screen.blit(text, [890, 506])
    text = font.render("Desert", 1, [221, 110, 21])
    screen.blit(text, [693, 394])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(space)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if ch_n.collidepoint(pos):
                    pygame.mixer.Sound.play(click)
                    return 'Nature_k.db', 'm_f_b.png', 'data/for.mp3'
                if ch_s.collidepoint(pos):
                    pygame.mixer.Sound.play(click)
                    return 's'
                if ch_c.collidepoint(pos):
                    pygame.mixer.Sound.play(click)
                    return 'c'
                if ch_w.collidepoint(pos):
                    pygame.mixer.Sound.play(click)
                    return 'w'
        clock.tick(FPS)
        pygame.display.flip()

def st_gender():
    bac = screen.blit(load_image('Bagr.png'), (0, 0))
    box1 = load_image('Main bx.png')
    box = screen.blit(box1, [1272 / 2 - 550, 807 / 2 - 231])
    x = load_image('Text_b_b.png')
    x2 = load_image('Text_b_b.png')
    k = screen.blit(x2, (721, 388))
    q = screen.blit(x, (279, 388))
    font = pygame.font.Font("data/planet benson 2.ttf", 60)
    text = font.render("Are you a king or queen?", 1, [11, 32, 225])
    screen.blit(text, [295, 290])
    font = pygame.font.Font("data/planet benson 2.ttf", 55)
    text = font.render("King", 1, (202, 11, 20))
    screen.blit(text, (358, 435))
    text = font.render("Queen", 1, (202, 11, 20))
    screen.blit(text, (780, 435))
    while True:
        for event_start in pygame.event.get():
            if event_start.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(space)
            if event_start.type == pygame.MOUSEBUTTONDOWN:
                if k.collidepoint(event_start.pos):
                    pygame.mixer.Sound.play(click)
                    return 'queen.png', 600, 265
                if q.collidepoint(event_start.pos):
                    pygame.mixer.Sound.play(click)
                    return 'king.png', 540, 295
        clock.tick(FPS)
        pygame.display.flip()

def rules():
    bac = screen.blit(load_image('Bagr.png'), (0, 0))
    box1 = load_image('Main bx.png')
    box = screen.blit(box1, [1272 / 2 - 550, 807 / 2 - 231])
    font = pygame.font.Font("data/planet benson 2.ttf", 50)
    txt = font.render("How to play?", 1, [11, 32, 225])
    screen.blit(txt, [500, 260])
    font = pygame.font.Font("data/planet benson 2.ttf", 45)
    txt = font.render("Press 'y' to say YES", 1, [12, 188, 33])
    screen.blit(txt, (435, 335))
    txt = font.render("Press 'n' to say NO", 1, (202, 11, 20))
    screen.blit(txt, (450, 410))
    txt = font.render("Press space to say 'continue'", 1, [221, 110, 21])
    screen.blit(txt, (335, 485))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(space)
                    return
        pygame.display.flip()
        clock.tick(FPS)

pygame.init()
size = width, height = 1272, 807
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 50
running = True

background_sprites = pygame.sprite.Group()
st_sprites = pygame.sprite.Group()
m_sprites = pygame.sprite.Group()

click = pygame.mixer.Sound("data/Modern9.wav")
space = pygame.mixer.Sound("data/Abstract1.wav")

bd, p_k, mu = st_kingdom()
p_g, pos_x, pos_y = st_gender()
if p_k == 'm_f_b.png':
    colourBar = (192, 109, 137)
else:
    colourBar = (50, 50, 50)

rules()

con = sqlite3.connect(bd)
cur = con.cursor()

background(background_sprites, p_k, 0, -80)
m_b(background_sprites)
m_b(background_sprites)
background(background_sprites, 'castle.png', 0, -70)
background(background_sprites, p_g, pos_x, pos_y)

pygame.mixer.music.load(mu)
pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.play()

pink = Stats(screen, 'Heart.png', 724, 123, st_sprites)
mix = Stats(screen, 'Leaf.png', 539, 115, st_sprites)

for _ in range(100):
    Money(m_sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(space)
    background_sprites.update()
    background_sprites.draw(screen)
    st_sprites.draw(screen)
    pink.DrawBar((544, 180), (20, 200), 'black', (106, 154, 145), 0, screen)
    mix.DrawBar((738, 180), (20, 200), 'black', colourBar, 0, screen)
    m_sprites.draw(screen)
    m_sprites.update(m_sprites)
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()