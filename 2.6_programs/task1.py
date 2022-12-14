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
        print(f"В классе: {key}: {value} учеников")

    print("\nВ одном из классов изменилось количество учащихся!")
    school['1А'] = 99
    for key, value in school.items():
        print(f"В классе: {key}: {value} учеников")

    print("\nВ школе появился новый класс!")
    school.setdefault("11Я", 10)
    for key, value in school.items():
        print(f"В классе: {key}: {value} учеников")

    print("\nВ школе был расформирован (удален) один из классов!")
    school.pop("1Б")
    for key, value in school.items():
        print(f"В классе: {key}: {value} учеников")

    amount = 0
    for value in school.values():
        amount += value
    print(f"\nВсего учеников: {amount}")
