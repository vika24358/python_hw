def welcome_user(username):
    formatted_username = f'<h1>Вітаємо тебе, шановний {username}</h1>'
    return formatted_username


# example of function usage
greeting = welcome_user('Вікусік777')
print(greeting)


def calculate_rectangle_area(length, width):
    rectangle_area = length * width
    return rectangle_area


# example of function usage
result_rectangle_area = calculate_rectangle_area(6, 15)
print(result_rectangle_area)
