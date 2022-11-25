import datetime
import itertools
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from pylab import rcParams
from pymongo import MongoClient

from Build_reverse_identity_dictionary import Build_reverse_identity_dictionary

cluster = MongoClient("mongodb://localhost:27017")

db = cluster["smartshark"]

projectCollections = db["project"]
commit_with_projectInfo_Collection = db['commit_with_project_info']
file_action_Collection = db["file_action"]

total_developers_in_project = 0
# developerCommits = defaultdict(set)

BRID = Build_reverse_identity_dictionary()
BRID.reading_identity_and_people_and_building_reverse_identity_dictionary()

def getTotalDevelopers(projectName):
    projectDetails = projectCollections.find_one({"name": projectName})
    committersWithCount = commit_with_projectInfo_Collection.aggregate([
        {"$match": {"project_id_info.project_id": projectDetails['_id']}},
        {"$group": {"_id": "$author_id", "commitCount": {"$sum": 1}}}
    ])

    developersCommitCount = defaultdict(int)
    for entry in committersWithCount:
        developersCommitCount[BRID.reverse_identity_dict[entry['_id']]] += entry['commitCount']

    return len(developersCommitCount)


def findHeroDevsBasedOnCommits(projectName):
    projectDetails = projectCollections.find_one({"name": projectName})

    committersWithCount = commit_with_projectInfo_Collection.aggregate([
        {"$match": {"project_id_info.project_id": projectDetails['_id']}},
        {"$group": {"_id": "$author_id", "commitCount": {"$sum": 1}}}
    ])

    # Number of commits done by each developer in Kafka Project
    developersCommitCount = defaultdict(int)
    for entry in committersWithCount:
        developersCommitCount[BRID.reverse_identity_dict[entry['_id']]] += entry['commitCount']

    developersCommitCountList = []
    for key, value in developersCommitCount.items():
        developersCommitCountList.append([key, value])

    developersCommitCountList.sort(key=lambda x: x[1], reverse=True)

    totalCommitsInProject = commit_with_projectInfo_Collection.count_documents(
        {"project_id_info.project_id": projectDetails['_id']})
    print("Total Number of commits in Project :- ", totalCommitsInProject)

    percent80_commits = totalCommitsInProject * 0.8

    tempCommit = 0
    heroDevsBasedOnCommit = set()
    i = 0
    while (tempCommit <= percent80_commits):
        tempCommit += int(developersCommitCountList[i][1])
        heroDevsBasedOnCommit.add(developersCommitCountList[i][0])
        i += 1

    return heroDevsBasedOnCommit


"""**Task - 2 : Find the number of files updated by each Developer**
Find list of commits done by each developer
"""

def __get_developers_commits(project_id):
    developerCommits = defaultdict(set)
    commits = commit_with_projectInfo_Collection.find({"project_id_info.project_id": project_id})
    for commit in commits:
        developerCommits[BRID.reverse_identity_dict[commit['author_id']]].add(commit['_id'])
    return developerCommits

def findHeroDevsBasedOnFiles(projectName):
    projectDetails = projectCollections.find_one({"name": projectName})
    # Make data structure ->
    # {
    #     developer1 : [commit_1, commit_2, ....],
    #     developer2 : [commit_1, commit_2, ....],
    # }
    # Number of files updated by each developer
    developerFilesDict = defaultdict(int)
    developerCommits = __get_developers_commits(projectDetails["_id"])
    for developerId, commitList in developerCommits.items():
        for commitId in commitList:
            no_of_files_Modified = file_action_Collection.count_documents({"commit_id": {"$eq": commitId}})
            developerFilesDict[developerId] += no_of_files_Modified

    developerFilesCount = list(developerFilesDict.items())
    developerFilesCount.sort(key=lambda x: x[1], reverse=True)

    """Total File Modifications in Project"""
    totalFileModifications = 0
    for entry in developerFilesCount:
        totalFileModifications += entry[1]

    percent80_Files = totalFileModifications * 0.8

    tempFiles = 0
    heroDevsBasedOnFiles = set()
    i = 0
    while (tempFiles <= percent80_Files):
        tempFiles += int(developerFilesCount[i][1])
        heroDevsBasedOnFiles.add(developerFilesCount[i][0])
        i += 1

    return heroDevsBasedOnFiles


"""**Total Number of Lines Added overall (Only Lines added are considered)**

"""


def findHeroDevsBasedOnLines(projectName):
    # Make data structure ->
    # {
    #     developer1 : numberOfLinesAdded,
    #     developer2 : numberOfLinesAdded,
    # }
    """Find number of lines changed by each developer in each commmit"""

    developerLinesDict = defaultdict(int)
    projectDetails = projectCollections.find_one({"name": projectName})
    developerCommits = __get_developers_commits(projectDetails["_id"])
    for developerId, commitList in developerCommits.items():
        count = 0
        for commitId in commitList:
            temp = file_action_Collection.aggregate([{
                "$match": {
                    "commit_id": commitId
                }
            }, {
                "$group": {
                    "_id": {},
                    "sum_lines_added": {
                        "$sum": "$lines_added"
                    }
                }
            }, {
                "$project": {
                    "sum_lines_added": 1,
                    "_id": 0
                }
            }])

            for data in temp:
                count += data['sum_lines_added']

        developerLinesDict[developerId] = count

    developerLinesCount = list(developerLinesDict.items())
    developerLinesCount.sort(key=lambda x: x[1], reverse=True)

    """Total Lines added in Project Kafka"""

    totalLinesWritten = 0
    for devId, linescount in developerLinesDict.items():
        totalLinesWritten += linescount


    percent80_Lines = totalLinesWritten * 0.8

    tempLines = 0
    heroDevsBasedOnLines = set()
    i = 0
    while (tempLines <= percent80_Lines):
        tempLines += int(developerLinesCount[i][1])
        heroDevsBasedOnLines.add(developerLinesCount[i][0])
        i += 1

    return heroDevsBasedOnLines


def findOverallTechnicalDevelopers(projectName):
    heroDevsBasedOnCommit = findHeroDevsBasedOnCommits(projectName)
    heroDevsBasedOnFile = findHeroDevsBasedOnFiles(projectName)
    heroDevsBasedOnLine = findHeroDevsBasedOnLines(projectName)
    # """Apply set intersection to find overall technical heros"""
    ans = dict()
    ans["heroDevsBasedOnCommit"] = len(heroDevsBasedOnCommit)
    ans["heroDevsBasedOnFile"] = len(heroDevsBasedOnFile)
    ans["heroDevsBasedOnLine"] = len(heroDevsBasedOnLine)

    heroDevsOverall = heroDevsBasedOnLine.intersection(heroDevsBasedOnCommit, heroDevsBasedOnFile)
    print("Overall Technical Heros : ", len(heroDevsOverall))
    print("------------------------------------------")
    # print(heroDevsOverall)
    ans["heroDevsOverall"] = len(heroDevsOverall)
    ans["heroDevsList"] = heroDevsOverall
    return ans
