import datetime
import itertools
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from pylab import rcParams
from pymongo import MongoClient

from Build_reverse_identity_dictionary import Build_reverse_identity_dictionary
from technical_heroes import findOverallTechnicalDevelopers

# import socialheroes


cluster = MongoClient("mongodb://localhost:27017")
db = cluster["smartshark"]
projectCollection = db["project"]
commit_with_projectInfo_Collection = db['commit_with_project_info']
file_action_Collection = db["file_action"]
comments_with_issue_and_project_info_collection = db["comments_with_issue_and_project_info"]
issue_with_project_info_collection = db['issue_with_project_info']
BRID = Build_reverse_identity_dictionary()
BRID.reading_identity_and_people_and_building_reverse_identity_dictionary()

def findMedian(l):
    # print("Developer comment length : ", len(l))
    mid = len(l) // 2
    median = (l[mid][1] + l[~mid][1]) / 2
    return median


def findTechnoSocialHeroes(projectName):
    projectDetails = projectCollection.find_one({"name": projectName})
    # print(projectDetails)
    techHeros = findOverallTechnicalDevelopers(projectName)

    # Social Contribution
    comments = comments_with_issue_and_project_info_collection.find(
        {
            "issue_info.project_id_info.project_id": projectDetails['_id']
        },
        {"author_id": 1}
    )

    authorCommentCountDict = defaultdict(int)

    for comment in comments:
        authorCommentCountDict[BRID.reverse_identity_dict[comment['author_id']]] += 1
    totalCommentsInProject = comments_with_issue_and_project_info_collection.count_documents(
        {"issue_info.project_id_info.project_id": projectDetails['_id']})

    # Sort the dev lists
    developerCommentCounts = list(authorCommentCountDict.items())
    developerCommentCounts.sort(key=lambda x: x[1], reverse=True)

    # print("Developer Comment Count list :- ", developerCommentCounts)
    median = findMedian(developerCommentCounts)
    socialHerosAboveMedian = set()

    i = 0
    while developerCommentCounts[i][1] > median and i < len(developerCommentCounts):
        socialHerosAboveMedian.add(developerCommentCounts[i][0])
        i += 1

    technoSocialheros = socialHerosAboveMedian.intersection(techHeros)
    return technoSocialheros