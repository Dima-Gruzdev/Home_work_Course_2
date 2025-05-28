import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class JsonSaveAbstract(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def save_vacancies(self, vacancies):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass


class JSONSaver(JsonSaveAbstract):

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

    def save_vacancies(self, vacancies):
        """Метод сохранения вакансии в файл"""
        with open(self.__path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def delete_vacancies(self):
        """Метод удаления из файла"""
        open(self.__path, "w").close()
