import random
import scipy.special
import numpy as np
import networkx as nx


class Robustness_metric():
    def __init__(self, G):
        self.G = G

    def molloy_reed(self):

        # Molloy-Reed criterion states that the network has a giant component if value is greater than 2
        # The criterion calculates the average of degree square, divded by the average degree

        k = [val for (node, val) in self.G.degree()]
        k_square = np.square(k)

        if all(v == 0 for v in k):
            return 0
        else:
            return np.mean(k_square) / np.mean(k)
