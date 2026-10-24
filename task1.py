from datetime import datetime, timedelta


# Returns the number of days from today to the given date
# argument: date in the format "YYYY-MM-DD"
#
# Returns: 
#  - positive for past dates, 
#  - negative for future dates, 
#  - and zero for today.
#  - None if the date is not valid
def get_days_from_today(date: str) -> int:
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return None

    today = datetime.today().date()
    return (today - given_date).days


# Example usage:
chosen_date = "2026-10-01"
days_from_today = get_days_from_today(chosen_date)
print(f"Days from today for '{chosen_date}': {days_from_today}")


# Test cases
if __name__ == "__main__":

    today = datetime.today().date()
    assert get_days_from_today(today.strftime("%Y-%m-%d")) == 0
    
    today_minus_5_days = (today - timedelta(days=5))
    assert get_days_from_today(today_minus_5_days.strftime("%Y-%m-%d")) == 5
    
    today_plus_5_days = (today + timedelta(days=5))
    assert get_days_from_today(today_plus_5_days.strftime("%Y-%m-%d")) == -5
    assert get_days_from_today("2026-10-23abc") is None
    