#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    dictionary = {
        1: "test",
        2: "tost",
        3: "ttst",
        4: "tset",
        5: "tttt"
    }
    print("Введенный словарь: ", dictionary)

    dict_items = dictionary.items()
    dictionary_new = {key: value for value, key in dict_items}
    print("Обратный словарь: ", dictionary_new)
