from src.api.hh_api import HeadHunterAPI
from src.storage.json_saver import JSONSaver
from src.utils import get_top_vacancies
from src.vacancy import Vacancy


def user_interaction() -> None:
    api = HeadHunterAPI()
    saver = JSONSaver()

    keyword = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий: "))

    raw_data = api.get_vacancies(keyword)
    vacancies = Vacancy.cast_to_object_list(raw_data)

    top_vacancies = get_top_vacancies(vacancies, top_n)

    for vacancy in top_vacancies:
        saver.add_vacancy(vacancy.to_dict())
        print(
            f"{vacancy.title}\n"
            f"Зарплата: {vacancy.salary_from}-{vacancy.salary_to} {vacancy.currency}\n"
            f"{vacancy.url}\n"
            f"{vacancy.description}\n"
        )


if __name__ == "__main__":
    user_interaction()
