def calculateSum(numbers):
    if numbers.__len__() == 0:
        return 0
    else:
        result = 0
        for i in numbers:
            result = result + i
        return result


def calculateProduct(numbers):
    if numbers.__len__() == 0:
        return 1
    else:
        product = 1
        for i in numbers:
            product = product * i
        return product


def average(numbers):
    if numbers.__len__() == 0:
        return None
    else:
        result = 0
        for i in numbers:
            result = result + i
        return result / numbers.__len__()


def median(numbers):
    if numbers.__len__() == 0:
        return None
    else:
        numbers.sort()
        middleIndex = numbers.__len__() // 2
        if numbers.__len__() % 2 == 0:
            return (numbers[middleIndex] + numbers[middleIndex - 1]) / 2
        else:
            return numbers[middleIndex]


if __name__ == '__main__':
    print('Calculate Sum Check')
    print(calculateSum([]) == 0)
    print(calculateSum([2, 4, 6, 8, 10]) == 30)
    print(calculateProduct([]) == 1)
    print(calculateProduct([2, 4, 6, 8, 10]) == 3840)
    print('\nCalculate Average Check')
    print(average([]) is None)
    print(average([1, 2, 3]) == 2)
    print(average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2)
    print(average([12, 20, 37]) == 23)
    print(average([0, 0, 0, 0, 0]) == 0)
    print('\nCalculate Median Check')
    print(median([]) is None)
    print(median([1, 2, 3]) == 2)
    print(median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5)
    print(median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6)

# %%
