import pytest
from src.user import User


@pytest.fixture(scope="module")  # (scope="session|package|module|class|function")
def user_fixture():
    # create a user -> precondition
    user_name = User.username # "automation_test_removein_30_days_non_existing_user"
    user = dict(name=user_name) 
    print(f"User {user_name} created")

    # execute test -> steps
    yield user

    # remove a user -> postcondition
    user = None   # user.remove()
    print(f"User {user_name} removed")


def pytest_html_report_title(report):
    report.title = "TE AQA 2023"
