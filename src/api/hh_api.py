from typing import Dict, List

import requests

from src.api.base_api import Parser


class HeadHunterAPI(Parser):
    """
    Класс для работы с API hh.ru
    """

    __BASE_URL = "https://api.hh.ru/vacancies"
    __MAX_PAGES = 20

    def __init__(self) -> None:
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__vacancies: List[Dict] = []

    def __connect(self, params: dict) -> requests.Response:
        """
        Приватный метод подключения к API hh.ru
        """
        response = requests.get(self.__BASE_URL, headers=self.__headers, params=params)
        if response.status_code != 200:
            raise ConnectionError("Ошибка подключения к hh.ru")
        return response

    def get_vacancies(self, keyword: str) -> List[Dict]:
        """
        Получает вакансии с hh.ru по ключевому слову
        """
        params = {"text": keyword, "page": 0, "per_page": 100}

        while params["page"] < self.__MAX_PAGES:
            response = self.__connect(params)
            self.__vacancies.extend(response.json()["items"])
            params["page"] += 1

        return self.__vacancies
