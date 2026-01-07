import requests
from src.api.hh_api import HeadHunterAPI


class MockResponse:
    def __init__(self, json_data, status_code):
        self._json_data = json_data
        self.status_code = status_code

    def json(self):
        return self._json_data


def mock_get(*args, **kwargs):
    return MockResponse(
        {
            "items": [
                {"name": "Python Dev", "alternate_url": "url"}
            ]
        },
        200
    )


def test_load_vacancies(monkeypatch):
    monkeypatch.setattr(requests, "get", mock_get)

    hh = HeadHunterAPI()
    result = hh.get_vacancies("Python")

    assert isinstance(result, list)
    assert len(result) > 0
