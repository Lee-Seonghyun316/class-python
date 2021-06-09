# 5. 6면체 주사위를 100 번 굴려서 4,5,6 이 나오면 리스트에 저장하시오
# list comprehension을 사용하여 저장하시오.

from random import *

dice = [1, 2, 3, 4, 5, 6]
a_list = []
for i in range(0, 100):
    a = randint(1, 6)
    a_list.append(a)

b_list = [x for x in a_list if x > 3]

print(b_list)
