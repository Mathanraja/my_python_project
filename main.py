import os
import requests
from dotenv import load_dotenv

load_dotenv()


def fetch_sample_data():
    base_url = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
    project_env = os.getenv("PROJECT_ENVIRONMENT", "unknown")

    target_endpoint = f"{base_url}/posts/1"

    print(f"Current Runtime Profile: {project_env.upper()}")
    print(f"Connecting to API endpoint: {target_endpoint}...")

    try:
        response = requests.get(target_endpoint, timeout=10)
        response.raise_for_status()

        data = response.json()
        print("\n[Success] Live Connection Verified via Environment Variables!")
        print(f"Title of Post #1: {data.get('title')}")
        print(f"Body snippet: {data.get('body')[:60]}...")

    except requests.exceptions.RequestException as error:
        print("\n[Error] Failed to connect to the external API.")
        print(f"Details: {error}")


if __name__ == "__main__":
    print("Python Runtime Environment: Operational")
    print(f"Dependency Version Verification -> Requests: {requests.__version__}")
    print("-" * 50)
    fetch_sample_data()
