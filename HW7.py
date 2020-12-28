# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.

import random
#
# numbers_list = [(random.randrange(1, 100)) for _ in range(20)]
# print(numbers_list)

# ______________________________
#
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.

# triangle = {key:(random.randrange(-10, 10)) for key in ['A', 'B', 'C']}
# print(triangle)

# ______________________________
#
# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает *I'm the string*
#
# def my_print(value):
#     print('***' + value + '***')
#
#
# my_str = "I`m the string"
# my_print(my_str)
#
# ______________________________
#
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.

# а)

# persons = [{"name": "John", "age": 15}, {"name": "Justin", "age": 16}, {"name": "Jack", "age": 45}]
#
# ages = [person["age"] for person in persons]
# min_age = min(ages)
#
#
# for value in persons:
#     if value["age"] == min_age:
#         print(value["name"])
# _________________________________

# б)

# persons = [{"name": "John", "age": 15}, {"name": "Justin", "age": 16}, {"name": "Jacckk", "age": 45}]
#
# name_len = [len(person["name"]) for person in persons]
# max_len = max(name_len)
#
# for value in persons:
#     if len(value["name"]) == max_len:
#         print(value["name"])
# ___________________________________
# в)

# persons = [{"name": "John", "age": 15}, {"name": "Justin", "age": 66}, {"name": "Jack", "age": 45}]
#
# ages = []
# for value in persons:
#     ages.append(value["age"])
#
# print(ages)
#
# average_ages = sum(ages) / (len(ages))
# print(average_ages)

# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]}
#
# а)

# my_dict_1 = {1 : 'a', 2 : 'b', 3 : 'z'}
# my_dict_2 = {1 : 'a', 22 : 'bb', 3 : 'z'}
#
# my_list = []
#
# my_dict_1_set = set(my_dict_1)
# my_dict_2_set = set(my_dict_2)
#
# my_list = list(my_dict_1_set.intersection(my_dict_2_set))
# print(my_list)

# ___________________________

# б)

# my_dict_1 = {1 : 'a', 2 : 'b', 3 : 'z'}
# my_dict_2 = {1 : 'a', 22 : 'bb', 3 : 'z'}
#
# my_list = []
#
# my_dict_1_set = set(my_dict_1)
# my_dict_2_set = set(my_dict_2)
#
# my_list = list(my_dict_1_set.difference(my_dict_2_set))
#
# print(my_list)
# ____________________________

# в)

# my_dict_1 = {1 : 'a', 2 : 'b', 3 : 'z'}
# my_dict_2 = {1 : 'a', 22 : 'bb', 3 : 'z'}
#
# result = dict((key, my_dict_1[key]) for key in my_dict_1 if key not in my_dict_2)
#
# print(result)
# ______________________________

# г)

# my_dict_1 = {1 : 'a', 2 : 'b', 33 : 'z'}
# my_dict_2 = {1 : 'a', 22 : 'bb', 3 : 'z'}
#
# res = {}
#
# for item in my_dict_1.items():
#     if item[0] not in my_dict_2:
#         res[item[0]] = item[1]
#     else:
#         res[item[0]] = [item[1], my_dict_2[item[0]]]
#
# print(res)