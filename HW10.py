import os
import json
import re


# ______________________________________________________________
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.


data_dir = os.listdir('.')
print(data_dir)  # проверка  есть ли необходимый файл в текущей директории


def read_file(file_name):
    with open(file_name, "r") as file:
        person = file.read()
        person = json.loads(person)
        return person


filename = "data.json"
persons = read_file(filename)
print(persons)

# ______________________________________________________________
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.


def sort_by_lastname_or_name(person):

    name = person["name"]
    name = name.split()

    if len(name) == 2:  # если есть фамилия, сортируйем по ней, если нет - сортируем по имени
        name_new = (name[1])
    else:
        name_new = (name[0])
    return name_new


sort_persons_by_lastname_or_name = sorted(persons, key=sort_by_lastname_or_name)
print(sort_persons_by_lastname_or_name)

# ______________________________________________________________
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.


def sort_by_deathdate(person):
    deathdate = person["years"]

    if "BC" in deathdate:
        pattern = r"\d+"
        result = int((re.findall(pattern, deathdate))[1]) * -1
        # print(result)
    else:
        pattern = r"\d+"
        result = int((re.findall(pattern, deathdate))[1])
        # print(result)

    return result


sort_persons_by_deathdate = sorted(persons, key=sort_by_deathdate)
print(sort_persons_by_deathdate)


# ______________________________________________________________
# 4. Написать функцию сортировки по количеству слов в поле "text"


def sort_by_count_words(person):
    words = person["text"]
    words = words.split()
    count_words = len(words)
    return count_words


sort_persons_by_count_words = sorted(persons, key=sort_by_count_words)
print(sort_persons_by_count_words)
