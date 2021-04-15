def acc(num_1, num_2):
    mul = num_1 * num_2
    if num_2 == 0:
        div = 'error'
    else:
        div = num_1 / num_2
    plu = num_1 + num_2
    min = num_1 - num_2
    return mul, div, plu, min


data_1, data_2 = input().split()
num_1 = int(data_1)
num_2 = int(data_2)

print(acc(num_1, num_2))
