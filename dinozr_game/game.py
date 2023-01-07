import math
import random
from typing import List, Dict

import pygame

from dinozr_game.dinozor import Dinozor
from dinozr_game.obsticle import Obsticle

pygame.init()
from dinozr_game.constants import SCREEN
from dinozr_game.Cactus import Cactus
from dinozr_game.bird import Bird

MAMAID_FONT = pygame.font.Font("dinozr_game/Mermaid Babies.ttf", 20)


def find_dis(player_x, obs: Obsticle):
    return player_x - obs.x_pos


def find_min_dis(player: Dinozor, obs_list):
    player_X = player.dino_rect.x - player.dino_rect.w
    min = math.inf
    min_index = 0
    for i in range(len(obs_list)):
        if 0 < find_dis(player_X, obs_list[i]) < min:
            min = find_dis(player_X, obs_list[i])
            min_index = i

    obs_type = isinstance(obs_list[min_index], Bird)
    return min, obs_type


def game_loose_check(player, obsticles):
    for obs in obsticles:
        if player.dino_rect.colliderect(obs.obs_rect):
            return True
    return False


def draw_data(points, alive_count):
    text_points = MAMAID_FONT.render("Points: " + str(points), True, (0, 0, 0))
    text_rect_points = text_points.get_rect()
    text_rect_points.center = (1000, 40)
    SCREEN.blit(text_points, text_rect_points)

    text_alive = MAMAID_FONT.render("Alive: " + str(alive_count), True, (0, 0, 0))
    text_rect_alive = text_alive.get_rect()
    text_rect_alive.center = (1000, 80)
    SCREEN.blit(text_alive, text_rect_alive)


def game(players: List[Dinozor]):
    results: Dict[Dinozor, int] = {}

    points = 0
    game_speed = 10

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
        # user_input = pygame.key.get_pressed()
        for player in players:
            player.draw(SCREEN)
            obs_distansce, obs_type = find_min_dis(player, obsticles)
            # print (obs_type, obs_distansce)
            player.nn_update(game_speed, obs_distansce, obs_type)

        for obs in obsticles:
            obs.update(game_speed)
            obs.draw(SCREEN)

        for player in players:
            if game_loose_check(player, obsticles):
                results[player.neron_network] = points
                players.remove(player)

        if not players:
            break

        points += 1
        if points % 100 == 0:
            game_speed += 1

        draw_data(points, len(players))

        clock.tick(30)
        pygame.display.update()

    return results
