"""
Exercise 15
"""


def median(num_list):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    if num_list.__len__() == 0:
        return None
    else:
        num_list.sort()
        middleIndex = num_list.__len__() // 2
        if num_list.__len__() % 2 == 0:
            return (num_list[middleIndex] + num_list[middleIndex - 1]) / 2
        else:
            return num_list[middleIndex]
