import itertools
from collections import defaultdict

import networkx as nx
import numpy as np
from bson import ObjectId
from pylab import rcParams
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from NewComers import findNewComers
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017")
db = cluster["smartshark"]
commit_with_project_info = db["commit_with_project_info"]
file_action = db["file_action"]
file = db["file"]

def createAndGetCollaborationGraph(projectName):
    newComers = findNewComers(projectName)
    file_devs_dict = defaultdict(set)

    for newComer in newComers:
        commits_ids = commit_with_project_info.find({"author_id": newComer}, {"_id": 1})
        for commit_id in commits_ids:
            file_ids = file_action.find({"commit_id": commit_id["_id"]}, {"file_id": 1})
            for file_id in file_ids:
                file_name = file.find_one({"_id": file_id["file_id"]}, {"path":1})
                file_name = file_name["path"].split("/")[-1]
                file_devs_dict[file_name].add(newComer)
    return file_devs_dict

def beatifulGraph(parentGraph):
    rcParams['figure.figsize'] = 14, 10
    pos = nx.spring_layout(parentGraph, scale=20, k=3/np.sqrt(parentGraph.order()))
    d = dict(parentGraph.degree)
    nx.draw(parentGraph, pos,
            with_labels=True,
            nodelist=d,
            node_size=[d[k]*100 for k in d])
    plt.show()
def create_and_plot_graph(G):
    parent_graph = nx.Graph()

    for fileName, devs in G.items():
        temp_graph = nx.Graph()
        # temp_graph.add_nodes_from(list(devs))
        for dev in devs:
            temp_graph.add_node(dev)
        temp_graph.add_edges_from(itertools.combinations(list(devs), 2))
        parent_graph = nx.compose(parent_graph, temp_graph)
    # nx.draw(parent_graph, with_labels=True, font_weight='bold')
    # plt.show()
    beatifulGraph(parent_graph)
create_and_plot_graph(createAndGetCollaborationGraph("kafka"))