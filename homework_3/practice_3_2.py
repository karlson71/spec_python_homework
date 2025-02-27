growth = 0.03

sales = int(input('Текущий объём продаж: '))

while sales <= 0:
    print('Объем продаж должен быть положительным')
    sales = int(input('Текущий объём продаж: '))

target = int(input('Целевой объём продаж: '))

while target <= sales:
    print('Целевой объём должен превышать исходный')
    target = int(input('Целевой объём продаж: '))

count = 0
while sales < target:
    sales = sales * 0.03 + sales
    count +=1
    print(f'{count}: {int(sales)}')

print(f'Месяцев {count}, продажи {int(sales)}')