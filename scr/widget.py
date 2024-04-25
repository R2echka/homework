from datetime import datetime as dt

# import sys, os
# sys.path.append(os.getcwd())
# без этих двух строчек код не работает, по крайней мере в VSCode
from scr.masks import bill_mask, card_mask


def mask(info: str) -> str:
    """Соединение функций масок в одну"""
    if "Счет" in info:
        return f"Счет {bill_mask(info.split()[-1])}"
    else:
        card_info = info.split()
        return str(" ".join(card_info[:-1]) + " " + card_mask(card_info[-1]))


def date_correction(date: str) -> str:
    """Форматирует дату"""
    formated_date = dt.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return formated_date.strftime("%d.%m.%Y")
