# curl -L -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/emojis

# curl -L -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/search/labels?repository_id=REPOSITORY_ID&q=Q
# curl -L -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/search/topics?q=Q
# curl -L -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/search/topics?q=ruby+is:featured


# hometask
# 1. Create config class in config module. 
# 1.1. class shall have get_property method
# 1.2. there shall be dev.json and prod.json files with API_BASE_URL property
# 2. Create GitHubAPIclient class with search repo method
# 3. Use GitHubAPIclient in fixture with module scope 
# 4. Create some tests using fixture from step #3

# curl -L -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/search/repositories?q=Q
# curl -L -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&order=desc