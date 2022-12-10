import os

import pygame

RUNNING_IMGS = [pygame.image.load(os.path.join("../dinozr_game/pictures", "dinozor.png")),
                pygame.image.load(os.path.join("../dinozr_game/pictures", "dinozor2.png"))]
DUCKING_IMGS = [pygame.image.load(os.path.join("../dinozr_game/pictures", "dinozor_duck.png")),
                pygame.image.load(os.path.join("../dinozr_game/pictures", "dinozor_duck2.png"))]
JUMPING_IMGS = [pygame.image.load(os.path.join("../dinozr_game/pictures", "dinozor_jump.png"))]
CACTUS_IMGS = [pygame.image.load(os.path.join("../dinozr_game/pictures", "cactus.png"))]
BIRD_IMGS = [pygame.image.load(os.path.join("../dinozr_game/pictures", "bird.png"))]

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

MAMAID_FONT = pygame.font.Font("Mermaid Babies.ttf", 20)