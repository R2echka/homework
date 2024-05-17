# import os
# import sys
# sys.path.append(os.getcwd())
from unittest.mock import patch, Mock

import pytest

from scr.utils import read_json, transaction_sum


@pytest.fixture
def first_operation() -> dict:
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


@patch('builtins.open', create=True)
def test_read_json(mock_open: Mock) -> None:
    "Тест чтения json-файла"
    with patch('json.load') as mock_load:
        mock_file = mock_open.return_value.__enter__.return_value
        mock_json = mock_load.return_value.json.return_value
        mock_json.return_value = ['test data']
        assert mock_json() == ['test data']


def test_transaction_sum() -> None:
    "тест вывода суммы транзакции"
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"Valute": {"USD": {"Value": 90}, "EUR": {"Value": 100}}}
        assert transaction_sum({"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}) == 9000
