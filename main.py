from src.Abstract_class import HHAPI
from src.json_saver_vacancy import JSONSaver


def user_interface():
    """Метод  поиска пользователем через консоль"""
    hh_api = HHAPI()
    storage = JSONSaver()
    all_vacancies = []

    query = input("Введите поисковый запрос для hh.ru: ")
    vacancies_data = hh_api.load_vacancies(query)
    all_vacancies.append(vacancies_data)

    storage.save_vacancies(vacancies_data)
    print(f"Сохранено {len(vacancies_data)} вакансий")

    try:
        count_vacancy = int(input("Введите количество вакансий для топа по зарплате: "))
        top_vacancies = sorted(all_vacancies, reverse=True)[:count_vacancy]
        for vac in top_vacancies:
            print(vac)
            print(type(all_vacancies))
    except ValueError:
        print("Некорректный ввод")

    keyword = input("Введите ключевое слово для поиска в описании: ").lower()
    filtered = [x for x in all_vacancies if keyword in x.description.lower()]
    for v in filtered:
        print(v)


if __name__ == "__main__":
    user_interface()
