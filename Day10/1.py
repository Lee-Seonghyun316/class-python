# 다항식 해 구하기 -> 시험 출제 가능성
import numpy as np
from numpy.core.defchararray import array
# a = np.array([[2, 3], [1, -2]])
# b = np.array([1, 4])
# c = np.linalg.solve(a, b)
# print(c)

new_a = list(map(int, input("공백기준 첫번째 일차다항식 입력: ").split()))
new_b = list(map(int, input("공백기준 두번째 일차다항식 입력: ").split()))

# print(new_a)
A = []
A.append(new_a[0:2])
A.append(new_b[0:2])
print(A)
B = []
B.append(new_a[2])
B.append(new_b[2])
print(B)

A = np.array(A)
B = np.array(B)

C = np.linalg.solve(A, B)
print("X : {} Y: {}".format(C[0], C[1]))
