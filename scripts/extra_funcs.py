from typing import Any, Union

'''
This module defines some extra functions requires for the main file 'Youtube'
'''


def superappend(lists: list[list[Any]], items: list[Any]) -> None:
    """Appends given items to the given lists in order.\n
    Raises IndexError if items is longer than the length of given lists"""
    for i, item in enumerate(items):
        try:
            lists[i].append(item)
        except IndexError:
            print("list: {lists[i]} out of range for index: {i}")


def _add_time(input_list: list[list[str]], desc: bool = False) -> str:
    hour_list, min_list, sec_list = [], [], []

    # get hours, minutes, seconds as three lists
    for i, time_str in enumerate(input_list):
        if len(time_str) == 3:
            hour, min, sec = time_str
            superappend([hour_list, min_list, sec_list],
                        [int(hour), int(min), int(sec)])
        elif len(time_str) == 2:
            min, sec = time_str
            superappend([min_list, sec_list], [int(min), int(sec)])
        elif len(time_str) == 1:
            sec_list.append(int(time_str))
        else:
            pass

    # take the sum of lists seperately
    hour_sum, min_sum, sec_sum = sum(hour_list), sum(min_list), sum(sec_list)

    # some changes to make it readable and accurate
    min_sum += sec_sum // 60
    hour_sum += min_sum // 60
    sec_sum = sec_sum % 60
    min_sum = min_sum % 60

    if len(str(sec_sum)) < 2:
        sec_sum = str(f'0{sec_sum}')

    if len(str(min_sum)) < 2:
        min_sum = str(f'0{min_sum}')

    if desc:
        return f'{hour_sum} hours, {min_sum} minutes and {sec_sum} seconds'

    return f'{hour_sum}:{min_sum}:{sec_sum}'
