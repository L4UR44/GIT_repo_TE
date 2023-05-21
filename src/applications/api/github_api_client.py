import requests

class GitHubAPIClient:

    def __init__(self) -> None:
        pass

    def login(self):
        print("DO LOGIN")

    def logout (self):
        print("DO LOGOUT")

    def get_emojis(self):
        """
            Get  list of available emojis in github system
        """
        r = requests.get(
            url = "https://api.github.com/emojis",
            # params = {
            #     # 'q' = "Sergeii"
            # },
            headers = {
            "Accept" : "application/vnd.github+json",
            "X-GitHub-Api-Version" : "2022-11-28",
            },
            # data = {},
            # json = {},
        )
        print("Get Emojis Response Status code", r.status_code)
        # print("Response Cache Headers", r.headers['Cache-Control'])
        # print("Response Body", r.json()['zzz'])
        
        r.raise_for_status()
        body = r.json()
        list_of_emojis = body.keys()

        return list_of_emojis
       