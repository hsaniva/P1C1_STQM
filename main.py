import NewComers
import socialHeroes
import socioTechnical_Heros
import technical_heroes
import technoSocialHeroes
from newcomers_relations_with_heroes import create_and_get_social_collaboration_dict_heroes, \
    newcomers_heroes_social_graphs_relation, correlation_of_degree_of_newcomer_becoming_heroes
from newcomers_social_collaboration_graph import create_and_get_social_collaboration_dict_newcomers
from superHeros import findSuperHeros


def get_new_comers(project_name):
    new_comers = NewComers.findNewComers(project_name)
    return new_comers

def print_new_comers(project_name):
    for new_comer in get_new_comers(project_name):
        print(new_comer)

def get_total_devs_in_project(project_name):
    print(technical_heroes.getTotalDevelopers(project_name))

# get_total_devs_in_project("kafka")

def get_technical_hero_devs_based_on_commit(project_name):
    return technical_heroes.findHeroDevsBasedOnCommits(project_name)

def print_technical_hero_devs_based_on_commit(project_name):
    totalDevs = technical_heroes.getTotalDevelopers(project_name)
    heroDevsBasedOnCommit = technical_heroes.findHeroDevsBasedOnCommits(project_name)

    print("Hero Developers : ", len(heroDevsBasedOnCommit))
    print("Total Developers in Project : ", totalDevs)
    print("Hero developer in Project by %: ", (len(heroDevsBasedOnCommit) / totalDevs) * 100)
    print(heroDevsBasedOnCommit)
    print("------------------------------------------------------------")

def get_technical_hero_devs_based_on_files(project_name):
    return technical_heroes.findHeroDevsBasedOnFiles(project_name)

def print_technical_hero_devs_based_on_files(project_name):
    totalDevs = technical_heroes.getTotalDevelopers(project_name)
    heroDevsBasedOnFiles = get_technical_hero_devs_based_on_files(project_name)
    print("Hero Developers : ", len(heroDevsBasedOnFiles))
    print("Total Developers in Project : ", totalDevs)
    print("Hero developer in project by % : ", (len(heroDevsBasedOnFiles) / totalDevs) * 100)
    print(heroDevsBasedOnFiles)
    print("--------------------------------------------------")

def get_technical_heroes_based_on_lines(project_name):
    return technical_heroes.findHeroDevsBasedOnLines(project_name)

def print_technical_heroes_based_on_lines(project_name):
    totalDevs = technical_heroes.getTotalDevelopers(project_name)
    heroDevsBasedOnLines = get_technical_heroes_based_on_lines(project_name)
    print("Hero Developers : ", len(heroDevsBasedOnLines))
    print("Total Developers in project : ", totalDevs)
    print("Hero developer in project by % : ", (len(heroDevsBasedOnLines) / totalDevs) * 100)
    print(heroDevsBasedOnLines)
    print("--------------------------------------------------")

def get_social_developers(project_name):
    return socialHeroes.findSocialHerosBasedOnComments(project_name)

def print_social_developers(project_name):
    totalDevs = technical_heroes.getTotalDevelopers(project_name)
    heroDevs = get_social_developers(project_name)
    print("Hero Devs : ", len(heroDevs))
    print("Total devs in Kafka : ", totalDevs)
    print("Dev percentage : ", (len(heroDevs) / totalDevs) * 100)
    print(heroDevs)
    print("--------------------------------------------------")

def get_technical_heroes(project_name):
    return technical_heroes.findOverallTechnicalDevelopers(project_name)

def print_technical_heroes(project_name):
    technical_heroes = get_technical_heroes(project_name)
    print("Total Technical Heroes : ", len(technical_heroes))
    print(technical_heroes)
    print("-------------------------------------")

def get_socio_technical_heroes(project_name):
    return socioTechnical_Heros.findSocioTechnicalHeros(project_name)

def print_socio_technical_heroes(project_name):
    socioTechnicalHeroes = get_socio_technical_heroes(project_name)
    print("Total number of socioTechnical Heros: ", len(socioTechnicalHeroes))
    print(socioTechnicalHeroes)

def get_techno_social_heroes(project_name):
    return technoSocialHeroes.findTechnoSocialHeroes(project_name)

def print_techno_social_heroes(project_name):
    technoSocialheros = get_techno_social_heroes(project_name)
    print("Total number of TechnoSocial Heros: ", len(technoSocialheros))
    print(technoSocialheros)

def get_super_heroes(project_name):
    return findSuperHeros(project_name)

def print_super_heroes(project_name):
    super_heroes = get_super_heroes(project_name)
    print("Super Heroes are : ", len(super_heroes))
    print(super_heroes)

def newcomer_degree_relation_due_to_heroes(project_name):
    return newcomers_heroes_social_graphs_relation(project_name)

def print_newcomer_degree_relation_due_to_heroes(project_name):
    for key, value in newcomer_degree_relation_due_to_heroes(project_name).items():
        print(key, value)

def get_correlation_of_degree_of_newcomer_becoming_heroes(project_name):
    return correlation_of_degree_of_newcomer_becoming_heroes(project_name)

def print_get_correlation_of_degree_of_newcomer_becoming_heroes(project_name):
    print("Correlation coefficient of newcomer degree ",
          get_correlation_of_degree_of_newcomer_becoming_heroes(project_name))

print_get_correlation_of_degree_of_newcomer_becoming_heroes("kafka")