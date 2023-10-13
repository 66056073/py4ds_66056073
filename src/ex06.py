"""
Execise 6
"""


def ordinal_suffix(num):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # FIX : complete this
    if num.__str__()[-2:] == '11' or num.__str__()[-2:] == '12' or num.__str__()[-2:] == '13':
        return num.__str__() + 'th'
    elif num.__str__()[-1:] == '1':
        return num.__str__() + 'st'
    elif num.__str__()[-1:] == '2':
        return num.__str__() + 'nd'
    elif num.__str__()[-1:] == '3':
        return num.__str__() + 'rd'
    else:
        return num.__str__() + 'th'
