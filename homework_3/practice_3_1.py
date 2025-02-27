import math

sales = int(input('Текущий объём продаж: '))

while sales <= 0:
    print('Объем продаж должен быть положительным')
    sales = int(input('Текущий объём продаж: '))
plan = int(input('Планируемый прирост: '))
while plan <= 0:
    print('Прирост должен быть положительным')
    plan = int(input('Планируемый прирост: '))

for i in range(1, 13):
    sales = sales * plan / 100 + sales
    print(f'{i}. {math.floor(sales)}')

print(f'Продажи увеличатся до {math.floor(sales)}')