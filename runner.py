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
        self.name = self.args.network
        self.p = self.args.p

        self.network = generate_network(self.name)

        self.attack = Attack(self.network, self.args.n_edge)
        self.defense = Defense(self.network, self.args.n_edge)

        self.metric = Robustness_metric(self.network)

        self.script_dir = os.path.dirname(__file__)
        self.results_dir = os.path.join(self.script_dir, 'experiment', self.name)
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
                #print(molly_reed)
                self.network = self.defense.random_defense()
                val = self.metric.molly_reed()
                molly_reed.append(val)

            elif self.args.algorithm == 'smart':
                self.network = self.attack.smart_attack(self.p)
                self.network = self.defense.smart_defense()
            
            if i % 100 == 0:
                plot_mr_robustness(molly_reed, self.results_dir, self.name)
                degree_dist(self.network, self.results_dir, self.name, i)

        plot_mr_robustness(molly_reed, self.results_dir, self.name)
        degree_dist(self.network, self.results_dir, self.name, i)

        return molly_reed
