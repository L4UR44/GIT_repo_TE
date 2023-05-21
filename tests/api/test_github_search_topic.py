import pytest
import requests


def test_search_topics_positive(fixture_git_hub_api_client):
    """
    positive parameters

    """

    topics = "ruby"

    topics_list = fixture_git_hub_api_client.search_topics(topics)
    assert topics in topics_list



def test_search_topics_negative(fixture_git_hub_api_client):
    """
    negative parameters
    """

    topics = "jkljkljklkljkl"

    topics_list = fixture_git_hub_api_client.search_topics(topics)
    assert topics not in topics_list
