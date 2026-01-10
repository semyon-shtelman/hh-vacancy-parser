from src.vacancy import Vacancy

def test_salary_validation_none():
    vacancy = Vacancy("Dev", "url", None, None, "rub", "desc")
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0


def test_salary_validation_int():
    vacancy = Vacancy("Dev", "url", 100000, 150000, "rub" , "desc")
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 150000


def test_vacancy_comparison():
    v1 = Vacancy("A", "url", 100000, None, "rub","")
    v2 = Vacancy("B", "url", 200000, None, "rub","")
    assert v2 > v1
    assert v1 < v2


def test_to_dict():
    vacancy = Vacancy("Dev", "url", 100, 200, "rub","desc")
    data = vacancy.to_dict()

    assert data["title"] == "Dev"
    assert data["salary_from"] == 100
