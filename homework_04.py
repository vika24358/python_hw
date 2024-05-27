from constants_homework_04 import MSG_FAVOURITE_FOOD, MSG_FOOD_RECIPE

header_footer = '~' * 50

print(header_footer)

food_name = input(MSG_FAVOURITE_FOOD).strip().upper()
food_recipe = input(MSG_FOOD_RECIPE).strip().lower()

beauty = '*' * 10

print(f'{beauty}{food_name}{beauty} ')
print(f'{food_recipe} 😋')
print(f'{food_recipe}'.count('мясо'))

print(header_footer)
