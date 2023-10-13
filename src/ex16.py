"""
Exercise 16
"""


def mode(num_list):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    mode_num = 0
    count = 0
    if num_list.__len__() == 0:
        return None
    else:
        for i in num_list:
            count_i = num_list.count(i)
            if count_i > count:
                count = count_i
                mode_num = i
        return mode_num


