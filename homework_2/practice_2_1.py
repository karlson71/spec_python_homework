tariff = input('Тип тарифа: ')
volume = int(input('Объём трафика: '))

dict_traf = {
    "S" : (500, 20),
    "M" : (750, 40),
    "L" : (1000, 80)
}

tariff_info = f"""
Тарифы:
S - {dict_traf.get("S")[0]} руб. / {dict_traf.get("S")[1]} Гб
M - {dict_traf.get("M")[0]} руб. / {dict_traf.get("M")[1]} Гб
L - {dict_traf.get("L")[0]} руб. / {dict_traf.get("L")[1]} Гб
"""

print(tariff_info)
print()

if tariff not in list(dict_traf.keys()):
    cost = "Такой тариф не существует"
elif volume < 0:
    cost = "Трафик не может быть отрицательны"
else:
    if volume - dict_traf.get(tariff)[1] >= 0:
        if (volume - dict_traf.get(tariff)[1]) % 5 > 0:
            cost = ((volume - dict_traf.get(tariff)[1]) // 5 + 1) * 150 + dict_traf.get(tariff)[0]
        else:
            cost =(volume - dict_traf.get(tariff)[1]) // 5 * 150 + dict_traf.get(tariff)[0]
    else:
        cost = dict_traf.get(tariff)[0]

cost_final = f"""
Тип тарифа: {tariff}
Объём трафика: {volume}
К оплате: {cost}
"""

print(cost_final)