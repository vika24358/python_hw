def add_two_numbers(number1: int | float, number2: int | float) -> float:
    result = number1 + number2
    return float(result)


def multiply_by(number, by=2):
    return number * by


def get_two_time_string(number: int) -> str:
    result = str(multiply_by(number))
    return result