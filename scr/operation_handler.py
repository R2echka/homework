import re
from collections import defaultdict
from typing import DefaultDict


def find_in_data(data: list, to_find: str) -> list:
    """Принимает список словарей и строку, которую необходимо найти в описании
    и возвращает список словарей, в описании которых есть эта строка"""
    sorted_data = []
    for operation in data:
        if re.findall(to_find.lower(), operation["description"].lower()) != []:
            sorted_data.append(operation)
    return sorted_data


def count_by_categories(data: list, categories: list) -> dict:
    """Принимает списки операций и категорий и возвращает словарь
    с названием категории и количеством к ней относящихся операций"""
    counted_dict: DefaultDict[str, int] = defaultdict(int)
    for category in categories:
        for operation in data:
            if operation["description"] == category:
                counted_dict[category] += 1
    return dict(counted_dict)
