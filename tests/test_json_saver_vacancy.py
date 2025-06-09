import pytest

from src.json_saver_vacancy import JSONSaver


def test_get_vacancies_nonexistent_file(tmp_path):
    """Проверка чтения несуществующего файла"""
    saver = JSONSaver(path=tmp_path / "nonexistent.json")
    with pytest.raises(FileNotFoundError):
        saver.get_vacancies()
