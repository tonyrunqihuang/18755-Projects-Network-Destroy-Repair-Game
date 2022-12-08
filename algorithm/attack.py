import random
import numpy as np
import igraph as ig
import networkx as nx


class Attack():
    def __init__(self, G, p):
        """
        Initates the attack algorithm class

        Parameters:
        G (networkx type): the network
        p (float): probability of attack (i.e., the proportion of edges being attacked)

        Returns:
        self.G (networkx type): the network
        self.p (float): probability of attack
        self.num_edges (int): the total number of edges being attacked
        """

        self.G = G
        self.p = p
        self.num_edges = int(self.G.number_of_edges() * self.p)


    def random_attack(self):
        """
        Executes random attack by selecting p% of the edges at random and removes them from the network

        Returns:
        self.G (networkx type): the network after attack
        """

        edges = list(self.G.edges())

        if not edges:
            return self.G
        else:
            random_edge = random.sample(edges, self.num_edges)
            for edge in random_edge:
                self.G.remove_edge(edge[0], edge[1])
            return self.G


    def degree_attack(self):
        """
        Executes degree attack by the following process:
        1) Rank the nodes by its degree from high to low
        2) First attack the edges connected to the node with highest degree
        3) Then attack the edges connected to the node with second highest degree
        4) Continue until p% of the edges have been attacked

        Returns:
        self.G (networkx type): the network after attack
        """

        count = 0
        degree = sorted(self.G.degree, key=lambda x: x[1], reverse=True)
        
        for node in degree:
            edges = self.G.edges(node[0])

            for edge in list(edges):
                self.G.remove_edge(edge[0], edge[1])
                count += 1
            #     # print(count, self.num_edges)
                
                if count == self.num_edges:
                    break
            if count == self.num_edges:
                break

        return self.G


    def betweenness_attack(self):
        """
        Executes betweenness attack by the following process:
        1) Compute and rank the edge betweenness centrality of the network
        2) Remove p% of the edges with the highest edge betweenness centrality

        Returns:
        self.G (networkx type): the network after attack

        Notes: 
        1) to speed up computation on betweenness centrality, igraph is used to calcualte betweenness
        """

        nx.write_gml(self.G, 'network.gml')
        g = ig.Graph.Read_GML('network.gml')

        count = 0

        # Calculate the edge betweenness using igraph
        ig_edge_btw = ig.Graph.edge_betweenness(g)

        # Create corresponding list for edge betweenness
        nx_btw_ctr = {}
        edge_list = list(nx.edges(self.G))

        for i in range(len(edge_list)):
            nx_btw_ctr[edge_list[i]] = ig_edge_btw[i]

        # Sort the edge betweeness from high to low
        nx_btw_ctr_sorted = {k: v for k, v in sorted(nx_btw_ctr.items(), key=lambda item: item[1], reverse= True)}

        for edge in nx_btw_ctr_sorted:
            self.G.remove_edge(edge[0], edge[1])
            count += 1

            if count == self.num_edges:
                break

        return self.G