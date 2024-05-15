import pytest
import sys, os
sys.path.append(os.getcwd())
from scr.utils import read_json, transaction_sum
from unittest.mock import Mock, patch

def test_read_json() -> None:
    mock_read = Mock(return_value=[])
    assert read_json('transactions.json') == mock_read()

def test_transaction_sum() -> None:
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'Valute': {'USD': {'Value': 90}, 'EUR': {'Value': 100}}}
        assert transaction_sum({'operationAmount': {'amount': 100, 'currency': {'code': 'USD'} }}) == 9000