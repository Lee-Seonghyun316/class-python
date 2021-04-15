import random as rd
initial_list = []


def making_list(a_list):
    for i in range(1, 46):
        a_list.append(i)
    return a_list


making_list(initial_list)
six_list = rd.sample(initial_list, 6)
sort_list = sorted(six_list)

print(sort_list)
