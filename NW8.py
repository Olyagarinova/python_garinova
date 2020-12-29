import os
import random


# 1. Написать функцию, которая считывает из файла domains.txt
# названия некоторых интернет доменов и возвращает их в виде списка строк (названия возвращать без точки).

def domains_return(filename):
    """Returning a list of domains without a character '.' from a file"""
    with open(filename, "r") as file:
        result = []
        for line in file.readlines():
            line = line.replace(".", "")
            result.append(line.strip())
    return result


domains = domains_return("domains.txt")
print(domains)

# 2. Написать функцию, которая считывает данные из файла names.txt
# и возвращает список всех фамилий из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии)


def lastnames_return(filename):
    """Returning a list of last names from a file"""
    with open(filename, "r") as file:
        result = []
        for line in file.readlines():
            line = line.split()
            result.append(line[1])
    return result


lastname = lastnames_return('names.txt')
print(lastname)

# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2.
# Строку и число генерировать случайным образом. Буквы могут повторяться.
# Пример: miller.249@sgdyyur.com

def generate_email():
    some_number = random.randint(100, 1000)
    some_string = ''.join(chr(random.randint(ord('a'), ord('z'))) for j in range(random.randint(5, 7)))
    email = random.choice(lastname) + '.' + str(some_number) + '@' + some_string + '.' + random.choice(domains)
    return email.lower()

mail = generate_email()
print(mail)
