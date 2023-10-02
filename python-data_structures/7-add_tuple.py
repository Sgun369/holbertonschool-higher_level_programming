#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[:2]
    b = tuple_b[:2]
    sum_first_element = a[0] + b[0] if len(a) > 0 and len(b) > 0 else 0
    sum_second_element = a[1] + b[1] if len(a) > 1 and len(b) > 1 else 0

    reuslt_tuple = (sum_first_element, sum_second_element)
    return reuslt_tuple
