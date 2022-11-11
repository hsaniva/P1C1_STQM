# projectList = ["freemarker","httpcomponents-core","httpcomponents-client","santuario-java",
#                "commons-bcel", "commons-vfs", "commons-validator", "commons-io",
#                "commons-collections", "xerces2-j"]

from networkx_utils import create_and_get_collaboration_graph, beautiful_graph
from newcomers_social_collaboration_graph import create_and_get_social_collaboration_dict
from newcomers_technical_collaboration_graph import createAndGetCollaborationDict
from centralities import eigenVectorCentralityForTechnicalCollab, eigenVectorCentralityForSocialCollab, degreeCentralityForTechnicalCollab, degreeCentralityForSocialCollab
beautiful_graph(create_and_get_collaboration_graph(createAndGetCollaborationDict("kafka")))
beautiful_graph(create_and_get_collaboration_graph(create_and_get_social_collaboration_dict("kafka")))

eigenVectorCentralityForTechnicalCollab("kafka")
