"""
Exercise 19 : Password Generator
"""
import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'  # 26
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 26
NUMBERS = '1234567890'  # 10
SPECIAL = '~!@#$%^&*()_+'  # 13

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def gen_password(char_num):
    # TODO : complete this
    password = []
    if char_num < 12:
        char_num = 12
    password.append((random.choice(LOWER_LETTERS)))
    password.append((random.choice(UPPER_LETTERS)))
    password.append((random.choice(NUMBERS)))
    password.append((random.choice(SPECIAL)))
    for i in range(char_num-4):
        password.append(random.choice(ALL_CHARS))
    random.shuffle(password)
    return password

