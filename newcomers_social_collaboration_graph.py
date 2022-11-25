from collections import defaultdict

from pymongo import MongoClient

from Build_reverse_identity_dictionary import Build_reverse_identity_dictionary
from NewComers import findNewComers

BRID = Build_reverse_identity_dictionary()
BRID.reading_identity_and_people_and_building_reverse_identity_dictionary()

cluster = MongoClient("mongodb://localhost:27017")
db = cluster["smartshark"]
issue_comment = db["issue_comment"]
project = db['project']

def create_and_get_social_collaboration_dict_newcomers(project_name):
    issue_new_comer = defaultdict(set)
    new_comers = findNewComers(project_name)
    for new_comer in new_comers:
        for temp in BRID.identity_dict[new_comer]:
            issue_ids = issue_comment.find({"author_id": temp}, {"issue_id": 1})
            for issue_id in issue_ids:
                issue_new_comer[issue_id["issue_id"]].add(new_comer)
    return issue_new_comer