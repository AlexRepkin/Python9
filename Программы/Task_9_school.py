#!usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    school = {"1A": 12, "1B": 21, "2A": 45,
              "2B": 23, "4A": 32, "5C": 14, "6F": 22}
    print("Good day, our current list of classes is:\n", school)
    # Задание a - изменить число студентов в требуемом классе.
    changed_class_key = input(
        "Please, give us the letter and the number of class, in which amount of students has changed -")
    changed_class_value = int(input("How many students are there now? - "))
    if school[changed_class_key] == changed_class_value:
        print("Excuse us, but amount of students hasn't changed.")
    else:
        school[changed_class_key] = changed_class_value
        print("Current list of classes:\n", school)
    # Задание b - добавить новый класс и информацию о нём.
    new_class_key = input(
        "Now give us the number and letter of a new class - ")
    new_class_value = int(input("Amount of students in it - "))
    school[new_class_key] = new_class_value
    # Задание c - удалить класс.
    goodbye = input("Which class doesn't exist anymore? - ")
    del school[goodbye]
    print("Final variant of list of classes:\n", school,
          "\nOverall amount of students - ", sum(school.values()))
