import networkx as nx

from newcomers_technical_collaboration_graph import create_and_get_technical_collaboration_dict_newcomers
from newcomers_social_collaboration_graph import create_and_get_social_collaboration_dict_newcomers
from networkx_utils import generate_graph


def find_degree_centrality(graph):
    degreeCentralities = nx.degree_centrality(graph)
    for devId, centrality in degreeCentralities.items():
        print(devId, " -> ", centrality)

    return degreeCentralities

def find_eigenvector_centrality(graph):
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
    d = create_and_get_social_collaboration_dict_newcomers(projectName)
    G = generate_graph(d)

    eigenCentralities = nx.eigenvector_centrality(G)

    for devId, centrality in eigenCentralities.items():
        print(devId ," -> ", centrality)
    return eigenCentralities

def degreeCentralityForSocialCollab(projectName):
    d = create_and_get_social_collaboration_dict_newcomers(projectName)
    G = generate_graph(d)

    degreeCentralities = nx.degree_centrality(G)
    for devId, centrality in degreeCentralities.items():
        print(devId, " -> ", centrality)

    return degreeCentralities

