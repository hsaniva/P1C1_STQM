from technical_heroes import findOverallTechnicalDevelopers
from socialHeroes import findSocialHerosBasedOnComments
from technoSocialHeroes import findTechnoSocialHerosBasedOnComments
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017")
db = cluster["smartshark"]
project = db['project']
commit_with_project_info = db['commit_with_project_info']

# for a in project.find({}):
#     print(a["name"])
#     print(findSocialHerosBasedOnComments(a["name"]))

# findOverallTechnicalDevelopers("kafka")
projectList = ["freemarker","httpcomponents-core","httpcomponents-client","santuario-java",
               "commons-bcel", "commons-vfs", "commons-validator", "commons-io",
               "commons-collections", "xerces2-j"]

for a in projectList:
    print("=====================================")
    print(a)
    print("=====================================")
    findTechnoSocialHerosBasedOnComments(a)


# findTechnoSocialHerosBasedOnComments("freemarker")