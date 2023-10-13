"""
Exercise 22 : Rock Paper Scissor
"""


def rps_check(p1, p2):
    """
    Check the result of a rock-paper-scissors game between two players.

    Parameters:
        p1 (str): The choice of player one. It can be 'rock', 'paper', or 'scissor'.
        p2 (str): The choice of player two. It can be 'rock', 'paper', or 'scissor'.

    Returns:
        str: The result of the game. It can be 'player one', 'player two', or 'tie'.
    """
    # FIX : complete this
    if p1 == p2:
        return 'tie'
    elif p1 == 'rock':
        if p2 == 'scissors':
            return 'player one'
        else:
            return 'player two'
    elif p1 == 'scissors':
        if p2 == 'paper':
            return 'player one'
        else:
            return 'player two'
    elif p1 == 'paper':
        if p2 == 'rock':
            return 'player one'
        else:
            return 'player two'
