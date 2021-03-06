import pygame
import os
import random


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


class Money(pygame.sprite.Sprite):

    def __init__(self, b):
        super().__init__(b)
        self.fire = [load_image('coin.png')]
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.pile = 0
        self.velocity = [0, random.randrange(1, 10)]
        c = random.choices([529, 578])
        self.gravity = 2
        self.position = random.randrange(550, 560) - self.pile
        if c == [529]:
            self.rect.x = random.randrange(451, 550)
        else:
            self.rect.x = random.randrange(725, 812)
        self.rect.y = random.randrange(-20, -5)

    def update(self, b):
        self.velocity[1] += self.gravity
        if self.rect.y < self.position - self.velocity[1]:
            self.rect.y += self.velocity[1]

    def inc_pile(self):
        self.pile += 10

    def dec_pile(self):
        if self.pile != 0:
            self.pile -= 10

    def no_m(self):
        self.kill()


class background(pygame.sprite.Sprite):
    def __init__(self, b, name, x, y, *size):
        super().__init__(b)
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if size:
            self.image = pygame.transform.scale(self.image, size)


class m_b(pygame.sprite.Sprite):
    lst = [-1, 1]

    def __init__(self, b, mov_bac):
        super().__init__(b)
        self.image = load_image(mov_bac)
        self.dir = random.choice(m_b.lst)
        del m_b.lst[m_b.lst.index(self.dir)]
        self.rect = self.image.get_rect()
        if self.dir == -1:
            self.x = 1500
        else:
            self.x = -600
        self.rect.y = random.randrange(0, 300)

    def update(self):
        if self.dir == 1:
            if self.rect.x == 1500:
                self.rect.x = -600
                self.rect.y = random.randrange(0, 300)
        else:
            if self.rect.x == -500:
                self.rect.x = 1500
                self.rect.y = random.randrange(0, 300)
        self.rect.x += self.dir


class Stats(pygame.sprite.Sprite):
    def __init__(self, screen, name, x, y, b):
        super().__init__(b)
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.i = 0.5
        self.f = 50

    def DrawBar(self, pos, size, borderC, barC, ch, screen):
        pygame.draw.rect(screen, borderC, (*pos, *size), 1)
        self.i = self.i + ch
        if (size[1] - 6) * self.i >= size[1]:
            self.i = 1
            self.f = 100
        elif (size[1] - 6) * self.i <= 0:
            self.i = 0
            self.f = 0
        innerSize = (size[0] - 6, (size[1] - 6) * self.i)
        innerPos = (pos[0] + 3, (pos[1] + (size[1] - int(innerSize[1]) - 6) + 3))
        pygame.draw.rect(screen, barC, (*innerPos, *innerSize))


class NPC(pygame.sprite.Sprite):
    def __init__(self, name, side, b):
        super().__init__(b)
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.rect.x = -80
        self.rect.y = 580
        self.dir = -1
        self.i = 0
        self.velx = 15
        self.vely = 5

    def update(self):
        if self.i % 20 < 10:
            self.dir = -1
        else:
            self.dir = 1
        self.rect.y += self.dir
        self.rect.x += self.velx
        self.i += 1
        if self.i % 7 == 0:
            self.rect.y -= self.vely

    def update2(self, name):
        self.image = pygame.transform.flip(load_image(name), True, False)
        if self.i % 20 < 10:
            self.dir = 1
        else:
            self.dir = -1
        self.rect.y += self.dir
        self.rect.x -= self.velx
        self.i += 1
        if self.i % 7 == 0:
            self.rect.y += self.vely + 1
        if self.rect.x < -450:
            self.kill()


class Text(pygame.sprite.Sprite):
    def __init__(self, b, t, n):
        super().__init__(b)
        pygame.time.wait(100)
        self.text = t.split("/n")
        self.image = load_image('text.png')
        self.rect = self.image.get_rect()
        self.rect.x = -10
        self.rect.y = 510
        self.i = 0
        self.j = len(self.text)
        self.font = pygame.font.SysFont("Arial", 20)
        self.textS = self.font.render(n, 1, 'black')
        self.image.blit(self.textS, [38, 20])
        self.font = pygame.font.SysFont("Arial", 14)

    def update(self, txt):
        try:
            self.textSurf = self.font.render(self.text[len(self.text) - self.j], 1, 'black')
            self.image.blit(self.textSurf, [45, 65 + self.i])
            self.i += 20
            self.j -= 1
            pygame.time.wait(200)
        except IndexError:
            pass
