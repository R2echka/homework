import pytest

# import sys, os
# sys.path.append(os.getcwd())
from scr.widget import date_correction, mask


@pytest.mark.parametrize(
    "info, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ],
)
def test_mask(info: str, expected: str) -> None:
    """Тест объединения масок в одну функцию"""
    assert mask(info) == expected


def test_date_correction() -> None:
    """Тест изменения формата даты"""
    assert date_correction("2018-07-11T02:26:18.671407") == "11.07.2018"
