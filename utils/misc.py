import os
import random
import math
import scipy.special
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def set_seed(seed=123456):
    random.seed(seed)
    np.random.seed(seed)


def generate_network(name):

    G = nx.read_edgelist('./data/' + name + ".txt", create_using=nx.DiGraph(), nodetype = int)

    return G


def get_network_attr(G):

    # number of nodes
    nodes = nx.number_of_nodes(G)

    # number of edges
    edges = nx.number_of_edges(G)

    # the average degree
    degrees = [val for (node, val) in G.degree()]
    avg_degree = np.mean(degrees)

    # number of components
    components = nx.number_connected_components(G)

    # average and global clustering coefficients
    avg_cluster_coef = nx.average_clustering(G)
    triangles = sum(nx.triangles(G.to_undirected()).values()) / 3
    global_cluster_coef = 3 * triangles / np.sum([scipy.special.binom(i, 2) for i in degrees])

    # Distance
    distance = nx.average_shortest_path_length(G)

    return nodes, edges, avg_degree, components, avg_cluster_coef, global_cluster_coef, distance
