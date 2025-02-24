

start_price = int(input("Начальная цена товара: "))
current_price = int(input("Текущая цена товара: "))
is_final = int(input("Финальная ли цена? 1(да) или 0(нет): "))
bonus = int(input("Число бонусов: "))
card_type = input("Тип бонусной карты: ").lower()

cards_dict = {
    'голубая' : 0.05,
    'серебрянная' : 0.07,
    'золотая' : 0.1
}

max_bonus = round(current_price * 0.3)

if is_final:
    bonus_to_use = 0
    final_sum = current_price
    remains_bonus = bonus
    earned_bonus = 0

elif current_price - max_bonus > start_price * 0.5:
    bonus_to_use = min(bonus, max_bonus)
    remains_bonus = bonus - bonus_to_use
    final_sum = current_price - bonus_to_use
    earned_bonus = 0

elif current_price < start_price * 0.5:
    bonus_to_use = 0
    remains_bonus = bonus
    final_sum = current_price
    earned_bonus = 0

elif current_price - max_bonus < start_price * 0.5:
    bonus_to_use = round(current_price - start_price * 0.5)
    remains_bonus =round(bonus - bonus_to_use)
    final_sum = round(current_price - bonus_to_use)
    earned_bonus = 0

if start_price == current_price:
    if bonus < max_bonus:
        bonus_to_use = current_price * bonus
        remains_bonus = bonus - bonus_to_use
        final_sum = current_price - bonus_to_use
        earned_bonus = round(final_sum * cards_dict.get(card_type, 0))
    elif bonus >= max_bonus:
        bonus_to_use = max_bonus
        remains_bonus = bonus - bonus_to_use
        final_sum = current_price - bonus_to_use
        earned_bonus = round(final_sum * cards_dict.get(card_type, 0))

print(f'К оплате: {final_sum}')
print(f'Списано бонусов: {bonus_to_use}')
print(f'Осталось бонусов: {remains_bonus}')
print(f'Будет начислено: {earned_bonus}')