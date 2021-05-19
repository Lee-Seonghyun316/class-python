from random import *

dice = [1, 2, 3, 4, 5, 6]
a_list = []
for i in range(0, 100):
    a = randint(1, 6)
    a_list.append(a)

b_list = [x for x in a_list if x > 3]

print(b_list)
