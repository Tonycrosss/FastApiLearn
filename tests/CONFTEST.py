import pytest
import httpx


class APIClient:

    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        print(f"POST request to {url}")
        return httpx.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        url = self.base_address + path
        return httpx.get(url=url, params=params)


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)
