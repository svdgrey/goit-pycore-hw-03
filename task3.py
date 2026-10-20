import re

# Function normalizes phone number to international format. 
# If the phone number has wrong symbols, they will be removed.
# If the phone number is missing the international prefix, it will be added (+380).
def normalize_phone(phone_number: str) -> str:
    # remove all non-digit characters (except the leading +) from the phone number
    pattern = r'(?!^\+)\D'
    corrected_phone_number = re.sub(pattern, '', phone_number)

    #check if the phone number needs a prefix
    prefix = ''
    if not corrected_phone_number.startswith('+'):
        prefix = '+'
        if not corrected_phone_number.startswith('38'):
            prefix = prefix + '38'

    return f"{prefix}{corrected_phone_number}"


# Example usage:
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)