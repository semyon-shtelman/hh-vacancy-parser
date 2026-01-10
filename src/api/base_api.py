from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Абстрактный класс для работы с API платформ вакансий
    """

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list[dict]:
        """Получает вакансии по ключевому слову"""
        pass
