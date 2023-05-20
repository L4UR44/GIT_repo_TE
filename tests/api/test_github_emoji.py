
import requests


def test_emoji():
    r = requests.get(
        url = "https://api.github.com/emojis",
        # params = {
        #     # 'q' = "Sergeii"
        # },
        headers = {
            "Accept" : "application/vnd.github+json",
            "X-GitHub-Api-Version" : "2022-11-28",
        }
    ,
    # data = {},
    # json = {},
    )

    # r.raise_for_status()
    
    print("Response Status code", r.status_code)
    # print(requests.codes.ok)
    print("Response Cache Headers", r.headers['Cache-Control'])
    print("Response Body", r.json()['zzz'])  # dict representation
    # print("Response Body", r.text) # string representation

    assert 'v8' in r.json()['zzz']
