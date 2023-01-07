from dinozr_game.neron_network_dinozor import NeronNetworkDinozor
from natural_selection.NeronNetworkBuilder import NeronNetworkBuilder
from natural_selection.neron_network_learner import NeronNetworkLearner
from dinozr_game import game

SIZE_LIST = [3, 4, 4, 2]
NUMBER_OF_NN_IN_GENERATION = 100


def main():
    nn_list = NeronNetworkBuilder.create_random_nn_list(SIZE_LIST, NUMBER_OF_NN_IN_GENERATION)
    for _ in range(10):
        nn_players = [NeronNetworkDinozor(i) for i in nn_list]
        dic_nn_to_score = game.game(nn_players)



        couples_nn_list = NeronNetworkLearner.choose_couples(dic_nn_to_score, NUMBER_OF_NN_IN_GENERATION)
        new_nn_list = []
        for couple in couples_nn_list:
            new_nn_list.append(NeronNetworkBuilder.merge_two_nn(*couple))

        nn_list = new_nn_list



if __name__ == '__main__':
    main()
