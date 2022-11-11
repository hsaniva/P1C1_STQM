import pytest
from bson import ObjectId

from NewComers import findNewComers

kafka_new_comers = {ObjectId('5b0fc419065f3902028dfa90'), ObjectId('5b0fc40a065f3902028de8d7'), ObjectId('58bfcda102ca40f8bf147ecd'), ObjectId('5b0fc415065f3902118df449'), ObjectId('5b0fc417065f3902078df847'), ObjectId('5b0fc415065f3902108df8d1'), ObjectId('5b0fc401065f3902088de3ab'), ObjectId('5b0fc419065f3902078df9d3'), ObjectId('5b0fc418065f3902058df8e4'), ObjectId('5b0fc418065f39020a8df66c'), ObjectId('5b0fc415065f3902058df6e4'), ObjectId('5b0fc415065f3902118df512'), ObjectId('5b0fc418065f3902028dfa01'), ObjectId('5b0fc400065f3902068de37d'), ObjectId('59e49df4f2a4565fe9e2bd8e'), ObjectId('5b0fc418065f39020d8df862'), ObjectId('5b0fc419065f3902048dfaad'), ObjectId('5b0fc415065f39020f8df6af'), ObjectId('5b0fc406065f39020d8de729'), ObjectId('5b0fc418065f3902108dfc07'), ObjectId('5b0fc419065f3902088dfbc1'), ObjectId('5b0fc419065f39020e8df895'), ObjectId('5b0fc401065f3902118de438'), ObjectId('5b0fc419065f3902118df849'), ObjectId('58c8dda402ca40f8bfbae3f8'), ObjectId('5b0fc40f065f3902088def23'), ObjectId('5b0fc419065f3902028dfa41'), ObjectId('5b0fc418065f3902128df9d4'), ObjectId('58c8d8ae02ca40f8bfbaaa9a'), ObjectId('5b0fc418065f3902068df8a3'), ObjectId('5b0fc418065f3902118df6fe'), ObjectId('5b0fc417065f3902058df80e'), ObjectId('5b0fc415065f3902118df47a'), ObjectId('5b0fc400065f3902058de36a')}
pig_new_comers = {ObjectId('5b2903cfa096a05e07d24bc0'), ObjectId('5b2903d0a096a05e0dd24b7c')}

@pytest.mark.parametrize("project_name, expected_output", [("kafka", kafka_new_comers), ("pig", pig_new_comers)])
def test_new_comers(project_name, expected_output):
    assert expected_output == findNewComers(project_name)