import math
import random

import pygame

from dinozr_game.dinozor import Dinozor
from dinozr_game.neron_network_dinozor import NeronNetworkDinozor
from dinozr_game.obsticle import Obsticle
from natural_selection.NeronNetwork import NeronNetwork, rand0m

pygame.init()
from dinozr_game.constants import SCREEN
from dinozr_game.Cactus import Cactus
from dinozr_game.bird import Bird

points = 0
game_speed = 10


def find_dis(player_x, obs: Obsticle):
    return player_x - obs.x_pos

def find_min_dis(player: Dinozor, obs_list):
    player_X = player.dino_rect.x -player.dino_rect.w
    min = math.inf
    for i in range(len(obs_list)):
        if 0 < find_dis(player_X, obs_list[i]) < min:
            min = find_dis(player_X, obs_list[i])

    obs_type = isinstance(obs_list[i], Bird)
    return min, obs_type


def game_loose_check(player, obsticles):
    for obs in obsticles:
        if player.dino_rect.colliderect(obs.obs_rect):
            return True
    return False


def score():
    global points, game_speed
    points += 1
    if points % 100 == 0:
        game_speed += 1

    # text = MAMAID_FONT.render("Points: " + str(points), True, (0, 0, 0))
    # text_rect = text.get_rect()
    # text_rect.center = (1000, 40)
    # SCREEN.blit(text, text_rect)


def game(player: Dinozor):
    global game_speed
    run = True
    clock = pygame.time.Clock()

    obsticles = []
    next_time_to_spoon_obsticale = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if next_time_to_spoon_obsticale == 0:
            obsticles.append(random.choice([Cactus(), Bird()]))
            next_time_to_spoon_obsticale = random.randint(50, 110)
        else:
            next_time_to_spoon_obsticale -= 1

        SCREEN.fill((255, 255, 255))
        user_input = pygame.key.get_pressed()
        player.draw(SCREEN)
        obs_distansce, obs_type = find_min_dis(player, obsticles)
        print (obs_type, obs_distansce)

        player.nn_update(game_speed, obs_distansce, obs_type)
        for obs in obsticles:
            obs.update(game_speed)
            obs.draw(SCREEN)
        if game_loose_check(player, obsticles):
            break
        score()

        clock.tick(30)
        pygame.display.update()


def game_2(dinozor):
    game(dinozor)
    return points
