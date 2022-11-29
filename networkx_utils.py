"""
Authors: Avinash Gaikwad, Sanghmitra Tamrakar, Neha Sarnaik, Ishan Srivastava
P1-C1
"""
import networkx as nx
import numpy as np
from pylab import rcParams
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import itertools

def plot_graph(parentGraph):
    """
    Function for plotting the input graph beautifully.
    :param parentGraph: networkx graph
    """
    rcParams['figure.figsize'] = 14, 10
    pos = nx.spring_layout(parentGraph, scale=20, k=3 / np.sqrt(parentGraph.order()))
    d = dict(parentGraph.degree)
    nx.draw(parentGraph, pos,
            with_labels=True,
            nodelist=d,
            node_size=[d[k] * 100 for k in d])
    plt.show()


def generate_graph(dictionary):
    """
    Takes dictionary as input and generates graph
    :param dictionary: dictionary
    :return: networkx graph
    """
    parent_graph = nx.Graph()
    for key, devs in dictionary.items():
        temp_graph = nx.Graph()
        for dev in devs:
            temp_graph.add_node(dev)
        temp_graph.add_edges_from(itertools.combinations(list(devs), 2))
        parent_graph = nx.compose(parent_graph, temp_graph)
    return parent_graph
