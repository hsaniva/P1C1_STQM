"""
Authors: Avinash Gaikwad, Sanghmitra Tamrakar, Neha Sarnaik, Ishan Srivastava
P1-C1
"""
import NewComers
import socialHeroes
import socioTechnical_Heros
import technical_heroes
import technoSocialHeroes
from centralities import eigenVectorCentralityForTechnicalCollab, eigenVectorCentralityForSocialCollab, \
    degreeCentralityForTechnicalCollab, degreeCentralityForSocialCollab
from newcomers_relations_with_heroes import create_and_get_social_collaboration_dict_heroes, \
    newcomers_heroes_social_graphs_relation, correlation_of_degree_of_newcomer_becoming_heroes
from newcomers_social_collaboration_graph import create_and_get_social_collaboration_dict_newcomers
from newcomers_technical_collaboration_graph import create_and_get_technical_collaboration_dict_newcomers
from superHeros import findSuperHeros



def get_new_comers(project_name):
    """
        Function for returning list of newcomers present in the project.
        :param project_name: Project name in string
        :return: list of newcomers present in the project
        :rtype: list
        """
    new_comers = NewComers.findNewComers(project_name)
    return new_comers

def print_new_comers(project_name):
    """
    Function for printing list of newcomers present in the project.
    :param project_name: Project name in string
    """
    for new_comer in get_new_comers(project_name):
        print(new_comer)

def get_total_devs_in_project(project_name):
    """
    Function for finding out the total number of developers present in the project.
    :returns: total number of developers present in the project.
    :rtype: integer
    :param project_name: Project name
    """
    print(technical_heroes.getTotalDevelopers(project_name))


def get_technical_hero_devs_based_on_commit(project_name):
    """
    Responsible for finding out the technical developers present in the project.
    :param project_name: Project name
    """
    return technical_heroes.findHeroDevsBasedOnCommits(project_name)

def print_technical_hero_devs_based_on_commit(project_name):
    """
    Prints the :get_technical_hero_devs_based_on_commit list
    :param project_name: Project name
    """
    totalDevs = technical_heroes.getTotalDevelopers(project_name)
    heroDevsBasedOnCommit = technical_heroes.findHeroDevsBasedOnCommits(project_name)

    print("Hero Developers : ", len(heroDevsBasedOnCommit))
    print("Total Developers in Project : ", totalDevs)
    print("Hero developer in Project by %: ", (len(heroDevsBasedOnCommit) / totalDevs) * 100)
    print(heroDevsBasedOnCommit)
    print("------------------------------------------------------------")

def get_technical_hero_devs_based_on_files(project_name):
    """
    Function for fetching the technical heroes based on files.
    :param project_name: Project name
    :return: Returns list of technical developers based on the files they changed.

    """
    return technical_heroes.findHeroDevsBasedOnFiles(project_name)

def print_technical_hero_devs_based_on_files(project_name):
    """
    Responsible for printing the technical heroes based on files.
    :param project_name: Project name
    """
    totalDevs = technical_heroes.getTotalDevelopers(project_name)
    heroDevsBasedOnFiles = get_technical_hero_devs_based_on_files(project_name)
    print("Hero Developers : ", len(heroDevsBasedOnFiles))
    print("Total Developers in Project : ", totalDevs)
    print("Hero developer in project by % : ", (len(heroDevsBasedOnFiles) / totalDevs) * 100)
    print(heroDevsBasedOnFiles)
    print("--------------------------------------------------")

def get_technical_heroes_based_on_lines(project_name):
    """
    Returns the technical heroes on the number of lines they committed.
    :param project_name: Project name
    :return: list of technical developers
    :rtype: list
    """
    return technical_heroes.findHeroDevsBasedOnLines(project_name)

def print_technical_heroes_based_on_lines(project_name):
    """
    Prints the technical heroes based on the number of lines committed.
    :param project_name: Project name
    """
    totalDevs = technical_heroes.getTotalDevelopers(project_name)
    heroDevsBasedOnLines = get_technical_heroes_based_on_lines(project_name)
    print("Hero Developers : ", len(heroDevsBasedOnLines))
    print("Total Developers in project : ", totalDevs)
    print("Hero developer in project by % : ", (len(heroDevsBasedOnLines) / totalDevs) * 100)
    print(heroDevsBasedOnLines)
    print("--------------------------------------------------")

def get_social_developers(project_name):
    """
    Returns the list of social developers
    :param project_name: Project name
    :return: list of developers
    """
    return socialHeroes.findSocialHerosBasedOnComments(project_name)

def print_social_developers(project_name):
    """
    Prints the list of social developers
    :param project_name: Project name
    """
    totalDevs = technical_heroes.getTotalDevelopers(project_name)
    heroDevs = get_social_developers(project_name)
    print("Hero Devs : ", len(heroDevs))
    print("Total devs in Kafka : ", totalDevs)
    print("Dev percentage : ", (len(heroDevs) / totalDevs) * 100)
    print(heroDevs)
    print("--------------------------------------------------")

def get_technical_heroes(project_name):
    """
    Returns a list of all kinds of(intersection) technical heroes
    :param project_name: Project name
    :return: list of overall developers
    """
    return technical_heroes.findOverallTechnicalDevelopers(project_name)

def print_technical_heroes(project_name):
    """
    Prints the list of heroes received from the function :get_technical_heroes
    :param project_name: Project name
    """
    technical_heroes = get_technical_heroes(project_name)
    print("Total Technical Heroes : ", len(technical_heroes))
    print(technical_heroes)
    print("-------------------------------------")

def get_socio_technical_heroes(project_name):
    """
    Returns a list of social-technical heroes present in the project.
    :param project_name: Project name
    :return: List of socio-technical developers
    """
    return socioTechnical_Heros.findSocioTechnicalHeros(project_name)

def print_socio_technical_heroes(project_name):
    """
    Prints the list of socio-technical developers received from :get_socio_technical_heroes function
    :param project_name: Project name
    """
    socioTechnicalHeroes = get_socio_technical_heroes(project_name)
    print("Total number of socioTechnical Heros: ", len(socioTechnicalHeroes))
    print(socioTechnicalHeroes)

def get_techno_social_heroes(project_name):
    """
    Returns the list of techno-social heroes present in the project.
    :param project_name: Project name
    :return: List of techno social heroes
    """
    return technoSocialHeroes.findTechnoSocialHeroes(project_name)

def print_techno_social_heroes(project_name):
    """
    Prints the list of techno-social heroes present in the project.
    :param project_name: Project name
    """
    technoSocialheros = get_techno_social_heroes(project_name)
    print("Total number of TechnoSocial Heros: ", len(technoSocialheros))
    print(technoSocialheros)

def get_super_heroes(project_name):
    """
    Returns the list of superheroes present in the project.
    :param project_name: Project name
    :return: list of heroes present in the project.
    """
    return findSuperHeros(project_name)

def print_super_heroes(project_name):
    """
    Prints the list received from :get_super_heroes function.
    :param project_name: Project name
    """
    super_heroes = get_super_heroes(project_name)
    print("Super Heroes are : ", len(super_heroes))
    print(super_heroes)

def newcomer_degree_relation_due_to_heroes(project_name):
    """
    Returns a dictionary which specifies the newcomers
    degree centrality change due to the introduction of heroes present in the project.
    :param project_name: Project name
    :return: dictionary having percentage change in degree centrality of newcomers.
    """
    return newcomers_heroes_social_graphs_relation(project_name)

def print_newcomer_degree_relation_due_to_heroes(project_name):
    """
    Simply prints the list of key value pairs received from :newcomer_degree_relation_due_to_heroes function.
    :param project_name: Project name
    """
    for key, value in newcomer_degree_relation_due_to_heroes(project_name).items():
        print(key, value)

def get_correlation_of_degree_of_newcomer_becoming_heroes(project_name):
    """
    Correlation coefficient of newcomers becoming heroes.
    :param project_name: Project name
    :return: Returns Correlation coefficient for newcomers who became heroes later on.
    """
    corr_coeff = correlation_of_degree_of_newcomer_becoming_heroes(project_name)
    return (corr_coeff[0][1] + corr_coeff[1][0])/2

def print_get_correlation_of_degree_of_newcomer_becoming_heroes(project_name):
    """
    Prints the correlation coefficient received from :get_correlation_of_degree_of_newcomer_becoming_heroes function.
    :param project_name: Project name
    """
    print("Correlation coefficient of newcomer degree ", get_correlation_of_degree_of_newcomer_becoming_heroes(project_name))

def eigenvector_centrality_of_newcomers_in_technical_collaboration(project_name):
    """
    Return list of eigenvector centrality for their technical collaboration.
    :param project_name: Project name
    :return: list of newcomers with eigenvector centralities
    """
    return eigenVectorCentralityForTechnicalCollab(project_name)

def eigenvector_centrality_of_newcomers_in_social_collaborations(project_name):
    """
    Return list of eigenvector centrality for their social collaboration.
    :param project_name: Project name
    :return:  list of newcomers with eigenvector centralities
    """
    return eigenVectorCentralityForSocialCollab(project_name)

def degree_centrality_of_newcomers_in_technical_collaboration(project_name):
    """
    Return list of degree centrality for their technical collaboration.
    :param project_name: Project name
    :return: list of newcomers with degree centralities
    """
    return degreeCentralityForTechnicalCollab(project_name)

def degree_centrality_of_newcomers_in_social_collaboration(project_name):
    """
    Returns degree centrality of newcomers in social collaborations
    :param project_name: Project name
    :return: degree centralities
    """
    return degreeCentralityForSocialCollab(project_name)