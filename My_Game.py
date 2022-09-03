import pygame
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
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
keystate = pygame.key.get_pressed()


class Title(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = title_img
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 3

class Close(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = close_img
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 1.5

title_img = pygame.image.load(path.join(img_dir, "Title.png")).convert()
close_img = pygame.image.load(path.join(img_dir, "Close.png")).convert()


all_sprites = pygame.sprite.Group()
title = Title()
all_sprites.add(title)
close = Close()
all_sprites.add(close)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # Closing the game with the close option
        if pygame.mouse.get_pressed()[0] and close.rect.collidepoint(pygame.mouse.get_pos()):
            running = False
        # Open Song Selection Screen
        if pygame.mouse.get_pressed()[0] and title.rect.collidepoint(pygame.mouse.get_pos()):
            call(["python", "Song_Selection.py"])

    # Process input (events)
    # Update
    # Draw/Render
    screen.fill((Black))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
