from collections import defaultdict

from pymongo import MongoClient
from NewComers import findNewComers

cluster = MongoClient("mongodb://localhost:27017")
db = cluster["smartshark"]
issue_comment = db["issue_comment"]

def create_and_get_social_collaboration_dict(project_name):
    issue_new_comer = defaultdict(set)
    new_comers = findNewComers(project_name)
    for new_comer in new_comers:
        issue_ids = issue_comment.find({"author_id": new_comer}, {"issue_id":1})
        for issue_id in issue_ids:
            issue_new_comer[issue_id["issue_id"]].add(new_comer)
    return issue_new_comer