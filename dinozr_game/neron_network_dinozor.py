import pygame

from dinozr_game.dinozor import Dinozor
from natural_selection.NeronNetwork import NeronNetwork


class NeronNetworkDinozor(Dinozor):
    def __init__(self, neron_network: NeronNetwork):
        super().__init__()
        self.neron_network = neron_network

    def nn_update(self, game_speed, distance, obs_type):
        neron_network_input = [game_speed, distance, obs_type]
        update = self.neron_network.forward_propagation(neron_network_input)

        user_input = {}
        user_input[pygame.K_UP] = update[0][0] > 0.5
        user_input[pygame.K_DOWN] = update[0][1] > 0.5

        self.update(user_input)