from random import randint

def get_numbers_ticket(min: int, max: int, quantity: int):
    """
    Generates a set of unique random numbers
    """

    if quantity > (max - min + 1)  or  min < 1 or  max > 1000 :
          return []

    result_array = set()
    while len(result_array) != quantity:
        result_array.add(randint(min, max))

    result = sorted(list(result_array))
    return result


# print(get_numbers_ticket(-10, 10, 5))