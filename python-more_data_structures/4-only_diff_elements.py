#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    different = set()
    for element_1 in set_1:
        if element_1 not in set_2 and element_1 not in different:
            different.add(element_1)

    for element_2 in set_2:
        if element_2 not in set_1 and element_2 not in different:
            different.add(element_2)
    return different
