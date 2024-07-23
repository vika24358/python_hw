from typing import Callable


def modifying_decorator(func: Callable):

    def wrapper(*args, **kwargs):
        result_dict = {}
        result = func(*args, **kwargs)
        result_dict.update({'result': result})
        return result_dict

    return wrapper


@modifying_decorator
def add_two_numbers(number1: int, number2: int) -> int:
    result = number1 + number2
    return result


print(add_two_numbers(1, 10))
