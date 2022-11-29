import pytest
from bson import ObjectId

from centralities import eigenVectorCentralityForTechnicalCollab, eigenVectorCentralityForSocialCollab

kafka_new_comers = {ObjectId('636529d6e9a99c9121bba37f'): 0.0, ObjectId('636529d6e9a99c9121bc92a5'): 0.0, ObjectId('636529d6e9a99c9121bc9830'): 0.0, ObjectId('636529d6e9a99c9121bc9117'): 0.11, ObjectId('636529d6e9a99c9121bb945b'): 0.35, ObjectId('636529d6e9a99c9121bc9f21'): 0.07, ObjectId('636529d5e9a99c9121bb2f16'): 0.44, ObjectId('636529d6e9a99c9121bbb43a'): 0.0, ObjectId('636529d6e9a99c9121bc9114'): 0.15, ObjectId('636529d6e9a99c9121bc92ae'): 0.35, ObjectId('636529d6e9a99c9121bc97fd'): 0.37, ObjectId('636529d6e9a99c9121bc9108'): 0.2, ObjectId('636529d6e9a99c9121bbedb5'): 0.27, ObjectId('636529d6e9a99c9121bc90f1'): 0.31, ObjectId('636529d6e9a99c9121bc9831'): 0.15, ObjectId('636529d6e9a99c9121bc911b'): 0.24, ObjectId('636529d5e9a99c9121bb43f5'): 0.15, ObjectId('636529d6e9a99c9121bbcfed'): 0.0, ObjectId('636529d5e9a99c9121bb2774'): 0.0, ObjectId('636529d6e9a99c9121bc9f1b'): 0.0, ObjectId('636529d6e9a99c9121bc9118'): 0.11, ObjectId('636529d6e9a99c9121bc5fc9'): 0.23, ObjectId('636529d6e9a99c9121bc9f1a'): 0.06, ObjectId('636529d6e9a99c9121bc9f20'): 0.1, ObjectId('636529d6e9a99c9121bc9f22'): 0.0, ObjectId('636529d6e9a99c9121bc982b'): 0.0, ObjectId('636529d6e9a99c9121bc982c'): 0.06, ObjectId('636529d6e9a99c9121bc92a1'): 0.06, ObjectId('636529d6e9a99c9121bc92a4'): 0.0, ObjectId('636529d6e9a99c9121bc9f1e'): 0.0}

@pytest.mark.parametrize("project_name, expected_output", [("kafka", kafka_new_comers)])
def test_eigenVectorCentralityForSocialCollab(project_name, expected_output):
    assert expected_output == eigenVectorCentralityForSocialCollab(project_name)
