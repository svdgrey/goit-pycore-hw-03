from datetime import date, datetime, timedelta


# Adjusts leap day birthdays to March 1 in non-leap years.
# Parameters:
# - date_of_birth: The date of birth of the person.
# - year: The year to adjust the birthday to.
#
# Returns:
#  The adjusted birthday date.
def adjust_leap_day_birthday(date_of_birth: date, year: int) -> date:
    try:
        return date_of_birth.replace(year=year)
    except ValueError:
        # Move February 29 birthdays to March 1
        return date_of_birth.replace(year=year, month=3, day=1)


# Find the next birthday, adjusting February 29 if necessary.
# Parameters:
# - date_of_birth: The date of birth of the person.
# - today: The current date.
#
# Returns:
#  The date of the next birthday.
def get_next_birthday(date_of_birth: date, today: date) -> date:
    next_birthday = adjust_leap_day_birthday(date_of_birth, today.year)

    # if the next birthday has already passed this year, adjust to the next year
    if next_birthday < today:
        next_birthday = adjust_leap_day_birthday(date_of_birth, today.year + 1)

    return next_birthday


# Return birthdays occurring within the next 7 days, including today.
# Move congratulation dates from weekends to Monday.
def get_upcoming_birthdays(birthdays: list[dict[str, str]]) -> list[dict[str, str]]:
    upcoming_birthdays = []
    today = datetime.today().date()

    for birthday_record in birthdays:
        name = birthday_record["name"]

        try:
            date_of_birth = datetime.strptime(birthday_record["birthday"], "%Y.%m.%d").date()
        except ValueError:
            continue

        next_birthday = get_next_birthday(date_of_birth, today)
               
        if 0 <= (next_birthday - today).days <= 7:
            weekday = next_birthday.weekday()

            # Move weekend birthday to Monday
            if weekday >= 5:
                next_birthday += timedelta(days=(7 - weekday))

            congratulation_date = next_birthday

            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming_birthdays



# Example usage
if __name__ == "__main__":

    users = [
        {"name": "John Doe", "birthday": "1985.10.23"},
        {"name": "Jane Smith", "birthday": "1990.10.27"},
        {"name": "Sarge Gray", "birthday": "1990.10.24"},
        {"name": "John Smith", "birthday": "1976.10.29"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)


