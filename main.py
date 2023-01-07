from dinozr_game.neron_network_dinozor import NeronNetworkDinozor
from natural_selection.NeronNetworkBuilder import NeronNetworkBuilder
from natural_selection.neron_network_learner import NeronNetworkLearner
from dinozr_game import game


size_list = [3, 4, 4, 2]
nn_list = NeronNetworkBuilder.create_random_nn_list(size_list, 100)


def main():
    nn_player = NeronNetworkDinozor(nn_list[0])
    print(game.game_2(nn_player))

if __name__ == '__main__':
    main()
