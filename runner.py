import sys
import math
import random
import scipy.special
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from utils.misc import *
from utils.plot import *
from utils.criterion import *
from algorithm.attack import *
from algorithm.defense import *


class Runner:
    def __init__(self, args):
        self.args = args
        self.name = self.args.network_name
        self.p = self.args.p

        self.network = generate_network(self.name)

        # I use self.p (i.e., the perecentage) as an input, instead of the actual number of edges to be removed
        self.attack = Attack(self.network, self.p)
        self.defense = Defense(self.network, self.p)

        self.metric = Robustness_metric(self.network)

        self.script_dir = os.path.dirname(__file__)
        self.results_dir = os.path.join(self.script_dir, 'experiment', self.name, str(self.p))
        if not os.path.isdir(self.results_dir):
            os.makedirs(self.results_dir)


    def run(self):

        print('Initiating experiment on {}'.format(self.name))
        print('Network information \n', nx.info(self.network))

        molly_reed = []

        for i in range(int(self.args.niter)):

            if self.args.algorithm == 'random':

                self.network = self.attack.random_attack()
                val = self.metric.molly_reed()
                molly_reed.append(val)

                self.network = self.defense.random_defense()
                val = self.metric.molly_reed()
                molly_reed.append(val)

            elif self.args.algorithm == 'smart':
                self.network = self.attack.smart_attack(self.p)
                self.network = self.defense.smart_defense()

            if i % 100 == 0:
                degree_dist(self.network, self.results_dir, self.name, i)
                nx.write_gml(self.network, self.results_dir + '/visualization_t' + str(i) + '.gml')

        np.save(self.results_dir + '/mollye_reed_result', np.array(molly_reed))
        plot_mr_robustness(molly_reed, self.results_dir, self.name)
        degree_dist(self.network, self.results_dir, self.name, i)
        nx.write_gml(self.network, self.results_dir + '/visualization_t' + str(self.args.niter) + '.gml')

        return molly_reed
