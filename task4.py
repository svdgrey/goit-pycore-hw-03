from datetime import date, datetime, timedelta


# Function returns the next birthday date based on the given date of birth.
def get_next_birthday(date_of_birth: date, today: date) -> date:

    next_birthday = date_of_birth.replace(year=today.year)

    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    return next_birthday

# Function returns a list of upcoming birthdays from the given list of birthdays.
# Parameters:
# - birthdays: A list of dictionaries, each containing 'name' and 'birthday' keys.
# 
# Returns a list of people who have upcoming birthdays within the next 7 days, in format 'name' and 'congratulation_date' keys
def get_upcoming_birthdays(birthdays: list[dict[str, str]]) -> list[dict[str, str]]:

    upcoming_birthdays = []
    today = datetime.today().date()

    for birthday_record in birthdays:
        name = birthday_record['name']
        date_of_birth = datetime.strptime(birthday_record['birthday'], '%Y.%m.%d').date()

        next_birthday = get_next_birthday(date_of_birth, today)
        
        if next_birthday - today <= timedelta(days=7):
            upcoming_birthdays.append({'name': name, 'congratulation_date': datetime.strftime(next_birthday, '%Y.%m.%d')})

    return upcoming_birthdays


#example usage
users = [
    {"name": "John Doe", "birthday": "1985.10.23"},
    {"name": "Jane Smith", "birthday": "1990.10.27"},
    {"name": "John Smith", "birthday": "1976.10.29"}
]
    
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

