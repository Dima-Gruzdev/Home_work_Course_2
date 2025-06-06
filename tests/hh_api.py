from unittest.mock import patch, MagicMock

from src.hh_api import HHAPI


def test_initialization(hh_api):
    """Проверка инициализации параметров"""
    assert getattr(hh_api, '_HHAPI__url') == "https://api.hh.ru/vacancies"
    assert getattr(hh_api, '_HHAPI__params') == {"text": "", "per_page": 50, "page": 0}


@patch('requests.get')
def test_connect_success(mock_get, hh_api):
    """Проверка успешного подключения к API"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": []}
    mock_get.return_value = mock_response

    result = hh_api._connect()
    assert result == {"items": []}
    mock_get.assert_called_with(hh_api._HHAPI__url, params=hh_api._HHAPI__params)


@patch('requests.get')
def test_connect_failure(mock_get, hh_api):
    """Проверка обработки ошибки подключения"""
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    result = hh_api._connect()
    assert result is None


def test_filter_vacancy():
    """Проверка фильтрации вакансий"""
    raw_vacancies = [
        {
            "name": "Python Developer",
            "alternate_url": "https://hh.ru/vacancy/123 ",
            "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
            "snippet": {"requirement": "Опыт работы от 3 лет"}
        }
    ]

    filtered = HHAPI.filter_vacancy(raw_vacancies)
    assert filtered == [{
        "name": "Python Developer",
        "url": "https://hh.ru/vacancy/123 ",
        "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
        "description": "Опыт работы от 3 лет"
    }]
