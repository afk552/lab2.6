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
    dictionary_new = {}
    for key,value in dictionary.items():
        dictionary_new[value] = key
    print("Обратный словарь: ", dictionary_new)
