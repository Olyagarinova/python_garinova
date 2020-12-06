# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.

# my_list = ['alarm', 'car', 'art', 'army', 'ten']
#
# new_my_list = []
#
# for id, element in enumerate(my_list):
#     if id % 2:
#         new_my_list.append(element)
#     else:
#         new_my_list.append(element[::-1])
#
# print(new_my_list)
#
# #####################################################################
#
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
#
# my_list = ['alarm', 'car', 'art', 'army', 'mom']
#
# new_list = [value for value in my_list if value[0] == 'a']
# print(new_list)
#
# #####################################################################
#
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
#
# my_list = ['alarm', 'car', 'art', 'army', 'mom']
#
# new_list = [value for value in my_list if 'a' in value]
# print(new_list)
#
# #####################################################################
#
# 4. Дан список my_list в котором могум быть как строки так и целые числа.
# Создать новый список в который поместить только строки из my_list.
#
# my_list = ['alarm', 2, 'car', 'art', 4, 'army', 'mom']
#
# new_list = [value for value in my_list if value == str(value)]
# print(new_list)
#
# #####################################################################
#
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
#
# my_str = '333oo1o22aaa/'
#
# my_list = [symbol for symbol in my_str if my_str.count(symbol) == 1]
# print(my_list)


# #####################################################################
#
#
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
#
# str_1 = 'qxxxty'
# str_2 = 'qxwerty'
#
#
# str_1_set = set(str_1)
# str_2_set = set(str_2)
#
# my_list = list(str_1_set.intersection(str_2_set))
#
# print(my_list)
#
# #####################################################################
#
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
#
# str_1 = 'qwertty'
# str_2 = 'qqwerrty'
# my_list = []
#
# for symbol in str_1:
#     if str_1.count(symbol) == 1:
#         if str_2.count(symbol) == 1:
#                 my_list.append(symbol)
#
# print(my_list)
#
