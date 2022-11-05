import math
import random
import scipy.special
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from utils.functions import generate_network


def random_attack(G, n=1):

    edges = list(G.edges())

    if not edges:
        return G
    else:
        random_edge = random.sample(edges, n)
        for i in random_edge:
            G.remove_edge(i[0], i[1])

        return G
