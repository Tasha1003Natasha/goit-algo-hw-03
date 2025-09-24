from random import randint

def get_numbers_ticket(min: int, max: int, quantity: int):
    """
    Generates a set of unique random numbers
    """

    min_value = 1 if min < 1 else min
    max_value = 1000 if max > 1000 else max

    if quantity > (max_value - min_value + 1):
          return []

    result_array = set()
    while len(result_array) != quantity:
        result_array.add(randint(min_value, max_value))

    result = sorted(list(result_array))
    return result
