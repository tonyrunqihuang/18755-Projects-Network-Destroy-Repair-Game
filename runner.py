import sys
import math
import random
import scipy.special
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from utils.misc import *
from utils.criterion import *
from algorithm.attack import *


class Runner:
    def __init__(self, name, niter):
        self.name = name
        self.G = generate_network(name)
        self.n = niter

        self.script_dir = os.path.dirname(__file__)
        self.results_dir = os.path.join(self.script_dir, 'experiment', self.name)

        if not os.path.isdir(self.results_dir):
            os.makedirs(self.results_dir)


    def run(self):

        molly_reed = []
        for i in range(self.n):
            self.G = random_attack(self.G, 1)
            # self.G = random_defense(self.G)
            val = molly_reed_criterion(self.G)
            molly_reed.append(val)

        # Plotting network robutsness vs. time
        t = np.arange(len(molly_reed))
        plt.figure()
        plt.plot(t, molly_reed, '-')
        plt.title('Robustness of ' + self.name)
        plt.xlabel('Time Step (t)')
        plt.ylabel('Molly-Reed Criteration')
        plt.savefig(self.results_dir + "/molly reed_result.png", format="PNG")

        # Plotting the degree distribution
        # y = nx.degree_histogram(self.G)
        # x = np.arange(len(y)).tolist()
        # plt.plot(x, y, 'o')
        # plt.title('Degree distribution of ' + self.name)
        # plt.xlabel('Node degree')
        # plt.ylabel('Frequency (number of nodes)')
        # plt.savefig(self.results_dir + "/degree dist.png", format="PNG")
        # plt.show()

        return molly_reed
