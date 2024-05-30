amount_of_people = 4
entrance_ticket_hrn = 500
taxi_to_park_hrn = 600
amount_of_pizzas = 2
price_per_pizza = 250
airhockey_rounds = 8
price_per_round = 80

# рахуємо білети в парк
entrance_total = entrance_ticket_hrn * amount_of_people

# рахуємо ціну на таксі
twenty_percent_from_taxi = taxi_to_park_hrn * 0.2
taxi_from_park_hrn = taxi_to_park_hrn + twenty_percent_from_taxi
taxi_total = taxi_to_park_hrn + taxi_from_park_hrn

# рахуємо піцу
two_pizzas_price = price_per_pizza * amount_of_pizzas
pizza_discount = two_pizzas_price * 0.15
pizza_total_price = two_pizzas_price - pizza_discount

# рахуємо аерохокей
airhockey_total = airhockey_rounds * price_per_round

# дізнаємося, скільки винна кожна людина
total_price = airhockey_total + pizza_total_price + taxi_total + entrance_total
price_per_person = total_price / amount_of_people

print(f'{price_per_person=}')
