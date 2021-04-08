def mul(*numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


print(mul(7, 2, 3))
