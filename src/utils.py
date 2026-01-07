from typing import List

from src.vacancy import Vacancy


def get_top_vacancies(vacancies: List[Vacancy], n: int) -> List[Vacancy]:
    """Возвращает топ N вакансий по зарплате"""
    return sorted(vacancies, reverse=True)[:n]
