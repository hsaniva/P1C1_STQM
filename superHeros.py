from pymongo import MongoClient

from socioTechnical_Heros import findSocioTechnicalHeros
from technical_heroes import findOverallTechnicalDevelopers
from socialHeroes import  findSocialHerosBasedOnComments
from technoSocialHeroes import findTechnoSocialHeroes

cluster = MongoClient("mongodb://localhost:27017")
db = cluster["smartshark"]
project = db['project']

def findSuperHeros(projectName):
    # techHeros = findOverallTechnicalDevelopers(projectName)
    # socialHeroes = findSocialHerosBasedOnComments(projectName)
    #
    # superHeros = techHeros["heroDevsList"].intersection(socialHeroes["social_hero_list"])
    # print("Total number of superheros in Project ", projectName, " : ", len(superHeros))
    # # print(superHeros)
    # return superHeros

    SocioTechnicalHeros = findSocioTechnicalHeros(projectName)
    TechnoSocialHeroes = findTechnoSocialHeroes(projectName)

    superHeros = SocioTechnicalHeros.intersection(TechnoSocialHeroes)
    return superHeros




