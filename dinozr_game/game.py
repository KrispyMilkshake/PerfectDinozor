import random

import pygame

pygame.init()
from dinozr_game.constants import SCREEN, MAMAID_FONT
from dinozr_game.dinozor import Dinozor
from dinozr_game.Cactus import Cactus
from dinozr_game.bird import Bird


points = 0
game_speed = 10

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

    text = MAMAID_FONT.render("Points: " + str(points), True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (1000, 40)
    SCREEN.blit(text, text_rect)

def main():
    global game_speed
    run = True
    clock = pygame.time.Clock()
    player = Dinozor()
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

        SCREEN.fill((100, 24, 255))
        user_input = pygame.key.get_pressed()
        player.draw(SCREEN)
        player.update(user_input)
        for obs in obsticles:
            obs.update(game_speed)
            obs.draw(SCREEN)
        if game_loose_check(player, obsticles):
            break
        score()

        clock.tick(30)
        pygame.display.update()


main()
