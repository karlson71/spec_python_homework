# # 1. Соединение двух списков с zip
# # Задача:
# # Даны два списка:
#
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# #
# # Создай список кортежей, где каждый кортеж содержит имя и возраст.
# # Ожидаемый результат:
# # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
#
# x = [i for i in zip(names, ages)]
#
# print(x)
#
# # 2. Словарь из двух списков
# # Задача:
# # Даны два списка
#
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "New York"]
#
# # Создай словарь, где ключи берутся из keys, а значения — из values.
# # Ожидаемый результат:
# # {'name': 'Alice', 'age': 25, 'city': 'New York'}
#
# result = dict(zip(keys, values))
# print(result)
#
#
# # 3. Пронумерованный список с enumerate
# # Задача:
# # Дан список:
# fruits = ["apple", "banana", "cherry"]
#
# # Создай новый список строк, где перед каждым элементом будет его номер (нумерация с 1).
# # Ожидаемый результат:
# # ['1. apple', '2. banana', '3. cherry']
#
# new_list = []
# for x, i in enumerate(fruits, 1):
#     new_list.append(f'{x}. {i}')
#
# print(new_list)
#
# # 4. Соединение трех списков
# # Задача:
# # Даны три списка:
# students = ["Alice", "Bob", "Charlie"]
# subjects = ["Math", "Physics", "Biology"]
# grades = [90, 85, 88]
#
# # Создай список строк вида:
# # "Alice изучает Math и получил 90 баллов"
# # Ожидаемый результат:
# # ['Alice изучает Math и получил 90 баллов',
# #  'Bob изучает Physics и получил 85 баллов',
# #  'Charlie изучает Biology и получил 88 баллов']
#
# new_list = []
# for x,y,z in zip(students, subjects, grades):
#     new_list.append(f'{x} изучает {y} и получил {z} баллов')
#
# print(new_list)

# 5. Поиск самого длинного слова с enumerate
# Задача:
# Дан список слов:

words = ["Python", "JavaScript", "C++", "Go"]

# Определи индекс самого длинного слова и само слово.
# Ожидаемый результат:

# (1, 'JavaScript')  # Индекс 1, слово 'JavaScript'
new_list = []
for i, x in zip(enumerate(words)):
    print(i)
    new_list.append(i)
#
# for n in new_list:
#     print(len(n[1]))

print(new_list)



