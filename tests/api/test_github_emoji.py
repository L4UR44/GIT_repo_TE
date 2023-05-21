import requests
import pytest

def test_emoji_1():
    r = requests.get(
        url = "https://api.github.com/emojis",
        # query params = {
        #     # 'q' = "Sergeii"
        # },
        headers = {
            "Accept" : "application/vnd.github+json",
            "X-GitHub-Api-Version" : "2022-11-28",
        },
        # body option 1
        # json = {},
        # body option 2
        #data = {}
    )

    r.raise_for_status()
    
    print("Response Status code", r.status_code)
    # print(requests.codes.ok)
    print("Response Cache Headers", r.headers['Cache-Control'])
    # print("Response Body", r.json())  # dict representation
    # print("Response Body", r.text) # string representation

    assert 'v8' in r.json()['zzz']


@pytest.fixture(scope='function')
def list_of_emojis(fixture_git_hub_api_client):
    yield fixture_git_hub_api_client.get_emojis()


def test_emoji_2(list_of_emojis):    
    assert len(list_of_emojis) != 0


def test_emoji_zzz_exist(list_of_emojis):
    assert 'zzz' in list_of_emojis


def test_emoji_laura_doesnt_exist(list_of_emojis):
    assert 'laura' not in list_of_emojis

