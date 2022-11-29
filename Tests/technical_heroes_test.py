import pytest
from bson import ObjectId

from technical_heroes import findHeroDevsBasedOnFiles, findHeroDevsBasedOnCommits, findHeroDevsBasedOnLines, \
    findOverallTechnicalDevelopers

kafka_tech_heroes_based_on_files = {ObjectId('636529d5e9a99c9121bb2d7d'), ObjectId('636529d6e9a99c9121bc90e8'), ObjectId('636529d6e9a99c9121bc8ba2'), ObjectId('636529d6e9a99c9121bc97fd'), ObjectId('636529d6e9a99c9121bc8ba4'), ObjectId('636529d6e9a99c9121bc9f27'), ObjectId('636529d6e9a99c9121bc8baa'), ObjectId('636529d6e9a99c9121bc911b'), ObjectId('636529d6e9a99c9121bb93d3'), ObjectId('636529d6e9a99c9121bc910d'), ObjectId('636529d5e9a99c9121bb2fe2'), ObjectId('636529d5e9a99c9121bb2d2b'), ObjectId('636529d5e9a99c9121bb283a'), ObjectId('636529d6e9a99c9121bbd9d2'), ObjectId('636529d6e9a99c9121bc9271'), ObjectId('636529d6e9a99c9121bc9274'), ObjectId('636529d5e9a99c9121bb2e79'), ObjectId('636529d6e9a99c9121bc97fc'), ObjectId('636529d6e9a99c9121bc90e2'), ObjectId('636529d5e9a99c9121bb2fe1'), ObjectId('636529d5e9a99c9121bb2f25'), ObjectId('636529d5e9a99c9121bb2f16'), ObjectId('636529d6e9a99c9121bc980d'), ObjectId('636529d6e9a99c9121bc8bb7'), ObjectId('636529d6e9a99c9121bc92ae')}
pig_tech_heroes_based_on_files = {ObjectId('636529d6e9a99c9121bc96b0'), ObjectId('636529d6e9a99c9121bc9efa'), ObjectId('636529d6e9a99c9121bc96ae'), ObjectId('636529d5e9a99c9121bb281e'), ObjectId('636529d6e9a99c9121bc4b16'), ObjectId('636529d6e9a99c9121bc96b1'), ObjectId('636529d6e9a99c9121bc9b91')}


@pytest.mark.parametrize("project_name, expected_output", [("kafka", kafka_tech_heroes_based_on_files), ("pig", pig_tech_heroes_based_on_files)])
def test_find_tech_heroes_based_on_files(project_name, expected_output):
    assert expected_output == findHeroDevsBasedOnFiles(project_name)


kafka_tech_heroes_based_on_commits = {ObjectId('636529d6e9a99c9121bc92ae'), ObjectId('636529d5e9a99c9121bb2f16'), ObjectId('636529d6e9a99c9121bb93d3'), ObjectId('636529d6e9a99c9121bbd600'), ObjectId('636529d6e9a99c9121bc90e6'), ObjectId('636529d5e9a99c9121bb271c'), ObjectId('636529d5e9a99c9121bb2d7d'), ObjectId('636529d6e9a99c9121bc8baa'), ObjectId('636529d6e9a99c9121bc8bb7'), ObjectId('636529d5e9a99c9121bb6530'), ObjectId('636529d6e9a99c9121bc910d'), ObjectId('636529d6e9a99c9121bbedb5'), ObjectId('636529d6e9a99c9121bb9408'), ObjectId('636529d6e9a99c9121bc9274'), ObjectId('636529d5e9a99c9121bb2e79'), ObjectId('636529d6e9a99c9121bc8ba4'), ObjectId('636529d6e9a99c9121bc90e8'), ObjectId('636529d6e9a99c9121bc9f0a'), ObjectId('636529d6e9a99c9121bc9f27'), ObjectId('636529d6e9a99c9121bc926f'), ObjectId('636529d5e9a99c9121bb2f0b'), ObjectId('636529d5e9a99c9121bb2fe2'), ObjectId('636529d6e9a99c9121bc97fe'), ObjectId('636529d5e9a99c9121bb283a'), ObjectId('636529d6e9a99c9121bc97fc'), ObjectId('636529d6e9a99c9121bc90f7'), ObjectId('636529d6e9a99c9121bc97fd'), ObjectId('636529d5e9a99c9121bb2727'), ObjectId('636529d6e9a99c9121bc8ba9'), ObjectId('636529d5e9a99c9121bb2d2b'), ObjectId('636529d6e9a99c9121bb9579'), ObjectId('636529d6e9a99c9121bc9273'), ObjectId('636529d6e9a99c9121bbd9d2'), ObjectId('636529d6e9a99c9121bc8ba2'), ObjectId('636529d6e9a99c9121bc980d'), ObjectId('636529d6e9a99c9121bc9108'), ObjectId('636529d6e9a99c9121bc911b'), ObjectId('636529d6e9a99c9121bc9271'), ObjectId('636529d5e9a99c9121bb2fe1'), ObjectId('636529d6e9a99c9121bc8ba8'), ObjectId('636529d6e9a99c9121bc90f1'), ObjectId('636529d6e9a99c9121bc9277'), ObjectId('636529d5e9a99c9121bb2f25'), ObjectId('636529d6e9a99c9121bb945b'), ObjectId('636529d6e9a99c9121bc980c'), ObjectId('636529d6e9a99c9121bc90e2')}
pig_tech_heroes_based_on_commits = {ObjectId('636529d6e9a99c9121bc96b1'), ObjectId('636529d6e9a99c9121bc96b0'), ObjectId('636529d6e9a99c9121bca2c0'), ObjectId('636529d6e9a99c9121bc9b92'), ObjectId('636529d6e9a99c9121bc96af'), ObjectId('636529d6e9a99c9121bc9efa'), ObjectId('636529d6e9a99c9121bc9b91'), ObjectId('636529d5e9a99c9121bb281e'), ObjectId('636529d6e9a99c9121bc96ae')}

@pytest.mark.parametrize("project_name, expected_output", [("kafka", kafka_tech_heroes_based_on_commits), ("pig", pig_tech_heroes_based_on_commits)])
def test_find_tech_heroes_based_on_commits(project_name, expected_output):
    assert expected_output == findHeroDevsBasedOnCommits(project_name)


kafka_tech_heroes_based_on_lines = {ObjectId('636529d6e9a99c9121bc9271'), ObjectId('636529d6e9a99c9121bbd600'), ObjectId('636529d5e9a99c9121bb2d7d'), ObjectId('636529d6e9a99c9121bc8ba4'), ObjectId('636529d6e9a99c9121bc8ba2'), ObjectId('636529d6e9a99c9121bc980d'), ObjectId('636529d6e9a99c9121bbd9d2'), ObjectId('636529d5e9a99c9121bb2f25'), ObjectId('636529d6e9a99c9121bc90e8'), ObjectId('636529d6e9a99c9121bc9f27'), ObjectId('636529d5e9a99c9121bb2e79'), ObjectId('636529d6e9a99c9121bb93d9'), ObjectId('636529d5e9a99c9121bb2f16'), ObjectId('636529d6e9a99c9121bc97fd'), ObjectId('636529d6e9a99c9121bb93d3'), ObjectId('636529d5e9a99c9121bb283a'), ObjectId('636529d6e9a99c9121bc97fc'), ObjectId('636529d6e9a99c9121bc910d'), ObjectId('636529d6e9a99c9121bc90e2'), ObjectId('636529d5e9a99c9121bb2d2b')}
pig_tech_heroes_based_on_lines = {ObjectId('636529d5e9a99c9121bb281e'), ObjectId('636529d6e9a99c9121bc9efa'), ObjectId('636529d6e9a99c9121bc96ae'), ObjectId('636529d6e9a99c9121bc9b91'), ObjectId('636529d6e9a99c9121bc96b2'), ObjectId('636529d6e9a99c9121bc4b16')}

@pytest.mark.parametrize("project_name, expected_output", [("kafka", kafka_tech_heroes_based_on_lines), ("pig", pig_tech_heroes_based_on_lines)])
def test_find_tech_heroes_based_on_lines(project_name, expected_output):
    assert expected_output == findHeroDevsBasedOnLines(project_name)

kafka_overall_tech_heroes = {ObjectId('636529d6e9a99c9121bb93d3'), ObjectId('636529d6e9a99c9121bc8ba4'), ObjectId('636529d5e9a99c9121bb2d2b'), ObjectId('636529d5e9a99c9121bb2f25'), ObjectId('636529d5e9a99c9121bb2f16'), ObjectId('636529d5e9a99c9121bb283a'), ObjectId('636529d6e9a99c9121bc90e2'), ObjectId('636529d5e9a99c9121bb2e79'), ObjectId('636529d6e9a99c9121bc9271'), ObjectId('636529d6e9a99c9121bc8ba2'), ObjectId('636529d6e9a99c9121bc97fc'), ObjectId('636529d6e9a99c9121bc9f27'), ObjectId('636529d6e9a99c9121bc90e8'), ObjectId('636529d6e9a99c9121bc97fd'), ObjectId('636529d6e9a99c9121bc980d'), ObjectId('636529d5e9a99c9121bb2d7d'), ObjectId('636529d6e9a99c9121bbd9d2'), ObjectId('636529d6e9a99c9121bc910d')}
pig_overall_tech_heroes = {ObjectId('636529d6e9a99c9121bc9b91'), ObjectId('636529d6e9a99c9121bc9efa'), ObjectId('636529d5e9a99c9121bb281e'), ObjectId('636529d6e9a99c9121bc96ae')}


@pytest.mark.parametrize("project_name, expected_output", [("kafka", kafka_overall_tech_heroes), ("pig", pig_overall_tech_heroes)])
def test_find_overall_tech_heroes(project_name, expected_output):
    assert expected_output == findOverallTechnicalDevelopers(project_name)