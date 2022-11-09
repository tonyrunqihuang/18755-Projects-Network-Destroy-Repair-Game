import random
import numpy as np
import networkx as nx


class Defense():
    def __init__(self, G, p, num_edges):
        self.G = G
        self.p = p
        self.num_edges = num_edges

    def random_defense(self):

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

    def smart_defense(self):
        
        
        degree = sorted(self.G.degree, key=lambda x: x[1], reverse=True)
        node_select = degree[:(int(len(degree) * self.p))]
        print((node_select))
        node_not_select = degree[(int(len(degree) * self.p)):]
        print("v")
        print(len(node_not_select))
        i = 0
       
        '''
        while(1):

         for node in node_select:

            random_node = random.sample(node_not_select, 1)
            print("r")
            print(node)
            
            #print(random_node)
        
            if self.G.has_edge(node[0], random_node[0]) == False:
                self.G.add_edge(node[0], random_node[0])
                i+=1
                print("i2")
                print(i)
                        
         if i == int(self.p * self.num_edges):
           break
        '''
        return self.G
