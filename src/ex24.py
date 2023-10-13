"""
Exercise 24 : Every 15 minutes, ante meridiem (am) and post meridiem (pm)
ante : before
post : after
meridiem : midday
"""


def get_time_every_15_min():
    """
    Generate a time string every 15 minutes.

    This function iterates through the meridiems, hours, and minutes to generate a time string
    for every 15 minutes. It prints the time string in the format "hour:minute meridiem".

    Returns:
        str: The generated time string.
    """
    # FIX : complete this
    minute = 15
    print('12:00 am')
    for i in range(3):
        print('12:' + str(minute) + ' am')
        minute += 15
    minute = 15

    for i in range(1, 12):
        print(str(i) + ':00 am')
        for j in range(3):
            print(str(i) + ':' + str(minute) + ' am')
            minute += 15
        minute = 15

    print('12:00 pm')
    for i in range(3):
        print('12:' + str(minute) + ' pm')
        minute += 15
    minute = 15
    for i in range(1, 12):
        print(str(i) + ':00 pm')
        for j in range(3):
            print(str(i) + ':' + str(minute) + ' pm')
            minute += 15
        minute = 15


if __name__ == '__main__':
    get_time_every_15_min()

