import pytest
from src.user import User
from src.applications.api.github_api_client import GitHubAPIClient
from src.config.config import Config


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


@pytest.fixture(scope='module')
def fixture_git_hub_api_client():
    api = GitHubAPIClient()
    api.login(Config.get_property("USERNAME"), Config.get_property("PASSWORD"))

    yield api

    api.logout()

