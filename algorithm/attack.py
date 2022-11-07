import random
import numpy as np
import networkx as nx


class Attack():
    def __init__(self, G, p):
        self.G = G
        self.p = p


    def random_attack(self):

        # Random attack selects p% of the edges at random and removes them from the network

        edges = list(self.G.edges())

        if not edges:
            return self.G
        else:
            random_edge = random.sample(edges, int(len(edges) * self.p))
            for i in random_edge:
                self.G.remove_edge(i[0], i[1])
            return self.G


    def smart_attack(self):

        # Smart attack follows this processs
        # 1. Select the top p% of nodes with the highest degree
        # 2. Randomly sample a set of edges from each of the selected node

        degree = sorted(self.G.degree, key=lambda x: x[1], reverse=True)
        node_select = degree[:(int(len(degree) * self.p))]

        for node in node_select:

            edge = list(self.G.edges(node[0]))
            random_edge = random.sample(edge, int(len(edge) * self.p))

            for i in random_edge:
                self.G.remove_edge(i[0], i[1])

        return self.G
