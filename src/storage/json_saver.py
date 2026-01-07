import json
from pathlib import Path
from typing import Dict, List

from src.storage.base_json_saver import BaseStorage


class JSONSaver(BaseStorage):
    """
    Класс для сохранения вакансий в JSON
    """

    def __init__(self, filename: str = "vacancies.json"):
        base_dir = Path(__file__).resolve().parents[2]
        data_dir = base_dir / "data"
        data_dir.mkdir(exist_ok=True)

        self.__file_path = data_dir / filename
        self.__data = self.__load()

    def __load(self) -> List[Dict]:
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def __save(self) -> None:
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__data, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, data: Dict) -> None:
        if data not in self.__data:
            self.__data.append(data)
            self.__save()

    def get_vacancy(self, keyword: str | None = None) -> List[Dict]:
        if not keyword:
            return self.__data
        return [v for v in self.__data if keyword.lower() in v["description"].lower()]

    def delete_vacancy(self, data: Dict) -> None:
        self.__data.remove(data)
        self.__save()
