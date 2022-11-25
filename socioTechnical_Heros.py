from collections import defaultdict

from pymongo import MongoClient

from Build_reverse_identity_dictionary import Build_reverse_identity_dictionary
from technical_heroes import findOverallTechnicalDevelopers
from socialHeroes import findSocialHerosBasedOnComments


cluster = MongoClient("mongodb://localhost:27017")
db = cluster["smartshark"]
projectCollection = db["project"]
commit_with_projectInfo_Collection = db['commit_with_project_info']

BRID = Build_reverse_identity_dictionary()
BRID.reading_identity_and_people_and_building_reverse_identity_dictionary()

def findMedian(l):
    # print("Developer comment length : ", len(l))
    mid = len(l) // 2
    median = (l[mid][1] + l[~mid][1]) / 2
    return median

def findSocioTechnicalHeros(projectName):
    socialHeroes = findSocialHerosBasedOnComments(projectName)
    projectDetails = projectCollection.find_one({"name": projectName})
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

    median = findMedian(developersCommitCountList)
    technicalHerosAboveMedian = set()

    i = 0
    while developersCommitCountList[i][1] > median and i < len(developersCommitCountList):
        technicalHerosAboveMedian.add(developersCommitCountList[i][0])
        i += 1

    socioTechnicalHeros = technicalHerosAboveMedian.intersection(socialHeroes)
    return socioTechnicalHeros
