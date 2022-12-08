import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def plot_mr_robustness(data, dir, name):

    """
    Plotting the robustness against the time steps

    Parameters:
    data (list): the robustness value
    dir (str): the directory to save the graph
    name (str): the name of network, for the caption in the graph

    Returns:
    data (list): the robustness value
    """

    t = np.arange(len(data))
    plt.figure()
    plt.plot(t, data, '-')
    plt.title('Robustness of ' + name)
    plt.xlabel('Time Step (t)')
    plt.ylabel('Molly-Reed Criteration')
    plt.savefig(dir + "/molly reed_result.png", format="PNG")
    plt.close()

    return data


def degree_dist(network, dir, name, time):

    """
    Plotting the network's degree distribution at time t

    Parameters:
    network (networkx file): the network to be analyzed
    dir (str): the directory to save the graph
    name (str): the name of network
    time (float): the time step that is being analyzed

    Returns:
    y (list): the network's degree distribution
    """

    y = nx.degree_histogram(network)
    x = np.arange(len(y)).tolist()
    plt.figure()
    plt.plot(x, y, 'o')
    plt.title('Degree distribution of ' + name)
    plt.xlabel('Node degree')
    plt.ylabel('Frequency (number of nodes)')
    plt.savefig(dir + "/degree dist_t" + str(time) + ".png", format="PNG")
    plt.close()
    np.save(dir + '/degree dist_t' + str(time), y)

    return y
