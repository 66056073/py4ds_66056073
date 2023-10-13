"""
Exercise 11
"""


def get_hr_min_sec(tsec):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """
    s = tsec % 60
    m = (tsec // 60) % 60
    h = (tsec // 60) // 60

    if h > 0:
        if m > 0:
            if s > 0:
                return h.__str__() + 'h ' + m.__str__() + 'm ' + s.__str__() + 's'
            else:
                return h.__str__() + 'h ' + m.__str__() + 'm'
        else:
            if s > 0:
                return h.__str__() + 'h ' + s.__str__() + 's'
            else:
                return h.__str__() + 'h'
    else:
        if m > 0:
            if s > 0:
                return m.__str__() + 'm ' + s.__str__() + 's'
            else:
                return m.__str__() + 'm'
        else:
            return s.__str__() + 's'
