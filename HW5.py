# 1. Дано целое число (int). Определить сколько нулей в этом числе.

# value = int(1010101010)
# value = str(value)
# my_symbol = '0'
#
# count = value.count(my_symbol)
# print(count)


# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.

# value = int(45600000000)
# revers_value = str(value)[::-1]
# revers_value_1 = int(revers_value)
# revers_value_1 = str(revers_value_1)
# result = len(revers_value) - len(revers_value_1)
# print(result)


# 3. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,2,3,4,5], my_list_2 = [10, 15, 20, 25] -> my_result [2, 4, 15, 25]

# my_list_1 = [1,2,3,4,5]
# my_list_2 = [10, 15, 20, 25]
# result = []
# for item1 in my_list_1:
#     if not item1 % 2:
#         result.append(item1)
# for item2 in my_list_2:
#     if item2 % 2:
#         result.append(item2)
# print(result)


# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
#
# my_list = [1, 2, 3, 4]
# a, b, c, d = my_list
# new_list = [b, c, d, a]
# print(new_list)

#
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

# my_list = [1,2,3,4]
# value = my_list.pop(0)
# my_list.append(value)
# print(my_list)


# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133.

# my_str = "43 больше чем 34 но меньше чем 56"
# result = []
# new_str = my_str.split()
# for symbol in new_str:
#     if symbol.isnumeric():
#         symbol = int(symbol)
#         result.append(symbol)
# print(result)
#
# res = sum(result)
# print(res)

# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', 'e_']
#
# my_str = "abcde"
# res = []
#
# if not len(my_str) % 2:
#     for x in range(0, len(my_str), 2):
#         res.append(my_str[x:x+2])
#
# else:
#     my_str = list(my_str)
#     my_str.append('_')
#     my_str = ''.join(my_str)
#     for x in range(0, len(my_str), 2):
#             res.append(my_str[x:x+2])
# print(res)


# #
# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"

# my_str = "My_long str"
# l_limit = "o"
# r_limit = "t"
#
# index_l = my_str.find(l_limit)
# index_r = my_str.find(r_limit)
# print (my_str[index_l+1:index_r])

# 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
#
# my_str = "My long string"
# l_limit = "o"
# r_limit = "g"
#
# index_l = my_str.find(l_limit)
# index_r = my_str.rfind(r_limit)
# new_str = my_str[index_l+1:index_r]
# print(new_str)

# 10. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

# my_list = [2, 4, 1, 5, 3, 9, 0, 7]
#
# count = 0
# new_list = []
#
# for value in range(1, len(my_list) - 1):
#     if my_list[value - 1] < my_list[value] > my_list[value + 1]:
#         # print(value)
#         new_list.append(value)
#
# # print(new_list)
# print(len(new_list))
