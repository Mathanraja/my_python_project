import requests

from core.config import API_BASE_URL


def fetch_sample_data():
    target_endpoint = f"{API_BASE_URL}/posts/1"

    print(f"Connecting to API endpoint: {target_endpoint}...")

    try:
        response = requests.get(target_endpoint, timeout=10)
        response.raise_for_status()

        data = response.json()
        print("\n[Success] Live Connection Verified via Environment Variables!")
        print(f"Title of Post #1: {data.get('title')}")
        print(f"Body snippet: {data.get('body')[:60]}...")
        return data

    except requests.exceptions.RequestException as error:
        print("\n[Error] Failed to connect to the external API.")
        print(f"Details: {error}")
        return None
