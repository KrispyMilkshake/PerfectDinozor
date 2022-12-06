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
        biest_list = []

        for i in range(len(first_nn.weight_list)):
            weight_metrix = []
            biest_metrix = []

            for j in range(len(first_nn.weight_list[i])):
                weight_array = []
                for k in range(len(first_nn.weight_list[i][j])):
                    weight_coin = random.random()
                    if weight_coin <= 0.45:
                        weight_array.append(first_nn.weight_list[i][j][k])
                    elif weight_coin <= 0.9:
                        weight_array.append(second_nn.weight_list[i][j][k])
                    else:
                        weight_array.append(random.random())
                weight_metrix.append(weight_array)

            for j in range(len(first_nn.biest_list[i])):
                biest_array = []
                for k in range(len(first_nn.biest_list[i][j])):
                    biest_coin = random.random()
                    if biest_coin <= 0.45:
                        biest_array.append(first_nn.biest_list[i][j][k])
                    elif biest_coin <= 0.9:
                        biest_array.append(second_nn.biest_list[i][j][k])
                    else:
                        biest_array.append(random.random())
                biest_metrix.append(biest_array)

            weight_list.append(np.array(weight_metrix))
            biest_list.append(np.array(biest_metrix))

        return NeronNetwork(weight_list, biest_list)


if __name__ == '__main__':
    # size_list = [3, 10, 10, 2]
    size_list = [1, 2, 1]
    nn1 = NeronNetworkBuilder.create_random_nn(size_list)
    nn2 = NeronNetworkBuilder.create_random_nn(size_list)
    print(nn1)
    nn3 = NeronNetworkBuilder.merge_two_nn(nn1, nn2)
    print(nn3)
