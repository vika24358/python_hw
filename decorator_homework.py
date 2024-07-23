from typing import Callable

result_dict = {}


def modifying_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result_dict.update({'result': result})
        return result_dict

    return wrapper


@modifying_decorator
def add_two_numbers(number1: int, number2: int) -> int:
    result = number1 + number2
    return result


add_two_numbers(1, 10)

print(result_dict)
