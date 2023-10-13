"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(amount, price):
    discount_time = amount // 9
    return (amount - discount_time) * price


def get_cost_of_coffee_2(amount, price):
    discount_time = amount // 9
    return (amount - discount_time) * price
