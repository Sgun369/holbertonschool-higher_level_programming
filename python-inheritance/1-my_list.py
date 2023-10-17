#!/usr/bin/python3
"""
a module for a class Mylist
"""


class MyList(list):
    """"
    class Mylist that inherit from list
    """

    def print_sorted(self):
        """
        prints the list in ascending sorted order
        """
        sorted_list = sorted(self)
        print(sorted_list)
