import random
import numpy as np
import networkx as nx
from utils.misc import generate_network


def random_attack(G, n):

    edges = list(G.edges())

    if not edges:
        return G
    else:
        random_edge = random.sample(edges, n)
        for i in random_edge:
            G.remove_edge(i[0], i[1])

        return G


def smart_attack(G, n):
    return G
