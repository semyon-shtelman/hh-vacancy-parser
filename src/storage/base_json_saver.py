from abc import ABC, abstractmethod
from typing import Dict, List


class BaseStorage(ABC):
    """
    Абстрактный класс работы с файлами
    """

    @abstractmethod
    def add_vacancy(self, data: Dict) -> None:
        pass

    @abstractmethod
    def get_vacancy(self, keyword: str | None = None) -> List[Dict]:
        pass

    @abstractmethod
    def delete_vacancy(self, data: Dict) -> None:
        pass
