import numpy as np


class Robustness_metric():
    def __init__(self, G):
        """
        Initiates the robustness metric class

        Parameters:
        G (networkx file): the network

        Returns:
        self.G: the network
        """

        self.G = G


    def molloy_reed(self):
        """
        Computes the Molloy-Reed criterion: the average of degree square, divded by the average degree
        The criterion states that the network has a giant component if value is greater than 2

        Returns:
        np.mean(k_square) / np.mean(k) (float): the Molloy-Reed value of the graph
        """

        k = [val for (node, val) in self.G.degree()]
        k_square = np.square(k)

        if all(v == 0 for v in k):
            return 0
        else:
            return np.mean(k_square) / np.mean(k)
