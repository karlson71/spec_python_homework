# ДЗ 5.1 Решить следующие задачи:
# 1.	Сформировать список слов строки (без повторений, без учета регистра, за исключением знаков препинания),
#       длина которых превышает 7 символов;
# 2.	Вывести общий список слов двух заданных строк (без повторений, без учета регистра, за исключением знаков препинания).

import string
new_str = 'My test string - the best string! The best program language - Python! Python - the high level language.'

print(new_str)

processed_str = ''.join([x.replace('  ', '') for x in new_str.lower() if x not in string.punctuation])

final_list =  list(set([val for val in processed_str.split(' ') if len(val) > 7]))

print(final_list)

# ======================================================================================================================

first_str = 'Мы учимся в учебном центре "Специалист"'
second_str = 'В центре мы изучаем курс Python!'

two_str = (first_str + ' ' + second_str).lower().strip()
lst = list(set(''.join([f for f in two_str if f not in string.punctuation]).split(' ')))

print(lst)
