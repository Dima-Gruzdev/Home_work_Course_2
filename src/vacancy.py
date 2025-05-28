class Vacancy:
    __slots__ = ("name", "salary", "url", "description", "salary_from", "salary_to")

    def __init__(self, name, salary, url, description):
        """Метод инициализации параметров вакансий"""
        self.name = name
        self.url = url
        self.description = description
        self.__validate_salary(salary)

    def __validate_salary(self, salary):
        """ Метод валидации валюты для  корректного возврата"""
        if not salary:
            self.salary_from = 0
            self.salary_to = 0
        else:
            self.salary_from = salary.get("from") if salary.get("from") else 0
            self.salary_to = salary.get("to") if salary.get("to") else 0

    def __lt__(self, other):
        """Метод сравнения зп"""
        return self.salary_from < other.salary_from

    def __str__(self):
        """Метод красивого возврата вакансии"""
        return f"""Название вакансии: {self.name}, Ссылка на вакансию: {self.url}, 
        Зарплата: от  {self.salary_from} до {self.salary_to}, Описание вакансии: {self.description}, """
