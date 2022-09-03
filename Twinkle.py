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
pygame.display.set_caption("Twinkle Twinkle Little Star")
song = pygame.mixer.Sound('Twinkle Twinkle Little Star.wav')
timer = time.time()
clock = pygame.time.Clock()
keystate = pygame.key.get_pressed()
wid = random.randrange(100, 1200)
hei = random.randrange(100, 625)

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, White)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Hitcircle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = HitC
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.x = wid
        self.rect.y = hei

HitC = pygame.image.load(path.join(img_dir, "hitcircle.png")).convert()

all_sprites = pygame.sprite.Group()
hit = Hitcircle()
all_sprites.add(hit)
song.play()
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0] and hit.rect.collidepoint(pygame.mouse.get_pos()):
            current_time = time.time() - timer
            if current_time >= 6.5:
                hit.rect.x = random.randrange(100, 1200)
                hit.rect.y = random.randrange(100, 625)
                score += random.randrange(1, 1000)
                if current_time >= 43 and score <= 4500:
                    print(score)
                    call(["python", "Fail.py"])
                    running = False
                if current_time >= 43 and score >= 4500:
                    print(score)
                    call(["python", "Final.py"])
                    running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    #Process input (events)
    #Update
    #Draw/Render
    screen.fill(Black)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 30, 1300, 700)
    pygame.display.flip()


pygame.quit()