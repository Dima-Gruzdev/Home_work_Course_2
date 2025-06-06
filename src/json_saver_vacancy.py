import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class JsonSaveAbstract(ABC):
    """Абстрактный класс для работы с хранилищем вакансий.
       Определяет интерфейс для добавления, получения и удаления данных."""

    def get_vacancies(self):
        """Получает вакансии из хранилища по указанным критериям."""
        pass

    @abstractmethod
    def save_vacancies(self, vacancies):
        """Сохранение вакансий"""
        pass

    @abstractmethod
    def delete_vacancies(self):
        """Удаление вакансий"""
        pass


class JSONSaver(JsonSaveAbstract):
    """Класс реализации методов добавления, удаления , сохранение, сортировки"""

    def __init__(self, path="data/vacancies.json"):
        self.__path = path

    def get_vacancies(self):
        """Метод запроса ваканский"""
        with open(self.__path, "r", encoding="utf-8") as f:
            data = json.load(f)
        vacancies = []
        for vac in data:
            vacancies.append(Vacancy(**vac))
        return vacancies

    def save_vacancies(self, vacancy):
        """Метод сохранения вакансии в файл"""
        all_vacancies = self.get_vacancies()
        all_vacancies_dict = [Vacancy.to_dict(vacancy) for vacancy in all_vacancies]
        vacancies_names = [vacancy.name for vacancy in all_vacancies]
        if vacancy["name"] not in vacancies_names:
            all_vacancies_dict.append(vacancy)
        with open(self.__path, "w", encoding="utf-8") as file:
            json.dump(all_vacancies_dict, file, ensure_ascii=False, indent=4)

    def delete_vacancies(self):
        """Метод удаления из файла"""
        open(self.__path, "w").close()
