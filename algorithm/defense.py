import random
import numpy as np
import igraph as ig
import networkx as nx


class Defense():
    def __init__(self, G, p, num_edges):
        self.G = G
        self.p = p
        self.num_edges = num_edges


    def random_defense(self):

        # Random defense proceeds as followed
        # 1) Select two nodes at random
        # 2) Add an edge between them if there is none, until the same number of removed edges are added back

        nodes = list(self.G.nodes())

        if not nodes:
            return self.G

        else:
            i = 0

            while(1):

                random_nodes = random.sample(nodes, 2)
                if self.G.has_edge(random_nodes[0], random_nodes[1]) == False:
                    self.G.add_edge(random_nodes[0], random_nodes[1])
                    i+=1
                if i == int(self.p * self.num_edges):
                    break

            return self.G


    def degree_defense(self):

        # Degree defense proceeds as followed:
        # 1) Sort the nodes by the highest degree and select the top  p% of nodes
        # 2) For each of the selected nodes, randomly choose an unselected node and add an edge if there none
        # 3) Continue until the number of removed edges are added back

        degree = sorted(self.G.degree, key=lambda x: x[1], reverse=True)
        node_select = degree[:(int(len(degree) * self.p))]
        node_not_select = degree[(int(len(degree) * self.p)):]

        i = self.G.number_of_edges()

        while(1):

          for node in node_select:

             random_node = random.sample(node_not_select, 1)

             if self.G.has_edge(node[0], random_node[0][0]) == False:

                self.G.add_edge(node[0], random_node[0][0])
                i+=1
                if  i == self.num_edges:
                  break

          if  i == self.num_edges:
             break

        return self.G


        def betweenness_defense(self):

            # Degree defense proceeds as followed:
            # 1) Sort the nodes by the highest degree and select the top  p% of nodes
            # 2) For each of the selected nodes, choose an unselected node based on betweenness and add an edge if there none
            # 3) Continue until the number of removed edges are added back

            return self.G
