import random
import argparse
import scipy.special
import numpy as np
import networkx as nx


def get_args():
    """
    Defining the parameters for the experiment, which include:
    1. seed (float): the random seed
    2. network_name (str): the name of the network
    3. attack_algorithm (str): the algorithm being used to remove edges
    4. defense_algorithm (str): the algorithm being used to add back edges
    5. criterion (str): the robustness metric being used
    6. niter (float): the total number of time steps for experiment
    7. p (float): the magnitude of attack and defense, which decides the number of edges that are attacked and defended

    Returns:
    parser.parse_args(): a collection of the arguments
    """

    parser = argparse.ArgumentParser("Experiment Hyperparamters")
    parser.add_argument("--seed", type=float, default=123456, help="random seed")
    parser.add_argument("--network_name", type=str, default='P2P network', help="network name",
                        choices=['P2P network'])
    parser.add_argument("--attack_algorithm", type=str, default='Random', help="attack algorithm name",
                        choices=['Random', 'Degree', 'Betweenness'])
    parser.add_argument("--defense_algorithm", type=str, default='Random', help="defense algorithm name",
                    choices=['Random', 'Degree', 'Betweenness'])
    parser.add_argument("--criterion", type=str, default='molloy_reed', help="robustness metric",
                        choices=['molloy_reed'])
    parser.add_argument("--niter", type=float, default=100, help="number of steps in experiment")
    parser.add_argument("--p", type=float, default=0.01, help="probability of selection",
                        choices=[0.01, 0.05, 0.1])

    return parser.parse_args()


def set_seed(seed=123456):

    """
    Setting the random seed for the experiment

    Parameters:
    seed (float): 1-dimensional torch tensor.
    """
    
    random.seed(seed)
    np.random.seed(seed)


def generate_network(name):

    """
    Generate the network by networkx

    Parameters:
    name (string): string of the name of the network

    Returns:
    network (networkx type): a networkx network
    """
    
    return nx.read_edgelist('./data/' + name + ".txt", create_using=nx.DiGraph(), nodetype = int)


def get_network_attr(G):

    """
    Analyze the key attributes of the network

    Parameters:
    G (networkx type): network from networkx

    Returns:
    nodes (float): the total number of nodes in the network
    edges (float): the total number of edges in the network
    avg_degree (float): the average degree of the network
    components (float): the total number of components in the network
    avg_cluster_coeff (float): the average clustering coefficient of the network
    global_cluster_coef (float): the global clustering coefficient of the network
    distance (float): the shortest distance of the network
    """

    # Number of nodes
    nodes = nx.number_of_nodes(G)

    # Number of edges
    edges = nx.number_of_edges(G)

    # The average degree
    degrees = [val for (node, val) in G.degree()]
    avg_degree = np.mean(degrees)

    # Number of components
    components = nx.number_connected_components(G)

    # Average and global clustering coefficients
    avg_cluster_coef = nx.average_clustering(G)
    triangles = sum(nx.triangles(G.to_undirected()).values()) / 3
    global_cluster_coef = 3 * triangles / np.sum([scipy.special.binom(i, 2) for i in degrees])

    # Distance of the graph
    distance = nx.average_shortest_path_length(G)

    return nodes, edges, avg_degree, components, avg_cluster_coef, global_cluster_coef, distance
