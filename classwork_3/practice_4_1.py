price = int(input('Первоначальная цена: '))

msg = 'Выберите категорию:\n'

groups = ['одежда', 'обувь', 'сумки']
bonus_levels = [20, 30, 10]

groups_bonus = list(zip(groups, bonus_levels))

for n, gb in enumerate(groups_bonus, start=1):
    msg += f'{n}\t{gb[0]} - {gb[1]}%\n'


g_num = int(input(msg))

bonus = int(price - price * (groups_bonus[g_num-1][1] / 100))

print(f'{bonus} руб.')