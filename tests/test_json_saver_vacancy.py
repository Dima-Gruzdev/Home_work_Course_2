import json

import pytest

from src.json_saver_vacancy import JSONSaver
from src.vacancy import Vacancy


def test_save_and_get_vacancies(json_saver, test_vacancies):
    """Проверка сохранения и чтения вакансий"""
    json_saver.save_vacancies(test_vacancies)
    loaded_vacancies = json_saver.get_vacancies()

    assert len(loaded_vacancies) == 2
    assert isinstance(loaded_vacancies[0], Vacancy)


def test_get_vacancies_nonexistent_file(tmp_path):
    """Проверка чтения несуществующего файла"""
    saver = JSONSaver(path=tmp_path / "nonexistent.json")
    with pytest.raises(FileNotFoundError):
        saver.get_vacancies()


def test_save_empty_vacancies(json_saver):
    """Проверка сохранения пустого списка"""
    json_saver.save_vacancies([])
    with open(json_saver._JSONSaver__path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data == []


def test_save_invalid_data(json_saver):
    """Проверка обработки некорректных данных"""
    invalid_data = [{"invalid_field": "value"}]
    json_saver.save_vacancies(invalid_data)

    with pytest.raises(TypeError):
        json_saver.get_vacancies()
