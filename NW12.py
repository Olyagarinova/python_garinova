# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).


import requests

# def quote_creator(number):
#     url = "http://api.forismatic.com/api/1.0/"
#     params = {"method": "getQuote",
#           "format": "json",
#           "key": 1,
#           "lang": "ru"}
#     r = requests.get(url, params=params)
#     quote = r.json()
#     quote_text = quote["quoteText"]
#     quote_author = quote["quoteAuthor"]
#     if len(quote_author) > 0:
#         return quote_author

url = "http://api.forismatic.com/api/1.0/"
params = {"method": "getQuote",
          "format": "json",
          "key": 1,
          "lang": "ru"}
r = requests.get(url, params=params)
quote = r.json()
quote_text = quote["quoteText"]
quote_author = quote["quoteAuthor"]
if len(quote_author) > 0:
    print(quote_author)

# def quote_creator_count(count: int):
#     return [quote_creator() for _ in range(count)]


# res = quote_creator_count(3)
# print(res)

# 2. Дан файл authors.txt
#
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая список строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.
#
# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
#
# Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "date": "01/01/1919"}]
#
# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.