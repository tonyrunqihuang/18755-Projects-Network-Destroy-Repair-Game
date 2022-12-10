import os
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm
from utils.misc import *
from utils.plot import *
from utils.criterion import *
from algorithm.attack import *
from algorithm.defense import *


class Runner:
    def __init__(self, args):
        """
        Initiates the runner class for experiments, this will set the target network, attack and defense algorithm, 
        evaluation metric, and the directory to save the files.

        The argument (self.args) are imported from the misc.py file, while the attack and defense algorithms are imported
        from the "algorithm" folder

        Parameters: 
        args: the parameters used in the experiment
        """

        self.args = args
        self.name = self.args.network_name
        self.p = self.args.p
        self.n = self.args.niter
        self.algo_name = self.args.attack_algorithm + " Attack"+ " vs. " + self.args.defense_algorithm + " Defense"

        self.network = generate_network(self.name)
        self.num_edges = len(list(self.network.edges()))

        self.attack = Attack(self.network, self.p)
        self.defense = Defense(self.network, self.p, self.num_edges)

        self.metric = Robustness_metric(self.network)

        self.script_dir = os.path.dirname(__file__)
        self.results_dir = os.path.join(self.script_dir, 'experiment', self.name, self.algo_name, str(self.p))
        if not os.path.isdir(self.results_dir):
            os.makedirs(self.results_dir)


    def run(self):

        """
        Runs the experiments for a total of n (self.n) time steps, where at each time step one attack and 
        one defense move will be executed, and the Molloy-Reed value will be recorded after each attack and defense

        Returns: 
        molloy_reed (list of length 2*n): the Molloy-Reed value for each attack and defense
        """

        # Printing the network information and experiment setting
        print('Network information \n', nx.info(self.network))
        print('Initiating experiment on {}, p = {}, iterations = {}, attack = {}, defense = {}'.format(\
                self.name, self.p, self.n, self.args.attack_algorithm, self.args.defense_algorithm))

        molloy_reed = []
        val = self.metric.molloy_reed()
        molloy_reed.append(val)

        for i in tqdm(range(self.n)):

            if self.args.attack_algorithm == 'Random':
                self.network = self.attack.random_attack()
            elif self.args.attack_algorithm == 'Degree':
                self.network = self.attack.degree_attack()
            else:
                self.network = self.attack.betweenness_attack()
            val = self.metric.molloy_reed()
            molloy_reed.append(val)

            if self.args.defense_algorithm == 'Random':
                self.network = self.defense.random_defense()
            elif self.args.defense_algorithm == 'Degree':
                self.network = self.defense.degree_defense()
            else:
                self.network = self.defense.betweenness_defense()
            val = self.metric.molloy_reed()
            molloy_reed.append(val)

            if i % 10 == 0:
                print('Time step = {}, Molloy-Reed = {}'.format(i, val))
                deg_dist = degree_dist(self.network, self.results_dir, self.name, i)
                nx.write_gml(self.network, self.results_dir + '/visualization_t' + str(i) + '.gml')

            np.save(self.results_dir + '/molloy_reed_result', np.array(molloy_reed))
            mr = plot_mr_robustness(molloy_reed, self.results_dir, self.name)
            
        deg_dist = degree_dist(self.network, self.results_dir, self.name, i+1)
        nx.write_gml(self.network, self.results_dir + '/visualization_t' + str(self.args.niter) + '.gml')

        return molloy_reed
