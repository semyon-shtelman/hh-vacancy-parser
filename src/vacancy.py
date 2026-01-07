from typing import Dict, List, Optional


class Vacancy:
    """
    Класс для представления вакансии
    """

    __slots__ = ("title", "url", "salary_from", "salary_to", "currency", "description")

    def __init__(
        self,
        title: str,
        url: str,
        salary_from: Optional[int],
        salary_to: Optional[int],
        currency: Optional[str],
        description: str,
    ):
        self.title = title
        self.url = url
        self.salary_from = self.__validate_salary(salary_from)
        self.salary_to = self.__validate_salary(salary_to)
        self.currency = currency if self.salary_from or self.salary_to else ""
        self.description = description

    @staticmethod
    def __validate_salary(value: Optional[int]) -> int:
        return value if isinstance(value, int) else 0

    def __lt__(self, other: "Vacancy") -> bool:
        return self.salary_from < other.salary_from

    def __gt__(self, other: "Vacancy") -> bool:
        return self.salary_from > other.salary_from

    @classmethod
    def cast_to_object_list(cls, data: List[Dict]) -> List["Vacancy"]:
        vacancies = []
        for item in data:
            salary = item.get("salary") or {}
            vacancies.append(
                cls(
                    title=item["name"],
                    url=item["alternate_url"],
                    salary_from=salary.get("from"),
                    salary_to=salary.get("to"),
                    currency=salary.get("currency"),
                    description=item.get("snippet", {}).get("requirement", ""),
                )
            )
        return vacancies

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "currency": self.currency,
            "description": self.description,
        }
