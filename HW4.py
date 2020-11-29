########################## 1
my_list = [1, 103, 88, 303]
for symbol in my_list:
    if symbol > 100:
        print(symbol)

########################## 2

my_list = [1, 103, 88, 303]
my_result = []
for element in my_list:
    if element > 100:
        my_result.append(element)
print(my_result)

########################## 3

my_list = [1, 2, 3]
if len(my_list) < 2:
    my_list.append(0)
    print(my_list)
elif len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
    print(my_list)




########################## 4

value = input("Введи число:")
try:
    value = float(value)
    print(value ** - 1)

except ValueError:
    print("This value isn`t float")


########################## 5

my_indexes = [0, 1, 2, 3]
my_list = [33, 34, 35, 36]

for index in my_indexes:
    print(my_list[index])


########################## 6

my_list_1 = [9, 6, 3]
my_list_2 = [6, 4, 2]
my_indexes = [0, 1, 2]

for index in my_indexes:
    print((my_list_1[index], my_list_2[index]))


########################## 7

my_string = '0123456789'
list = []
# my_string = int(my_string)
for symb_1 in my_string:
    for symb_2 in my_string:
        list.append(int(symb_1 + symb_2))
print(list)