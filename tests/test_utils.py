from src.vacancy import Vacancy
from src.utils import get_top_vacancies


def test_get_top_vacancies():
    v1 = Vacancy("A", "url", 100, None, "rub", "")
    v2 = Vacancy("B", "url", 300, None, "rub", "")
    v3 = Vacancy("C", "url", 200, None, "rub", "")

    result = get_top_vacancies([v1, v2, v3], 2)

    assert len(result) == 2
    assert result[0].title == "B"
