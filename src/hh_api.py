from abc import ABC, abstractmethod
import requests


class AbstractAPI(ABC):
    """Абстрактный класс для соединение и запроса вакансий"""
    @abstractmethod
    def _connect(self):
        pass

    @abstractmethod
    def load_vacancies(self, text):
        pass


class HHAPI(AbstractAPI):
    """ Класс для соединение с АПИ """
    def __init__(self):
        """Метод инициализации параметров API"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"text": "", "per_page": 50, "page": 0}

    def _connect(self):
        """ Метод соединения с API"""
        response = requests.get(self.__url, params=self.__params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Ошибка соединения")

    def load_vacancies(self, text: str) -> list:
        """Метод запроса вакансий"""
        self.__params["text"] = text
        all_vacancies = []
        while self.__params["page"] < 5:
            vacancies = self._connect()["items"]
            all_vacancies.extend(self.filter_vacancy(vacancies))
            self.__params["page"] += 1
        return all_vacancies

    @staticmethod
    def filter_vacancy(vacancies: list) -> list:
        """Метод фильтрация возращаемого запроса"""
        all_vacancies = []
        for vacancy in vacancies:
            all_vacancies.append({"name": vacancy["name"], "url": vacancy["alternate_url"],
                                  "salary": vacancy["salary"], "description": vacancy["snippet"]["requirement"]})
        return all_vacancies
