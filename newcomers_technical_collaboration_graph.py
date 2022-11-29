"""
Authors: Avinash Gaikwad, Sanghmitra Tamrakar, Neha Sarnaik, Ishan Srivastava
P1-C1
"""
from collections import defaultdict

from Build_reverse_identity_dictionary import Build_reverse_identity_dictionary
from NewComers import findNewComers
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017")
db = cluster["smartshark"]
commit_with_project_info = db["commit_with_project_info"]
file_action = db["file_action"]
file = db["file"]

BRID = Build_reverse_identity_dictionary()
BRID.reading_identity_and_people_and_building_reverse_identity_dictionary()

def create_and_get_technical_collaboration_dict_newcomers(projectName):
    """
    Fetches list of newcomers, finds out all of their commits in the files and creates a
    dictionary where key is the common file name and value is the list of newcomers
    :param projectName: Project name
    :return: dictionary(file, [list of newcomers])
    """
    newComers = findNewComers(projectName)
    file_devs_dict = defaultdict(set)

    for newComer in newComers:
        for temp in BRID.identity_dict[newComer]:
            commits_ids = commit_with_project_info.find({"author_id": temp}, {"_id": 1})
            for commit_id in commits_ids:

                file_ids = file_action.find({"commit_id": commit_id["_id"]}, {"file_id": 1})
                for file_id in file_ids:
                    file_name = file.find_one({"_id": file_id["file_id"]}, {"path": 1})
                    file_name = file_name["path"].split("/")[-1]
                    file_devs_dict[file_name].add(temp)
    return file_devs_dict

