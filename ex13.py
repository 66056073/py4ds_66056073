def calculateSum(list_data):
    if list_data.__len__() == 0:
        return 0
    else:
        total = 0
        for i in list_data:
            total = total + i
        return total


def calculateProduct(list_data):
    if list_data.__len__() == 0:
        return 1
    else:
        product = 1
        for i in list_data:
            product = product * i
        return product


def average(list_data):
    if list_data.__len__() == 0:
        return 0
    else:
        total = 0
        for i in list_data:
            total = total + i
        return total / list_data.__len__()


if __name__ == '__main__':
    print(calculateSum([]) == 0)
    print(calculateSum([2, 4, 6, 8, 10]) == 30)
    print(calculateProduct([]) == 1)
    print(calculateProduct([2, 4, 6, 8, 10]) == 3840)
    print(average([1, 2, 3]) == 2)
    print(average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2)
    print(average([12, 20, 37]) == 23)
    print(average([0, 0, 0, 0, 0]) == 0)

# %%
