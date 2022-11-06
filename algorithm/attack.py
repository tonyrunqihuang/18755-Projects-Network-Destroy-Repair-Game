import numpy as np
import random
import networkx as nx


class Attack():
    def __init__(self, G, n):
        self.G = G
        self.n = n


    def random_attack(self):

        # Random attack selects n edges at random and removes them from the network

        edges = list(self.G.edges())

        if not edges:
            return self.G
        else:
            random_edge = random.sample(edges, self.n)
            for i in random_edge:
                self.G.remove_edge(i[0], i[1])
            return self.G


    def smart_attack(self, p):

        # Smart attack follows this processs
        # 1. Select the top p% of nodes with the highest degree
        # 2. Randomly sample a set of edges from each of the selected node

        degree = sorted(self.G.degree, key=lambda x: x[1], reverse=True)
        node_select = degree[:(int(len(degree) * p))]

        for node in node_select:

            edge = list(self.G.edges(node[0]))
            random_edge = random.sample(edge, int(len(edge) * p))

            for i in random_edge:
                self.G.remove_edge(i[0], i[1])

        return self.G
