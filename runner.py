import sys
import math
import random
import scipy.special
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from utils.misc import *
from utils.criterion import *


class Runner:
    def __init__(self, name, niter):
        self.name = name
        self.G = generate_network(name)
        self.n = niter

    def run(self):

        molly_reed = []

        for i in range(self.n):
            self.G = random_attack(self.G)
            self.G = random_defense(self.G)
            val = molly_reed_criterion(self.G)
            molly_reed.append(val)

        return molly_reed
