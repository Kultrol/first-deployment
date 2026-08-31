from sqlalchemy import inspect

from deploy_first.app.database import engine


def test_deployment_test_table_exists() -> None:
    inspector = inspect(engine)

    table_names = inspector.get_table_names()

    assert "deployment_tests" in table_names
