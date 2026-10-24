import random

# Generate a sorted list of unique random numbers in the given range.
#
# Function parameters:
# min - the minimum number in the set, must be greater than or equal to 1
# max - the maximum number in the set, must not exceed 1000
# quantity - the number of unique numbers to return in the set
#
# Return:
#  an empty list if the parameters are invalid.
#  a sorted list of unique random numbers otherwise.
def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if not (1 <= min <= max <= 1000):
        return []

    # Check that enough unique numbers are available.
    if not (1 <= quantity <= (max - min + 1)):
        return []

    numbers_range = range(min, max + 1)
    
    generated_sample = random.sample(numbers_range, quantity)
    return sorted(generated_sample)



# Example usage:
lottery_numbers  = get_numbers_ticket(1, 36, 6)
print(f" Generated lottery numbers: {lottery_numbers}")


# Tests cases
if __name__ == "__main__":
    assert get_numbers_ticket(0, 36, 6) == []
    assert get_numbers_ticket(1, 36, 0) == []
    assert get_numbers_ticket(1, 1001, 6) == []
    assert get_numbers_ticket(1, 100, 101) == []
    assert get_numbers_ticket(10, 12, 4) == []
    assert get_numbers_ticket(5, 5, 1) == [5]
    numbers = get_numbers_ticket(1, 49, 6)
    assert len(numbers) == 6
    assert len(set(numbers)) == 6
    assert numbers == sorted(numbers)
