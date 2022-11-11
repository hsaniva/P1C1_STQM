from collections import defaultdict
from NewComers import findNewComers
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017")
db = cluster["smartshark"]
commit_with_project_info = db["commit_with_project_info"]
file_action = db["file_action"]
file = db["file"]


def createAndGetCollaborationDict(projectName):
    newComers = findNewComers(projectName)
    file_devs_dict = defaultdict(set)

    for newComer in newComers:
        commits_ids = commit_with_project_info.find({"author_id": newComer}, {"_id": 1})
        for commit_id in commits_ids:
            file_ids = file_action.find({"commit_id": commit_id["_id"]}, {"file_id": 1})
            for file_id in file_ids:
                file_name = file.find_one({"_id": file_id["file_id"]}, {"path": 1})
                file_name = file_name["path"].split("/")[-1]
                file_devs_dict[file_name].add(newComer)
    return file_devs_dict

