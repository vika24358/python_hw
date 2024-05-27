import decimal

cheese_kg = decimal.Decimal('0.234')
cheese_price_kg = decimal.Decimal('132.64')

final_cost = cheese_kg * cheese_price_kg
final_cost = final_cost.quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_HALF_UP)

# representation
divider_symbol = '$'
divider = divider_symbol * 30
cheese_emoji = '\U0001F9C0'  # 🧀
shop_name = 'АТБ'
header = f'{divider} {shop_name} {divider}'
length_header = len(header)
footer = divider_symbol * length_header

# result output
print(header)

print('Товар\t\tвага\t\tціна\t\tвартість')
print(f'Сир{cheese_emoji}\t\t{cheese_kg}\t\t{cheese_price_kg}\t\t{final_cost}')

print(footer)

print()
