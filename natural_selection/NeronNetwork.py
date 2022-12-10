import numpy as np

ReLU = lambda x: np.max(x, 0)


def rand0m(size):
    return np.random.random(size) * 2 - 1

class NeronNetwork:

    def __init__(self, weight_list, biest_list):
        self.weight_list = weight_list
        self.biest_list = biest_list

    def forward_propagation(self, nn_input):
        layer = nn_input

        for i in range(len(self.weight_list) - 1):
            layer = layer @ self.weight_list[i] + self.biest_list[i]
            layer = ReLU(layer)

        layer = layer @ self.weight_list[-1] + self.biest_list[-1]
        layer = np.tanh(layer)
        return layer

    def __str__(self):
        print(self.weight_list)
        print(self.biest_list)
        return ""


if __name__ == '__main__':
    weight_list = [rand0m((3, 10)), rand0m((10, 10)), rand0m((10, 2))]
    biest_list = [rand0m((1, 10)), rand0m((1, 10)), rand0m((1, 2))]
    nn = NeronNetwork(weight_list, biest_list)

    nn_input = np.ones((3))
    print(nn.forward_propagation(nn_input))
