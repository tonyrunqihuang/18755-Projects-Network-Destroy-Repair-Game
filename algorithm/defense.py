import random
import networkx as nx


class Defense():
    def __init__(self, G, n):
        self.G = G
        self.n = n

    def random_defense(self):
        return self.G

    def smart_defense(self):
        return self.G
