
# 1. Четные числа из списка
# Задача:
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Используя list comprehension, создай новый список, содержащий только четные числа.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = [x for x in numbers if x % 2 == 0]

print(new_list)

# 2. Квадраты чисел
# Задача:
# Дан список numbers = [1, 2, 3, 4, 5].
# Используя list comprehension, создай новый список, где каждое число возведено в квадрат.

numbers = [1, 2, 3, 4, 5]

x = [val ** 2 for val in numbers]

print(x)

# 3. Длины слов
# Задача:
# Дан список слов words = ["apple", "banana", "cherry", "date"].
# Создай список их длин.

words = ["apple", "banana", "cherry", "date"]

y = [len(word) for word in words]

print(y)

# 4. Фильтрация слов по длине
# Задача:
# Дан список слов words = ["hello", "hi", "world", "Python", "AI"].
# Создай список, содержащий только слова длиной более 3 символов.

words = ["hello", "hi", "world", "Python", "AI"]

list_n = [n for n in words if len(n) > 3]

print(list_n)

# 5. Преобразование строк в верхний регистр
# Задача:
# Дан список слов words = ["python", "java", "c++", "go"].
# Создай новый список, в котором все слова записаны в верхнем регистре.

words = ["python", "java", "c++", "go"]

new_l = [x.upper() for x in words]

print(new_l)


# 6. Первые буквы слов
# Задача:
# Дан список слов:
words = ["apple", "banana", "cherry", "date"]

# Создай новый список, содержащий первую букву каждого слова.
# Ожидаемый результат:
# ['a', 'b', 'c', 'd']

lower_case = [x[0] for x in words]

print(lower_case)


# 7. Длина слов больше 5
# Задача:
# Дан список слов:
words = ["hello", "world", "Python", "AI", "developer"]

# Создай новый список, содержащий только слова длиной больше 5 символов.
# Ожидаемый результат:
# ['Python', 'developer']

five_symbols = [x for x in words if len(x) > 5]
print(five_symbols)


# 8. Длина слов и сами слова
# Задача:
# Дан список слов:
words = ["apple", "banana", "cherry", "date"]
# Создай список кортежей, где каждый кортеж состоит из слова и его длины.
# Ожидаемый результат:
# [('apple', 5), ('banana', 6), ('cherry', 6), ('date', 4)]

new_list = [(x, len(x)) for x in words]
print(new_list)

# 9. Слова, содержащие букву "а"
# Задача:
# Дан список слов:
words = ["apple", "banana", "cherry", "date", "grape"]

# Создай новый список, содержащий только слова, в которых есть буква "а".
# Ожидаемый результат:
# ['apple', 'banana', 'date', 'grape']

new_list = [x for x in words if x.find('e') >= 5]
print(new_list)


