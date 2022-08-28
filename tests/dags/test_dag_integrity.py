import pytest

# from airflow.models.dagbag import DagBag


# @pytest.fixture()
# def dagbag():
#     return DagBag(include_examples=False)

# def test_dagbag(dagbag):
#     assert not dagbag.import_errors
    
#     # If you want all your dags to have tags:
#     for dag in dagbag.dags.items():
#         assert dag.tags