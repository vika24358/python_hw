from pywebio.input import input as input_pw
from pywebio.input import NUMBER
from pywebio.output import put_text, put_html, put_image

import constants_pizza

# header
put_html('<h1>Вас вітає Буфет</h1>')
put_html('<h2>Будь ласка, зробіть замовлення</h2>')

# input section
name = str(input_pw(constants_pizza.msg_ask_name)).title()

formatted_order_pizza = f'Добрий день, {name}! Скільки акційних піц бажаєте замовити?'
put_text(formatted_order_pizza)

pizza_count_order = input_pw(constants_pizza.msg_enter_quantity, type=NUMBER)

pizza_order_cost = pizza_count_order * constants_pizza.pizza_cost

formatted_order_cola = f'{name}, ще дуже рекомендуємо колу по {constants_pizza.cola_cost} грн за пляшку'
put_text(formatted_order_cola)
cola_count_order = input_pw(constants_pizza.msg_enter_quantity, type=NUMBER)
cola_order_cost = cola_count_order * constants_pizza.cola_cost

total_cost = cola_order_cost + pizza_order_cost
put_text(f'Загальна вартість замовлення: {total_cost} грн')

img = open('a6bdb196bee23faef1d8020319c7c64750ef7686.avif', 'rb').read()
put_image(img, width='500px')
