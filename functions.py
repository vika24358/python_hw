# # user_name = input('Enter your name: ')
# # normalized_user_name = user_name.strip().title()
# # print(normalized_user_name)
# #
# #
# # user_surname = input('Enter your surname: ')
# # normalized_user_surname = user_surname.strip().title()
# # print(normalized_user_surname)
#
#
# def get_normalized_print(message):
#     user_name = input(message)
#     normalized_user_name = user_name.strip().title()
#     print(normalized_user_name)
#
#
# # get_normalized_print('Enter your name: ')
# # get_normalized_print('Enter your surname: ')
#
#

#
#
#
# def can_you_swim(answer):
#     positive_part = 'yes'
#     result = positive_part in answer.lower()
#     return result
#
# print(can_you_swim('yes'))
# print(can_you_swim('no'))


def add_two_numbers(number_1, number_2):
    result = number_1 + number_2
    return result


def divide_two_numbers(divided, divider):
    """divider must not equal zero"""  # documentation string
    result = divided / divider
    return result


def count_equation(first_add_number, second_add_number, divider):
    summa = add_two_numbers(first_add_number, second_add_number)
    division_result = divide_two_numbers(summa, divider)
    return division_result


result = count_equation(15, 85, 10)
print(result)

print()
