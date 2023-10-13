"""
Execise 12
"""


def get_smallest(num_list):
    """
    Get the smallest number from a list of numbers.

    Args:
        num_list (list): A list of numbers.

    Returns:
        int or None: The smallest number from the list. If the list is empty, returns None.
    """
    if num_list.__len__() == 0:
        return None
    else:
        smallest = num_list[0]
        for i in range(num_list.__len__()):
            if smallest > num_list[i]:
                smallest = num_list[i]
        return smallest
