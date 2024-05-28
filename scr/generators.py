from typing import Generator


def filter_by_currency(list_: list, currency: str, file_type: str) -> Generator[dict, None, None]:
    """Принимает список словарей и возвращает генератор словарей, сортирующий их по валюте"""
    for i in list_:
        if file_type == 'json':
            if i["operationAmount"]["currency"]["code"] == currency.upper():
                yield i
        else:
            if i['currency_code'] == currency.upper():
                yield i


def transaction_descriptions(list_: list) -> Generator[str, None, None]:
    """Принимает список словарей и возвращает генератор их описаний"""
    for i in list_:
        yield i["description"]


def card_number_generator(first: int, last: int) -> Generator[str, None, None]:
    """Генерирует номера карт"""
    for i in range(first, last + 1):
        card_num = f"{i:0>16}"
        yield card_num[:4] + " " + card_num[4:8] + " " + card_num[8:12] + " " + card_num[12:]
