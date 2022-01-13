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
        a = (491, 598)
        b = (705, 802)
        self.velocity = [0, random.randrange(1, 10)]
        c = random.choices([529, 578])
        self.gravity = 2
        self.position = random.randrange(550, 560)
        if c == [529]:
            self.rect.x = random.randrange(451, 550)
        else:
            self.rect.x = random.randrange(725, 812)
        self.rect.y = random.randrange(-20, -5)

    def update(self, b):
        self.velocity[1] += self.gravity
        if self.rect.y < self.position - self.velocity[1]:
            self.rect.y += self.velocity[1]



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
    def __init__(self, b):
        super().__init__(b)
        self.image = load_image('m_f_b.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -80
        self.dir = 0.9
        m_b.update(self)

    def update(self):
        if self.rect.x == -10:
            self.dir = 0
        elif self.rect.x == 10:
            self.dir = -0
        self.rect.x += self.dir

class Stats(pygame.sprite.Sprite):
    def __init__(self, screen, name, x, y, b):
        super().__init__(b)
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def DrawBar(pos, size, borderC, barC, progress, screen):
        pygame.draw.rect(screen, borderC, (*pos, *size), 1)
        innerSize = (size[0] - 6, (size[1] - 6) * progress)
        innerPos = (pos[0] + 3, (pos[1] + (size[1] - int(innerSize[1]) - 6) + 3))
        pygame.draw.rect(screen, barC, (*innerPos, *innerSize))



class NPC(pygame.sprite.Sprite):
    def __init__(self, name, side, b):
        super().__init__(b)
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 595
        self.dir = -1
        self.i = 0

    def update(self):
        if self.rect.x < 407:
            if self.i % 20 < 10:
                self.dir = -1
            else:
                self.dir = 1
            self.rect.y += self.dir
            self.rect.x += 2
            self.i += 1
            if self.i % 7 == 0:
                self.rect.y -= 1

class Text(pygame.sprite.Sprite):
    def __init__(self, b):
        super().__init__(b)
        self.image = load_image('text.png')
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 510
        self.font = pygame.font.SysFont("Arial", 18)
        self.textSurf = self.font.render('hello', 1, 'black')
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [400 / 2 - W / 2, 164 / 2 - H / 2])