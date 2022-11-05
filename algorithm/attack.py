import random
import networkx as nx


class Attack():
    def __init__(self, G, n):
        self.G = G
        self.n = n


    def random_attack(self):

        edges = list(self.G.edges())

        if not edges:
            return self.G
        else:
            random_edge = random.sample(edges, self.n)
            for i in random_edge:
                self.G.remove_edge(i[0], i[1])
            return self.G


    def smart_attack(self):
        return self.G
