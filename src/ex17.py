"""
Exercise 17
"""
import random


def roll_dice(num_of_dice):
    """
    Calculate the total sum of rolling a certain number of dice.

    Parameters:
        num_of_dice (int): The number of dice to roll.

    Returns:
        int: The total sum of the dice rolls.
    """
    dice_point = (1, 2, 3, 4, 5, 6)
    sum_point = 0
    if num_of_dice == 0:
        return 0
    else:
        for i in range(num_of_dice):
            sum_point += random.choice(dice_point)
        return sum_point

