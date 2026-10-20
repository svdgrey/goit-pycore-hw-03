import random

# The function generates a set of unique random numbers for lotteries.
# The set of numbers is generated within the range from min to max (inclusive).
#
# Function parameters:
# min - the minimum number in the set, must be greater than or equal to 1
# max - the maximum number in the set, must not exceed 1000
# quantity - the number of unique numbers to return in the set
#
# Returns: a list of unique random sorted numbers or None if one or more parameters are invalid.
def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if max > 1000 or \
      not (1 <= min < max) or \
      not (min <= quantity <= max):
        return None 

    numbers_range = range(min, max + 1)
    
    generated_sample = random.sample(numbers_range, quantity)
    return sorted(generated_sample)


# Example usage:
lottery_numbers  = get_numbers_ticket(1, 36, 6)
print(f" Generated lottery numbers: {lottery_numbers}")


# tests with invalid parameters
assert get_numbers_ticket(0, 36, 6) is None # min is less than 1
assert get_numbers_ticket(1, 36, 0) is None # quantity is less than min
assert get_numbers_ticket(1, 1001, 6) is None # max is greater than 1000
assert get_numbers_ticket(1, 100, 101) is None # quantity is greater than max
