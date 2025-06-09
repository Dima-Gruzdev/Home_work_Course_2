from typing import Optional, Any


class Vacancy:
    """Класс  реализации вакансий"""
    __slots__ = ("name", "salary", "url", "description", "salary_from", "salary_to")

    def __init__(self, name: str, salary: int, url: str, description: str) -> None:
        """Метод инициализации параметров вакансий"""
        self.name = name
        self.url = url
        self.description = description
        self.__validate_salary(salary)

    def __str__(self):
        """Метод красивого возврата вакансии"""
        return f"""Название вакансии: {self.name},\nСсылка на вакансию: {self.url},
Зарплата: от {self.salary_from} до {self.salary_to},\nОписание вакансии: {self.description}\n"""

    def __validate_salary(self, salary: dict[str]) -> Optional[Any]:
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

    @classmethod
    def from_dict(cls, data: Optional) -> Optional:
        """Метод преобразование в объект класса"""
        return cls(
            name=data["name"],
            url=data["alternate_url"],
            salary=Vacancy.__validate_salary(data),
            description=data["description"])

    @classmethod
    def to_dict(cls, vacancy):
        """Метод преобразование в словарь"""
        return {"name": vacancy.name, "url": vacancy.url,
                "salary": {"from": vacancy.salary_from, "to": vacancy.salary_to}, "description": vacancy.description}
