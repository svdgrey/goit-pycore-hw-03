from datetime import datetime

# The function returns the number of days from today to the given date
# The function expects the date to be in the format "YYYY-MM-DD"
#
# Returns:
# - positive if date is in the past
# - negative if date is in the future
# - 0 if the date is today
#
# Since the task did not specify how to handle errors in the input parameter, 
# function returns None if the date is not a valid date
def get_days_from_today(date: str) -> int:
    try:
        arg_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return None
    
    delta = datetime.today() - arg_date
    return delta.days


# Example usage:
chosen_date = "2026-10-01"
days_from_today = get_days_from_today(chosen_date)
print(f"Days from today for '{chosen_date}': {days_from_today}")


# test cases (tested on 20.10.2026)
assert get_days_from_today("2026-10-20") == 0 # today's date is 20.10.2026
assert get_days_from_today("2026-10-01") == 19 # past date
assert get_days_from_today("2026-10-23") == -3 # future date
assert get_days_from_today("2026-10-23abc") is None # invalid date
