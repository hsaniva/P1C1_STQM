import pytest
from bson import ObjectId

from superHeros import findSuperHeros

kafka_social_heroes = {ObjectId('636529d5e9a99c9121bb2d2b'), ObjectId('636529d6e9a99c9121bc9271'), ObjectId('636529d5e9a99c9121bb283a'), ObjectId('636529d5e9a99c9121bb2f16'), ObjectId('636529d5e9a99c9121bb2e79'), ObjectId('636529d5e9a99c9121bb2d7d'), ObjectId('636529d6e9a99c9121bc90e2'), ObjectId('636529d6e9a99c9121bc97fd'), ObjectId('636529d6e9a99c9121bc97fc'), ObjectId('636529d6e9a99c9121bc90e8'), ObjectId('636529d6e9a99c9121bc8ba4'), ObjectId('636529d5e9a99c9121bb2f25'), ObjectId('636529d6e9a99c9121bc910d'), ObjectId('636529d6e9a99c9121bb93d3'), ObjectId('636529d6e9a99c9121bc980d'), ObjectId('636529d6e9a99c9121bc8ba2')}
pig_social_heroes = {ObjectId('636529d6e9a99c9121bc9efa'), ObjectId('636529d6e9a99c9121bc9b91'), ObjectId('636529d5e9a99c9121bb281e')}

@pytest.mark.parametrize("project_name, expected_output", [("kafka", kafka_social_heroes), ("pig", pig_social_heroes)])
def test_super_heroes(project_name, expected_output):
    assert expected_output == findSuperHeros(project_name)
