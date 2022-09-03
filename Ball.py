import pygame
from os import path
import os
from subprocess import *
import random
import time

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 1366
HEIGHT = 768
FPS = 60

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0 ,0)
Green = (0, 255, 0)
Blue = (0, 0, 255)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Song")
song = pygame.mixer.Sound('Collapse.wav')
timer = time.time()
clock = pygame.time.Clock()
game_clock = pygame.time.Clock()
wid = random.randrange(400, 900)
hei = 50

# Test for automatic sound recognition
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, White)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def newKeyG():
    g = NoteRed()
    all_sprites.add(g)
    rnote.add(g)

class NoteRed(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = HitKey
        self.rect = self.image.get_rect()
        self.rect.x = 478
        self.rect.y = hei
        self.speedy = (17/5)
        self.last_update = pygame.time.get_ticks()
        self.miss = False
        
    def update(self):
        self.rect.y += self.speedy
        self.speedy = (17/5)

        if not self.miss and self.rect.centery > 700:
            self.miss = True

        if self.rect.centery < 700:
            self.miss = False

class KeyPad(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Keypad
        self.rect = self.image.get_rect()
        self.rect.x = 478
        self.rect.y = 669

HitKey = pygame.image.load(path.join(img_dir, "HitKeyRed.png")).convert()
Keypad = pygame.image.load(path.join(img_dir, "Keys.png")).convert()

all_sprites = pygame.sprite.Group()
rnote = pygame.sprite.Group()
hitkeyred = NoteRed()
pad = KeyPad()
all_sprites.add(hitkeyred)
all_sprites.add(pad)
song.play()

score = 0
multi = 0
combo = 0

running = True
while running:
    for event in pygame.event.get():

        # Closing of game
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # Game Function
        if event.type == pygame.KEYDOWN:
            if hitkeyred.miss and event.key == pygame.K_z:
                combo = 0
                score = score/random.randrange(100, 1000)
                hitkeyred.rect.x = random.randrange(720, 878)
                hitkeyred.rect.y = 1
                score = round(score)

            if hitkeyred.miss and event.key == pygame.K_m:
                combo = 0
                score = score/random.randrange(1, 100)
                hitkeyred.rect.x = random.randrange(478, 634)
                hitkeyred.rect.y = 1
                score = round(score)

            if event.key == pygame.K_z and hitkeyred.rect.y >= 650 and hitkeyred.rect.x <= 634:
                hitkeyred.rect.x = random.randrange(720, 878)
                hitkeyred.rect.y = 1
                combo = combo + 1
                multi = combo * (random.randrange(1, 100))/10
                score = score + multi
                score = round(score)

            if event.key == pygame.K_m and hitkeyred.rect.y >= 650 and hitkeyred.rect.x >= 720:
                hitkeyred.rect.x = random.randrange(478, 634)
                hitkeyred.rect.y = 1
                combo = combo + 1
                multi = combo * (random.randrange(1, 100))/10
                score = score + multi
                score = round(score)

            current_time = time.time() - timer
            if current_time >= 152 and score <= 999:
                print(score)
                call(["python", "Fail.py"])
                running = False
            if current_time >= 152 and score >= 1000:
                print(score)
                call(["python", "Final.py"])
                running = False

            if score <= 0:
                score = 0

    all_sprites.update()

    #Process input (events)
    #Update
    #Draw/Render
    screen.fill(Black)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 30, 1300, 700)
    draw_text(screen, str(combo), 30, 50, 700)
    pygame.display.flip()


pygame.quit()
