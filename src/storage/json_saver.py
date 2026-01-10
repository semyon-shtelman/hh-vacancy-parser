import json
from pathlib import Path
from typing import Dict, List

from src.storage.base_json_saver import BaseStorage


class JSONSaver(BaseStorage):
    """
    Класс для сохранения и управления вакансиями в JSON-файле.

    Отвечает за:
    - загрузку вакансий из файла;
    - добавление новых вакансий без дублирования;
    - получение вакансий по ключевому слову;
    - удаление вакансий из хранилища.
    """

    def __init__(self, filename: str = "vacancies.json"):
        """
        Инициализирует объект для работы с JSON-файлом.

        При инициализации:
        - определяется корневая директория проекта;
        - создаётся папка `data`, если она отсутствует;
        - загружаются ранее сохранённые вакансии из файла.

        :param filename: Имя JSON-файла для хранения вакансий
        """
        base_dir = Path(__file__).resolve().parents[2]
        data_dir = base_dir / "data"
        data_dir.mkdir(exist_ok=True)

        self.__file_path = data_dir / filename
        self.__data = self.__load()

    def __load(self) -> List[Dict]:
        """
        Загружает данные о вакансиях из JSON-файла.

        :return: Список словарей с данными вакансий;
                 пустой список, если файл не найден
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def __save(self) -> None:
        """
        Сохраняет текущие данные о вакансиях в JSON-файл.

        Перезаписывает файл актуальным состоянием хранилища.
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__data, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, data: Dict) -> None:
        """
        Добавляет вакансию в хранилище.

        Вакансия добавляется только в том случае,
        если она отсутствует в текущем списке вакансий.

        :param data: Словарь с данными вакансии
        """
        if data not in self.__data:
            self.__data.append(data)
            self.__save()

    def get_vacancy(self, keyword: str | None = None) -> List[Dict]:
        """
        Получает вакансии из хранилища.

        Если ключевое слово не указано, возвращаются все вакансии.
        Если указано — возвращаются только вакансии,
        в описании которых содержится данное слово.

        :param keyword: Ключевое слово для фильтрации вакансий
        :return: список словарей с данными вакансий
        """
        if not keyword:
            return self.__data
        return [v for v in self.__data if keyword.lower() in v["description"].lower()]

    def delete_vacancy(self, data: Dict) -> None:
        """
        Удаляет вакансию из хранилища.

        После удаления изменения сохраняются в JSON-файл.

        :param data: Словарь с данными вакансии для удаления
        """
        self.__data.remove(data)
        self.__save()
