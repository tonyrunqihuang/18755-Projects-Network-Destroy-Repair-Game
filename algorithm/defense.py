import random
import numpy as np
import networkx as nx


class Defense():
    def __init__(self, G, p):
        self.G = G
        self.p = p


    def random_defense(self):

        nodes = list(self.G.nodes())

        if not nodes:
            return self.G

        else:
            for i in range(int(self.p * len(nodes))):
                random_nodes = random.sample(nodes, 2)
                if random_nodes[0] in self.G.neighbors(random_nodes[1]) == False:
                    self.G.add_edge(random_nodes[0], random_nodes[1])
            return self.G

    def smart_defense(self):
        return self.G
