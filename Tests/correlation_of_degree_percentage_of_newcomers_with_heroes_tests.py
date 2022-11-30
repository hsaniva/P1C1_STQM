import pytest

from newcomers_relations_with_heroes import correlation_of_degree_of_newcomer_becoming_heroes

kafka_corr_coeff = round(0.9482931244142663, 3)

@pytest.mark.parametrize("project_name, expected_output", [("kafka", kafka_corr_coeff)])
def test_degree_centrality_for_technical_colab(project_name, expected_output):
    corr_coeff = correlation_of_degree_of_newcomer_becoming_heroes(project_name)
    assert expected_output == round((corr_coeff[0][1] + corr_coeff[1][0])/2, 3)
