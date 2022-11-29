"""
Authors: Avinash Gaikwad, Sanghmitra Tamrakar, Neha Sarnaik, Ishan Srivastava
P1-C1
"""
from pymongo import MongoClient

from socioTechnical_Heros import findSocioTechnicalHeros
from technoSocialHeroes import findTechnoSocialHeroes

cluster = MongoClient("mongodb://localhost:27017")
db = cluster["smartshark"]
project = db['project']

def findSuperHeros(projectName):
    """
    Return list of heroes that are both technical heroes and social hero for a
    particular project.
    :param projectName: Project name
    :return: list of super heroes
    """
    SocioTechnicalHeros = findSocioTechnicalHeros(projectName)
    TechnoSocialHeroes = findTechnoSocialHeroes(projectName)

    superHeroes = SocioTechnicalHeros.intersection(TechnoSocialHeroes)
    return superHeroes




