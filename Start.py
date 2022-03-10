import pygame
import os
import sys
import sqlite3
from b import background, m_b, NPC, Text, Money, Stats
import random

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
            if event_start.type == pygame.KEYDOWN:
                if event_start.key == pygame.K_SPACE:
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

def going_out(ind):
    res = cur.execute("""SELECT npc, offic_npc
                            FROM Level1
                            WHERE id = ?""", (ind,)).fetchall()
    flag = False
    npc = NPC(res[0][0], 0, npc_sprites)
    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        background_sprites.draw(screen)
        background_sprites.update()
        st_sprites.draw(screen)
        pink.DrawBar((544, 180), (20, 200), 'black', (106, 154, 145), 0, screen)
        mix.DrawBar((738, 180), (20, 200), 'black', (192, 109, 137), 0, screen)
        m_sprites.draw(screen)
        m_sprites.update(m_sprites)
        npc_sprites.draw(screen)
        if npc.rect.x > 407 and flag is False:
            quest(ind, res[0][1])
            flag = True
        if npc.rect.x < -85:
            return
        if flag is False:
            npc.update()
        elif flag is True:
            npc.update2(res[0][0])
        pygame.display.flip()
        clock.tick(40)

def quest(ind, name):
    res = cur.execute("""SELECT text, smth_op, yes_m, yes_h,
                            yes_l, no_m, no_h, no_l, yes_text, no_text
                            FROM Level1
                            WHERE id = ?""", (ind,)).fetchall()
    text = Text(text_sprites, res[0][0], name)
    pygame.mixer.Sound.play(txt)
    ch_p = 0
    ch_m = 0
    flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y and flag is False:
                    pygame.mixer.Sound.play(yes)
                    ch_p = res[0][3] / 100
                    ch_m = res[0][4] / 100
                    pink.DrawBar((544, 180), (20, 200), 'black', (106, 154, 145), ch_p, screen)
                    mix.DrawBar((738, 180), (20, 200), 'black', (192, 109, 137), ch_m, screen)
                    if res[0][2] > 0:
                        for i in range(res[0][2]):
                            Money(m_sprites)
                            lst_m[i].inc_pile()
                    elif res[0][2] < 0:
                        for i in range(abs(res[0][2])):
                            lst_m[i].no_m()
                    text = Text(text_sprites, res[0][8], name)
                    pygame.mixer.Sound.play(txt)
                    if res[0][1] != 0:
                        pass
                    flag = True
                elif event.key == pygame.K_n and flag is False:
                    pygame.mixer.Sound.play(yes)
                    ch_p = res[0][6] / 100
                    ch_m = res[0][7] / 100
                    pink.DrawBar((544, 180), (20, 200), 'black', (106, 154, 145), ch_p, screen)
                    mix.DrawBar((738, 180), (20, 200), 'black', (192, 109, 137), ch_m, screen)
                    if res[0][5] > 0:
                        for i in range(res[0][5]):
                            Money(m_sprites)
                            lst_m[i].inc_pile()
                    elif res[0][5] < 0:
                        for i in range(abs(res[0][5])):
                            lst_m[i].no_m()
                    text = Text(text_sprites, res[0][9], name)
                    pygame.mixer.Sound.play(txt)
                    flag = True
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(space)
                    if flag is True:
                        return
        background_sprites.draw(screen)
        background_sprites.update()
        st_sprites.draw(screen)
        pink.DrawBar((544, 180), (20, 200), 'black', (106, 154, 145), 0, screen)
        mix.DrawBar((738, 180), (20, 200), 'black', (192, 109, 137), 0, screen)
        m_sprites.draw(screen)
        m_sprites.update(m_sprites)
        text_sprites.draw(screen)
        text_sprites.update(txt)
        npc_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(40)


pygame.init()
size = width, height = 1272, 807
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 50
running = True

background_sprites = pygame.sprite.Group()
st_sprites = pygame.sprite.Group()
m_sprites = pygame.sprite.Group()
npc_sprites = pygame.sprite.Group()
text_sprites = pygame.sprite.Group()

click = pygame.mixer.Sound("data/Modern9.wav")
space = pygame.mixer.Sound("data/Abstract1.wav")
txt = pygame.mixer.Sound("data/writing.wav")
yes = pygame.mixer.Sound("data/yes.wav")
no = pygame.mixer.Sound("data/no.wav")

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
lst_m = list()
background(background_sprites, 'castle.png', 0, -70)
background(background_sprites, p_g, pos_x, pos_y)

pygame.mixer.music.load(mu)
pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.play()

pink = Stats(screen, 'Heart.png', 724, 123, st_sprites)
mix = Stats(screen, 'Leaf.png', 539, 115, st_sprites)

for _ in range(100):
    lst_m.append(Money(m_sprites))

i = 1
f = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(space)
                if f is False:
                    f = True
                    going_out(1)
        if i % 100 == 0 and f is True:
            x = random.randrange(2, 2)
            res = cur.execute("""SELECT avi
                                        FROM Level1
                                        WHERE id = ?""", (x,)).fetchall()
            while res[0] == 0:
                x = random.randrange(2, 2)
                res = cur.execute("""SELECT avi
                                        FROM Level1
                                        HERE id = ?""", (x,)).fetchall()
            going_out(x)
        i += 0.5
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