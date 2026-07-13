from core.api_client import fetch_sample_data
from core.config import API_BASE_URL


def test_fetch_sample_data_success(requests_mock):
    requests_mock.get(
        f"{API_BASE_URL}/posts/1",
        json={"id": 1, "title": "Mock Title", "body": "Mock body content"},
    )

    result = fetch_sample_data()

    assert result is not None
    assert result["title"] == "Mock Title"
    assert result["body"] == "Mock body content"


def test_fetch_sample_data_http_error(requests_mock):
    requests_mock.get(f"{API_BASE_URL}/posts/1", status_code=500)

    result = fetch_sample_data()

    assert result is None


def test_fetch_sample_data_connection_error(requests_mock):
    import requests

    requests_mock.get(
        f"{API_BASE_URL}/posts/1", exc=requests.exceptions.ConnectionError
    )

    result = fetch_sample_data()

    assert result is None
