"""
Authors: Avinash Gaikwad, Sanghmitra Tamrakar, Neha Sarnaik, Ishan Srivastava
P1-C1
"""
from collections import defaultdict
from pymongo import MongoClient
from Build_reverse_identity_dictionary import Build_reverse_identity_dictionary

cluster = MongoClient("mongodb://localhost:27017")
db = cluster["smartshark"]

projectCollections = db["project"]
commit_with_projectInfo_Collection = db['commit_with_project_info']
file_action_Collection = db["file_action"]

total_developers_in_project = 0

BRID = Build_reverse_identity_dictionary()
BRID.reading_identity_and_people_and_building_reverse_identity_dictionary()

def getTotalDevelopers(projectName):
    """
    Returns the total developers
    :param projectName: Project name
    :return: total developers
    """
    projectDetails = projectCollections.find_one({"name": projectName})
    committers = commit_with_projectInfo_Collection.aggregate([
        {"$match": {"project_id_info.project_id": projectDetails['_id']}},
        {"$group": {"_id": "$author_id"}}
    ])

    total_devs_in_project = set()
    for a in committers:
        total_devs_in_project.add(BRID.reverse_identity_dict[a["_id"]])
    return len(total_devs_in_project)


def findHeroDevsBasedOnCommits(projectName):
    """
    Returns list of hero developers based on their
    :param projectName: Project name
    :return: list of hero devs
    """
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
    # print("Total Number of commits in Project :- ", totalCommitsInProject)

    percent80_commits = totalCommitsInProject * 0.8

    tempCommit = 0
    heroDevsBasedOnCommit = set()
    i = 0
    while (tempCommit <= percent80_commits):
        tempCommit += int(developersCommitCountList[i][1])
        heroDevsBasedOnCommit.add(developersCommitCountList[i][0])
        i += 1

    return heroDevsBasedOnCommit


def __get_developers_commits(project_id):
    """
    Returns all the commits made for a project
    :param project_id: ID for the project.
    :return: Cursor object for the list of commits.
    """
    developerCommits = defaultdict(set)
    commits = commit_with_projectInfo_Collection.find({"project_id_info.project_id": project_id})
    for commit in commits:
        developerCommits[BRID.reverse_identity_dict[commit['author_id']]].add(commit['_id'])
    return developerCommits

def findHeroDevsBasedOnFiles(projectName):
    """
    Returns list of hero devs based on files
    :param projectName: Project name
    :return: list of devs based on files
    """
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


def findHeroDevsBasedOnLines(projectName):
    """
    Finds list of hero developers based on the lines of code that they committed.
    :param projectName: Project name
    :return: hero devs list
    """
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
    """
    Returns the list of developers that are heroes in all sectors.
    :param projectName: Project name
    :return: list of overall technical developers
    """
    heroDevsBasedOnCommit = findHeroDevsBasedOnCommits(projectName)
    heroDevsBasedOnFile = findHeroDevsBasedOnFiles(projectName)
    heroDevsBasedOnLine = findHeroDevsBasedOnLines(projectName)
    # """Apply set intersection to find overall technical heros"""
    heroDevsOverall = heroDevsBasedOnLine.intersection(heroDevsBasedOnCommit, heroDevsBasedOnFile)

    return heroDevsOverall
