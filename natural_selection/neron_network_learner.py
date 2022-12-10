import random
from collections import Counter
from typing import Dict, List

from natural_selection.NeronNetwork import NeronNetwork


class NeronNetworkLearner:
    @staticmethod
    def choose_couples(neron_network_to_score: Dict[NeronNetwork, int], num_of_couples: int) -> List[List[NeronNetwork]]:
        sum_of_scores = sum(neron_network_to_score.values())
        couples_list = []
        for _ in range(num_of_couples):
            couples_list.append(NeronNetworkLearner.choose_couple(neron_network_to_score, sum_of_scores))
        return couples_list

    @staticmethod
    def choose_couple(neron_network_to_score: Dict[NeronNetwork, int], sum_of_scores: int) -> List[NeronNetwork]:
        first_parent = NeronNetworkLearner.choose_random_nn(neron_network_to_score, sum_of_scores)
        second_parent = NeronNetworkLearner.choose_random_nn(neron_network_to_score, sum_of_scores)
        while first_parent is second_parent:
            second_parent = NeronNetworkLearner.choose_random_nn(neron_network_to_score, sum_of_scores)
        return [first_parent, second_parent]

    @staticmethod
    def choose_random_nn(neron_network_to_score: Dict[NeronNetwork, int], sum_of_scores: int) -> NeronNetwork:
        coin = random.randint(1, sum_of_scores)
        scores_sum = 0

        for neron_network, score in neron_network_to_score.items():
            if scores_sum <= coin <= scores_sum + score:
                return neron_network
            scores_sum += score

        raise RuntimeError("What da fuck")


if __name__ == '__main__':
    dic = {"first": 1,
           "second": 2}
    l = [NeronNetworkLearner.choose_random_nn(dic, 3) for i in range(10000)]
    print(Counter(l))
