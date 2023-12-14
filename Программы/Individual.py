#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import datetime


if __name__ == "__main__":
    print("Good day!, please, enter your command: ('help' will list all of them)")
    people = []
    while True:
        command = input(">>> ").lower()
        if command == "exit":
            break
        elif command == "add":
            name = input("Name - ")
            surname = input("Surname - ")
            telephone = input("Telephone number - ")
            happy_birthday = input("Date of birth (Day.Month.Year) - ")
            human = {"name": name, "surname": surname,
                     "telephone": telephone, "birthday": happy_birthday}
            people.append(human)
            # Сортировка идёт по фамилиям. Если фамилии одинаковые, то рассматриваются имена
            people.sort(key=lambda person: (person.get(
                "surname", ""), person.get("name", "")))
        elif command == "list":
            line = "├-{}-⫟-{}⫟-{}-⫟-{}-⫟-{}-┤".format(
                "-" * 5, "-" * 25, "-" * 25, "-" * 25, "-" * 18)
            print(line)
            print("| {:^5} | {:^24} | {:^25} | {:^25} | {:^18} |".format(
                "№", "Name", "Surname", "Telephone", "Birthday"))
            print(line)
            for number, human in enumerate(people, 1):
                print("| {:^5} | {:<24} | {:<25} | {:<25} | {:<18} |".format(number, human.get(
                    "name", ""), human.get("surname", ""), human.get("telephone", ""), human.get("birthday", "")))
            print(line)
        elif command.startswith("select "):
            which_month = command.split(" ", maxsplit=1)
            user_month = int(which_month[1])
            count = 0
            for human in people:
                # Разбиение строки на день, месяц и год. Нужен только месяц, так что
                # возможно ещё использовать срез int(human.get("birth")[3:5]).
                human_month = human.get("birthday").split(".")
                if user_month == int(human_month[1]):
                    count += 1
                    print("{:>4}: {} {}".format(
                        count, human.get("name"), human.get("surname")))
            if count == 0:
                print("There is no such a human.")
        elif command == "help":
            print("List of commands:")
            print("add - adding the human;")
            print("list - list of known people;")
            print("select 'month' - list of people, born in needed month;")
            print("help - list of commands;")
            print("exit - exit this program.")
        else:
            print(f"Unknown command! - {command}", file=sys.stderr)
