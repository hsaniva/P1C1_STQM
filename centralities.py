"""
Authors: Avinash Gaikwad, Sanghmitra Tamrakar, Neha Sarnaik, Ishan Srivastava
P1-C1
"""
import networkx as nx

from newcomers_social_collaboration_graph import create_and_get_social_collaboration_dict_newcomers
from networkx_utils import generate_graph


def find_degree_centrality(graph):
    """
    Finds out the degree centrality of the given graph.
    :param graph: networkx graph
    :return: returns the dictionary of devs and their corresponding centralities.
    """
    degreeCentralities = nx.degree_centrality(graph)
    for devId, centrality in degreeCentralities.items():
        print(devId, " -> ", centrality)

    return degreeCentralities

def find_eigenvector_centrality(graph):
    """
    Finds out the eigenvector centrality of the given graph.
    :param graph: networkx graph
    :return: returns the dictionary of devs and their corresponding centralities.
    """
    eigenCentralities = nx.eigenvector_centrality(graph)

    for devId, centrality in eigenCentralities.items():
        print(devId, " -> ", centrality)
    return list(eigenCentralities.items())


# def eigenVectorCentralityForTechnicalCollab(projectName):
#     d = create_and_get_technical_collaboration_dict_newcomers(projectName)
#     G = generate_graph(d)
#
#     eigenCentralities = nx.eigenvector_centrality(G)
#
#     for devId, centrality in eigenCentralities.items():
#         print(devId ," -> ", centrality)
#     return list(eigenCentralities.items())
#
# def degreeCentralityForTechnicalCollab(projectName):
#     d = create_and_get_technical_collaboration_dict_newcomers(projectName)
#     G = generate_graph(d)
#
#     degreeCentralities = nx.degree_centrality(G)
#     for devId, centrality in degreeCentralities.items():
#         print(devId, " -> ", centrality)
#
#     return degreeCentralities

def eigenVectorCentralityForSocialCollab(projectName):
    """
    Finds out eigen vector centrality for social collaboration graph.
    :param projectName: Project name
    :return: returns the dictionary of devs and their corresponding centralities.
    """
    d = create_and_get_social_collaboration_dict_newcomers(projectName)
    G = generate_graph(d)

    eigenCentralities = nx.eigenvector_centrality(G)

    for devId, centrality in eigenCentralities.items():
        print(devId ," -> ", centrality)
    return eigenCentralities

def degreeCentralityForSocialCollab(projectName):
    """
    Returns the degree centrality for the social collaboration graph.
    :param projectName: Project name
    :return: returns the dictionary of devs and their corresponding centralities.
    """
    d = create_and_get_social_collaboration_dict_newcomers(projectName)
    G = generate_graph(d)

    degreeCentralities = nx.degree_centrality(G)
    for devId, centrality in degreeCentralities.items():
        print(devId, " -> ", centrality)

    return degreeCentralities

