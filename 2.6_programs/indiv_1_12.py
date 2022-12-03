#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    people = []
    print("Программа запущена, введите help для просмотра команд!")
    while True:
        command = input(">>> ").lower()
        if command == "exit":
            break

        # Добавление новых людей
        elif command == "add":
            name = input("Введите фамилию и имя через пробел: ")
            pnumber = input("Введите номер телефона: ")
            birth = input("Введите дату рождения (01.01.2077): ")
            # Создание словаря
            person = {
                'name': name,
                'pnumber': pnumber,
                'birth': birth
            }
            # Добавление в список людей
            people.append(person)
            # Сортировка по алфавиту (на основе имени)
            if len(people) > 1:
                people.sort(key=lambda item: item.get('name', ''))

        # Вывод списка людей
        elif command == "list":
            # Оформление таблицы
            line = '---------------------'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
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
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        nmbr,
                        person.get('name', ''),
                        person.get('pnumber', ''),
                        person.get('birth', '')
                    )
                )
            print(line)

        # Выборка людей по введенному месяцу
        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            printed_month = parts[1]
            count = 0
            for person in people:
                birth = person.get('birth', 0)
                b_spl = birth.split('.')
                if printed_month == b_spl[1]:
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
            print("select <месяц> - запросить людей, чьи "
                  "дни рождения приходятся на указанный месяц;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда: {command}", file=sys.stderr)
