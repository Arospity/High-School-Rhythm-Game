import pygame
from os import path
import os
from subprocess import *
import random
import time

img_dir = path.join(path.dirname(__file__), 'img')

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
pygame.display.set_caption("Congrats!")
timer = time.time()
clock = pygame.time.Clock()
keystate = pygame.key.get_pressed()

class Show(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Cong
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 3.23
        self.rect.y = HEIGHT / 3

class MainM(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Menu
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 3.23
        self.rect.y = HEIGHT / 1.5

class Dog(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Dog_img
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2.26
        self.rect.y = 50

Cong = pygame.image.load(path.join(img_dir, "BL.png")).convert()
Menu = pygame.image.load(path.join(img_dir, "MM.png")).convert()
Dog_img = pygame.image.load(path.join(img_dir, "HappyDog.jpg")).convert()

all_sprites = pygame.sprite.Group()
show = Show()
all_sprites.add(show)
main = MainM()
all_sprites.add(main)
dog = Dog()
all_sprites.add(dog)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0] and main.rect.collidepoint(pygame.mouse.get_pos()):
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    #Process input (events)
    #Update
    #Draw/Render
    screen.fill(Black)
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()