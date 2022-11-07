import os
import math
import random
import argparse
import scipy.special
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def get_args():

    parser = argparse.ArgumentParser("Experiment Hyperparamters")
    parser.add_argument("--network_name", type=str, default='social network', help="network name",
                        choices=['social network', 'p2p network', 'email network', 'as network'])
    parser.add_argument("--algorithm", type=str, default='random', help="algorithm name",
                        choices=['random', 'smart'])
    parser.add_argument("--criterion", type=str, default='molly_reed', help="robustness metric",
                        choices=['molly_reed'])
    parser.add_argument("--niter", type=float, default=200, help="number of steps in experiment")
    parser.add_argument("--p", type=float, default=0.01, help="probability of selection",
                        choices=[0.01, 0.05, 0.1])

    return parser.parse_args()


def set_seed(seed=123456):
    random.seed(seed)
    np.random.seed(seed)


def generate_network(name):
    return nx.read_edgelist('./data/' + name + ".txt", create_using=nx.DiGraph(), nodetype = int)


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
