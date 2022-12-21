#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import datetime as dt

if __name__ == '__main__':
    people = []
    print("Программа запущена, введите help для просмотра команд!")
    # Словарь месяцев по их названию для select
    month_by_text = {
        "январь": "01",
        "февраль": "02",
        "март": "03",
        "апрель": "04",
        "май": "05",
        "июнь": "06",
        "июль": "07",
        "август": "08",
        "сентябрь": "09",
        "октябрь": "10",
        "ноябрь": "11",
        "декабрь": "12",
    }

    while True:
        command = input(">>> ").lower()
        # Команда выхода из программы
        if command == "exit":
            break

        # Добавление новых людей
        elif command == "add":
            name = input("Введите фамилию и имя через пробел: ")
            pnumber = input("Введите номер телефона: ")
            birth = input("Введите дату рождения (01.01.2077): ").split('.')
            birth_dt = dt.datetime(int(birth[2]),
                                   int(birth[1]),
                                   int(birth[0])
                                   )
            # Создание словаря
            person = {
                'name': name,
                'pnumber': pnumber,
                'birth': birth_dt
            }
            # Добавление в список людей
            people.append(person)
            # Сортировка по алфавиту (на основе имени)
            if len(people) > 1:
                people.sort(key=lambda item: item.get('name', ''))

        # Вывод списка людей
        elif command == "list":
            # Оформление таблицы
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 14,
                '-' * 19
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^14} | {:^19} |'.format(
                    "№п/п",
                    "Фамилия Имя",
                    "Номер телефона",
                    "Дата рождения"
                )
            )
            print(line)
            # Вывод информации по каждому человеку
            for nmbr, person in enumerate(people, 1):
                print(
                    '| {:>4} | {:<30} | {:<14} | {:>19} |'.format(
                        nmbr,
                        person.get('name', ''),
                        person.get('pnumber', ''),
                        person.get('birth', '').strftime("%d.%m.%Y")
                    )
                )
            print(line)

        # Выборка людей по введенному месяцу
        elif command.startswith('select '):
            # Делим команду
            parts = command.split(' ', maxsplit=1)
            # Переменная коррекции месяца при вводе одной цифры
            printed_month_correct = ""
            printed_month = parts[1]
            # Если ввели месяц как текст, ищем значение в словаре
            if printed_month.isalpha():
                printed_month.lower()
                for key, value in month_by_text.items():
                    if key == printed_month:
                        printed_month = value
            if len(printed_month) == 1:
                printed_month_correct += "0"
                printed_month_correct += printed_month
            else:
                printed_month_correct = printed_month

            count = 0
            for person in people:
                birth = person.get('birth')
                if printed_month_correct == birth.strftime("%m"):
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, person.get('name', ''))
                    )
            if count == 0:
                print("Людей, чьи дни рождения приходятся на указанный месяц нет.")

        # Вывод справки по командам
        elif command == 'help':
            print("Список доступных команд:")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("select <месяц> ('Январь' / '01') - запросить людей, чьи "
                  "дни рождения приходятся на указанный месяц;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда: {command}", file=sys.stderr)
