def sort_by_state(list_: list, state_status: str = "executed") -> list:
    '''Получает список и возвращает список словарей, удовлетворяющих заданному значению "state"'''
    sorted_list = []
    for dict_ in list_:
        if dict_["state"] == state_status.upper():
            sorted_list.append(dict_)
    return sorted_list


def date_sort(list_: list, time: str = "increasing") -> list:
    """Сортирует полученный список по дате"""
    sorted_list = []
    if time == "increasing":
        sorted_list = sorted(list_, key=lambda dict_: dict_["date"], reverse=True)
    elif time == "decreasing":
        sorted_list = sorted(list_, key=lambda dict_: dict_["date"])
    return sorted_list
