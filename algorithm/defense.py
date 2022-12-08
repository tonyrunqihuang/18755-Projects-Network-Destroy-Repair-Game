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

        # Random defense proceeds as followed:
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
        # 1) Sort the nodes by the highest degree and highest betweenness and select the top p% of nodes for both
        # 2) For each of the highest betweenness nodes, choose an node based on degree and add an edge if there none
        # 3) Continue until the number of removed edges are added back
            
        nx.write_gml(self.G, 'network.gml')
        g = ig.Graph.Read_GML('network.gml')
        
        #computing node betweenness
        ig_node_btw = ig.Graph.betweenness(g)
        
        nx_btw_ctr = {}
        node_list = list(nx.nodes(self.G))

        for i in range(len(node_list)):
            nx_btw_ctr[node_list[i]] = ig_node_btw[i]


        degree = [k for k, v in sorted(self.G.degree, key=lambda x: x[1], reverse=True)]
        betweenness = [k for k, v in sorted(nx_btw_ctr.items(), key=lambda x: x[1], reverse=True)]

        #sorting p nodes with highest betweenness
        node_betweenness_select = betweenness[:(int(len(betweenness) * self.p))]
        num_nodes = len(degree)
        j = 0
        i = self.G.number_of_edges()
    
        while(1):

          if  i == self.num_edges:
            break
         
          for node in node_betweenness_select:

             
             while(1): #to prevent self linkage
              second_node = degree[j] #second node is selected from p highest degrees list 
              if second_node != node:
                  break
              else:
                  j+=1
                  if j == num_nodes:
                    j = 0
            
             
             if self.G.has_edge(node, second_node) == False:

                self.G.add_edge(node, second_node)
                i+=1
                j+=1

                if  i == self.num_edges:
                  break

                if j == num_nodes:
                    j = 0

          if  i == self.num_edges:
             break

          j+=1

        return self.G