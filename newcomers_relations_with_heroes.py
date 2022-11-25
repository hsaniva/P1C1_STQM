from collections import defaultdict

import networkx as nx
import numpy as np
from pymongo import MongoClient

from Build_reverse_identity_dictionary import Build_reverse_identity_dictionary
from NewComers import findNewComers
from centralities import find_degree_centrality
from networkx_utils import generate_graph
from newcomers_social_collaboration_graph import create_and_get_social_collaboration_dict_newcomers
from socialHeroes import findSocialHerosBasedOnComments
from socioTechnical_Heros import findSocioTechnicalHeros
from superHeros import findSuperHeros
from technical_heroes import findOverallTechnicalDevelopers
from technoSocialHeroes import findTechnoSocialHeroes

BRID = Build_reverse_identity_dictionary()
BRID.reading_identity_and_people_and_building_reverse_identity_dictionary()

cluster = MongoClient("mongodb://localhost:27017")
db = cluster["smartshark"]
issue_comment = db["issue_comment"]

def create_and_get_social_collaboration_dict_heroes(project_name):
    issue_devs = defaultdict(set)
    devs = findOverallTechnicalDevelopers(project_name)\
        .union(findSocialHerosBasedOnComments(project_name))\
        .union(findTechnoSocialHeroes(project_name))\
        .union(findSocioTechnicalHeros(project_name))

    for dev in devs:
        for temp in BRID.identity_dict[dev]:
            issue_ids = issue_comment.find({"author_id": temp}, {"issue_id":1})
            for issue_id in issue_ids:
                issue_devs[issue_id["issue_id"]].add(dev)
    return issue_devs


def newcomers_heroes_social_graphs_relation(projectName):
    newcomers_dict = create_and_get_social_collaboration_dict_newcomers(projectName)
    heroes_dict = create_and_get_social_collaboration_dict_heroes(projectName)

    g1 = generate_graph(newcomers_dict)
    degree_centralities_g1 = find_degree_centrality(g1)

    g2 = generate_graph(heroes_dict)
    g3 = nx.compose(g1, g2)

    degree_centralities_g3 = find_degree_centrality(g3)

    final_dict = {x:degree_centralities_g1[x] for x in degree_centralities_g1 if x in degree_centralities_g3}
    final_ans_dict = defaultdict(float)
    for key, value in final_dict.items():
        val1 = degree_centralities_g1[key]
        val2 = degree_centralities_g3[key]
        if max(val1, val2) == 0:
            final_ans_dict[key] = 0
        else:
            final_ans_dict[key] = (abs(val2 - val1)/max(val1, val2))*100
    return final_ans_dict

def correlation_of_degree_of_newcomer_becoming_heroes(projectName):
    newcomers_dict = create_and_get_social_collaboration_dict_newcomers(projectName)
    heroes_dict = create_and_get_social_collaboration_dict_heroes(projectName)

    g1 = generate_graph(newcomers_dict)
    degree_centralities_g1 = find_degree_centrality(g1)

    g2 = generate_graph(heroes_dict)
    g3 = nx.compose(g1, g2)

    degree_centralities_g3 = find_degree_centrality(g3)

    final_dict = {x:degree_centralities_g1[x] for x in degree_centralities_g1 if x in degree_centralities_g3}
    x_list = []
    y_list = []

    for key, value in final_dict.items():
        x_list.append(degree_centralities_g1[key])
        y_list.append(degree_centralities_g3[key])
    return np.corrcoef(x_list, y_list)
