#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    school = {
        "1А": 21,
        "1Б": 33,
        "2А": 10,
        "2Б": 23,
        "3А": 30,
        "3Б": 26,
    }

    for key, value in school.items():
        print("В классе: {0}: {1} учеников".format(key, value))

    print("\nВ одном из классов изменилось количество учащихся!")
    school['1А'] = 99
    for key, value in school.items():
        print("В классе: {0}: {1} учеников".format(key, value))

    print("\nВ школе появился новый класс!")
    school.setdefault("11Я", 10)
    for key, value in school.items():
        print("В классе: {0}: {1} учеников".format(key, value))

    print("\nВ школе был расформирован (удален) один из классов!")
    school.pop("1Б")
    for key, value in school.items():
        print("В классе: {0}: {1} учеников".format(key, value))

    amount = 0
    for value in school.values():
        amount += value
    print("\nВсего учеников: {0}".format(amount))
