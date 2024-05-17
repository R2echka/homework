# import os
# import sys
# sys.path.append(os.getcwd())
from unittest.mock import Mock, patch

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


def test_read_json(first_operation: list) -> None:
    "Тест чтения json-файла"
    mock = Mock(return_value=first_operation)
    assert read_json("idk.json") == []
    assert read_json("data/operations.json")[1] == mock()


def test_transaction_sum() -> None:
    "тест вывода суммы транзакции"
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"Valute": {"USD": {"Value": 90}, "EUR": {"Value": 100}}}
        assert transaction_sum({"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}) == 9000
