from src.config.config import Config
import requests


class GitHubAPIClient:

    def __init__(self) -> None:
        pass

    def login(self, username, password):
        print(f"DO LOGIN for {username} and {password}")

    def logout (self):
        print("DO LOGOUT")

    def get_emojis(self):
        """
            Get  list of available emojis in github system
        """
        r = requests.get(
            url = f"https:://{Config.get_property('TARGET')}/emojis",
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
    
    def search_topics(self, topics):
        """
        Search topic by a rtopics param
        Return list of topics
        """
        # sendgin the request
        r = requests.get(
            url=f"{Config.get_property('API_BASE_URL')}/search/topics",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            # add query parameter
            params={
                'q': topics,
            },
        )
        print("Get Search Topics Response Status Code:", r.status_code)

        # throw an error if response is not 2xx and 3xx
        # optional
        r.raise_for_status()
        
        # get body
        body = r.json()

        body_topics = [x['name'] for x in body['items']]
        
        return body_topics

       