import os
import networkx as nx
import numpy as np
from runner import Runner
from utils.misc import *


if __name__ == '__main__':
    set_seed()
    runner = Runner('social network', 2)
    result = runner.run()
