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

print(date_sort([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], "decreasing"))