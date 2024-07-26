import os
import requests


def search_bing(query,bing_subscription_key, mkt="zh-CN"):
    headers = {"Ocp-Apim-Subscription-Key": bing_subscription_key}
    params = {"q": query, 'mkt': mkt, 'count': 3, 'responseFilter': 'webPages'}
    endpoint = "https://api.bing.microsoft.com/v7.0/search" # Bing Search API endpoint
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    return search_results
