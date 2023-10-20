#!/usr/bin/python3
"""
Load,add,save module
"""

import sys
if __name__ == '__main__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =\
        __import__('6-load_from_json_file').load_from_json_file

    json_filename = "add_item.json"

    try:
        item_list = load_from_json_file(json_filename)
    except FileNotFoundError:
        item_list = []

    item_list.extend(sys.argv[1:])
    save_to_json_file(item_list, json_filename)
