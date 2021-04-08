data_1, data_2 = input().split()
num_1 = int(data_1)
num_2 = int(data_2)


def mul(num_1, num_2):
    return num_1 * num_2


print(mul(num_1, num_2))


def div(num_1, num_2):
    if num_2 == 0:
        return 'error'
    else:
        return num_1 / num_2


print(div(num_1, num_2))


def plu(num_1, num_2):
    return num_1 + num_2


print(plu(num_1, num_2))


def min(num_1, num_2):
    return num_1 - num_2


print(min(num_1, num_2))
