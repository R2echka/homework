import sys, os
sys.path.append(os.getcwd())
from scr.widget import date_correction


def sort_by_state(list_: list, state_status:str = 'executed') -> str:
    sorted_list = []
    for dict_ in list_:
        if dict['state'] == state_status.upper():
            sorted_list.append(dict_)
    return sorted_list
