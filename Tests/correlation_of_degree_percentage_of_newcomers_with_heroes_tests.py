import pytest

from newcomers_relations_with_heroes import correlation_of_degree_of_newcomer_becoming_heroes

kafka_corr_coeff = 0.9482931244142663

@pytest.mark.parametrize("project_name, expected_output", [("kafka", kafka_corr_coeff)])
def correlation_coeff_test(project_name, expected_output):
    assert expected_output == correlation_of_degree_of_newcomer_becoming_heroes(project_name)
