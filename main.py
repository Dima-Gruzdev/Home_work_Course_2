from src.hh_api import HHAPI
from src.json_saver_vacancy import JSONSaver
from src.utils import sort_vacancies, get_top_vacancies, print_vacancies, filter_vacancies


def user_interface():
    """Метод поиска пользователем через консоль"""
    hh_api = HHAPI()
    storage = JSONSaver()

    query = input("Введите поисковый запрос для hh.ru: ")
    vacancies_data = hh_api.load_vacancies(query)

    for vacancy in vacancies_data:
        storage.save_vacancies(vacancy)
    print(f"Сохранено {len(vacancies_data)} вакансий")
    all_vacancies = storage.get_vacancies()

    try:
        count_vacancy = int(input("Введите количество вакансий для топа по зарплате: "))
        sorted_vacancies = sort_vacancies(all_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, count_vacancy)
        print_vacancies(top_vacancies)
    except ValueError:
        print("Некорректный ввод")

    keyword = input("Введите ключевое слово для поиска в описании: ").lower()
    filtered = filter_vacancies(all_vacancies, keyword)
    print_vacancies(filtered)


if __name__ == "__main__":
    user_interface()
