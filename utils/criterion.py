import random
import scipy.special
import numpy as np
import networkx as nx


class Robustness_metric():
    def __init__(self, G):
        self.G = G

    def molloy_reed(self):

        # Molly-Reed criterion states that the network has a giant component if <k^2> / <k> > 2

        degree = [val for (node, val) in self.G.degree()]
        degree_sqrt = np.square(degree)

        if all(v == 0 for v in degree):
            return 0
        else:
            return np.mean(degree_sqrt) / np.mean(degree)
