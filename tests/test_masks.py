import pytest

# import sys, os
# sys.path.append(os.getcwd())
from scr.masks import bill_mask, card_mask


@pytest.mark.parametrize(
    "card_num, expected", [("7000792289606361", "7000 79** **** 6361"), ("1596837868705199", "1596 83** **** 5199")]
)
def test_card_mask(card_num: str, expected: str) -> None:
    """Тест применения маски на номер карты"""
    assert card_mask(card_num) == expected


@pytest.mark.parametrize(
    "bill_num, expected", [("64686473678894779589", "**9589"), ("35383033474447895560", "**5560")]
)
def test_bill_mask(bill_num: str, expected: str) -> None:
    """Тест применения маски на номер счёта"""
    assert bill_mask(bill_num) == expected
