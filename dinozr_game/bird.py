import pygame

from dinozr_game.obsticle import Obsticle
import dinozr_game.constants


class Bird(Obsticle):
    def __init__(self):
        super().__init__(pygame.transform.scale(dinozr_game.constants.BIRD_IMGS[0], (45, 45)), 0, 490)
