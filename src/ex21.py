"""
Exercise 21 : Validate Date
"""


def is_valid_date(year, month, day):
    """
    Check if a given date is valid.

    Parameters:
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # important to import here
    from src.ex20 import is_leap_year

    # FIX : complete this
    if is_leap_year(year) is True:
        if month in range(1, 13):
            if month == 2:
                if day in range(1, 30):
                    return True
                else:
                    return False
            if month in [4, 6, 9, 11]:
                if day in range(1, 31):
                    return True
                else:
                    return False
            else:
                if day in range(1, 32):
                    return True
                else:
                    return False
        else:
            return False
    else:
        if month in range(1, 13):
            if month == 2:
                if day in range(1, 29):
                    return True
                else:
                    return False
            if month in [4, 6, 9, 11]:
                if day in range(1, 31):
                    return True
                else:
                    return False
            else:
                if day in range(1, 32):
                    return True
                else:
                    return False
        else:
            return False
# %%
