# import time
#
# # 1. Определить количество слов в строке
#
# st = 'My test string'
#
# print(len(st.strip().split(' ')))
#
# st_num = '2, -1, 99.7, -10, 20, 8, 0'
#
# numbers = [float(x) for x in st_num.strip().split(', ')]
# numbers.sort()
#
# print(numbers)
#
# numbers = list(map(float, st_num.split(', ')))
# numbers.sort()
# print(numbers)
#
#
# numbers = numbers * 10
#
# start = time.time()
#
# positive = [n for n in numbers if n > 0]
# negative = [n for n in numbers if n < 0]
#
# print(time.time() - start)
#
# start = time.time()
# positive = list(filter(lambda n: n > 0, numbers))
# negative = list(filter(lambda n: n < 0, numbers))
#
# print(time.time() - start)
# # print(list(positive))
# # print(list(negative))
#

print(', '.join(map(str, range(0, 10))))


st = ('ключ, книга, Киоск, ' * 10)[:-2]

st = st.lower()

start = st.lower()

print(st)

