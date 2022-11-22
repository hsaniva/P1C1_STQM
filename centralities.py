import networkx as nx

from newcomers_technical_collaboration_graph import createAndGetCollaborationDict
from newcomers_social_collaboration_graph import create_and_get_social_collaboration_dict
from networkx_utils import create_and_get_collaboration_graph

def eigenVectorCentralityForTechnicalCollab(projectName):
    d = createAndGetCollaborationDict(projectName)
    G = create_and_get_collaboration_graph(d)

    eigenCentralities = nx.eigenvector_centrality(G)

    for devId, centrality in eigenCentralities.items():
        print(devId ," -> ", centrality)
    return list(eigenCentralities.items())

def degreeCentralityForTechnicalCollab(projectName):
    d = createAndGetCollaborationDict(projectName)
    G = create_and_get_collaboration_graph(d)

    degreeCentralities = nx.degree_centrality(G)
    for devId, centrality in degreeCentralities.items():
        print(devId, " -> ", centrality)

    return degreeCentralities

def eigenVectorCentralityForSocialCollab(projectName):
    d = create_and_get_social_collaboration_dict(projectName)
    G = create_and_get_collaboration_graph(d)

    eigenCentralities = nx.eigenvector_centrality(G)

    for devId, centrality in eigenCentralities.items():
        print(devId ," -> ", centrality)
    return eigenCentralities

def degreeCentralityForSocialCollab(projectName):
    d = create_and_get_social_collaboration_dict(projectName)
    G = create_and_get_collaboration_graph(d)

    degreeCentralities = nx.degree_centrality(G)
    for devId, centrality in degreeCentralities.items():
        print(devId, " -> ", centrality)

    return degreeCentralities


print(degreeCentralityForTechnicalCollab("kafka"))
