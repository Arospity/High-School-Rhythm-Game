import pygame
import random
from os import path
import os
from subprocess import *

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 1600
HEIGHT = 900
FPS = 60

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0 ,0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Song Selection")
clock = pygame.time.Clock()

class HappyBday(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Bday_img
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 1.18
        self.rect.bottom = HEIGHT / 6

class Twinkle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Twinkle_img
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 1.27
        self.rect.bottom = HEIGHT / 2.3

class BallGame(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Ball_img
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 1.31
        self.rect.bottom = HEIGHT / 1.38

class Robin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Robin_img
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 1.15
        self.rect.bottom = HEIGHT / 1.05

class Back(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Back_img
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 20
        self.rect.bottom = HEIGHT / 1.01


Bday_img = pygame.image.load(path.join(img_dir, "bday.png")).convert()
Twinkle_img = pygame.image.load(path.join(img_dir, "Twinkle.png")).convert()
Ball_img = pygame.image.load(path.join(img_dir, "BallGame.png")).convert()
Robin_img = pygame.image.load(path.join(img_dir, "Robin.png")).convert()
Back_img = pygame.image.load(path.join(img_dir, "Back.png")).convert()

all_sprites = pygame.sprite.Group()
bday = HappyBday()
all_sprites.add(bday)
twinkle = Twinkle()
all_sprites.add(twinkle)
ball = BallGame()
all_sprites.add(ball)
robin = Robin()
all_sprites.add(robin)
back = Back()
all_sprites.add(back)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0] and bday.rect.collidepoint(pygame.mouse.get_pos()):
            call(["python", "Happy_Bday.py"])
        if pygame.mouse.get_pressed()[0] and twinkle.rect.collidepoint(pygame.mouse.get_pos()):
            call(["python", "Twinkle.py"])
        if pygame.mouse.get_pressed()[0] and ball.rect.collidepoint(pygame.mouse.get_pos()):
            call(["python", "Ball.py"])
        if pygame.mouse.get_pressed()[0] and robin.rect.collidepoint(pygame.mouse.get_pos()):
            call(["python", "Robin.py"])
        if pygame.mouse.get_pressed()[0] and back.rect.collidepoint(pygame.mouse.get_pos()):
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


    #Process input (events)
    #Update
    #Draw/Render
    screen.fill(Black)
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()
