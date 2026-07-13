import requests

from core.config import PROJECT_ENVIRONMENT
from core.api_client import fetch_sample_data

if __name__ == "__main__":
    print("Python Runtime Environment: Operational")
    print(f"Dependency Version Verification -> Requests: {requests.__version__}")
    print(f"Current Runtime Profile: {PROJECT_ENVIRONMENT.upper()}")
    print("-" * 50)
    fetch_sample_data()
