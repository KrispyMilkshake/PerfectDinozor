import random
from typing import List

import numpy as np

from NeronNetwork import NeronNetwork
from NeronNetwork import rand0m


class NeronNetworkBuilder:
    @staticmethod
    def create_random_nn(size_list: List[int]) -> NeronNetwork:
        weight_list = []
        biest_list = []
        for i in range(len(size_list) - 1):
            weight_list.append(rand0m((size_list[i], size_list[i + 1])))
            biest_list.append(rand0m((1, size_list[i + 1])))
        return NeronNetwork(weight_list, biest_list)

    @staticmethod
    def merge_two_nn(first_nn: NeronNetwork, second_nn: NeronNetwork) -> NeronNetwork:
        weight_list = []
        for w1, w2 in zip(first_nn.weight_list, second_nn.weight_list):
            weight_metrix = NeronNetworkBuilder.marage_matrix(w1, w2)
            weight_list.append(np.array(weight_metrix))

        biest_list = []
        for b1, b2 in zip(first_nn.biest_list, second_nn.biest_list):
            biest_metrix = NeronNetworkBuilder.marage_matrix(b1, b2)
            biest_list.append(np.array(biest_metrix))

        return NeronNetwork(weight_list, biest_list)

    @staticmethod
    def marage_matrix(first_metrix, second_metrix):
        metrix = []
        for i in range(len(first_metrix)):
            array = []
            for j in range(len(first_metrix[i])):
                weight_coin = random.random()
                if weight_coin <= 0.45:
                    array.append(first_metrix[i][j])
                elif weight_coin <= 0.9:
                    array.append(second_metrix[i][j])
                else:
                    array.append(random.random())
            metrix.append(array)
        return metrix


if __name__ == '__main__':
    # size_list = [3, 10, 10, 2]
    size_list = [1, 2, 1]
    nn1 = NeronNetworkBuilder.create_random_nn(size_list)
    nn2 = NeronNetworkBuilder.create_random_nn(size_list)
    print(nn1)
    nn3 = NeronNetworkBuilder.merge_two_nn(nn1, nn2)
    print(nn3)
