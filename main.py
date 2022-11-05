import networkx as nx
import numpy as np
from runner import Runner


if __name__ == '__main__':
    G = nx.complete_graph(10)
    print(nx.info(G))
    runner = Runner('twitter_combined', 10)
