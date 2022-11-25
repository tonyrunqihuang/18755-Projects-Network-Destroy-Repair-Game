import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def plot_mr_robustness(data, dir, name):

    # Plotting network robutsness vs. time

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

    # Plotting the degree distribution at time t

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
