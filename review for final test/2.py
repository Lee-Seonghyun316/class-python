# 수식을 입력 받아 답을 내시오
# 이차 방정식 두개를 입력하여 그 식을 만족하는 X와 Y의 값을 출력하시오
# x, y 없는 경우 생각하지 않음

# 3x+4y = 10
# 5x+3y = 7
# Day10 1 참고

# 다항식 해 구하기 -> 시험 출제 가능성
import numpy as np
from numpy.core.defchararray import array
# a = np.array([[2, 3], [1, -2]])
# b = np.array([1, 4])
# c = np.linalg.solve(a, b)
# print(c)

new_first = list(input("공백기준 첫번째 일차다항식 입력: "))
new_second = input("공백기준 두번째 일차다항식 입력: ")

# print(new_first)

for i in range(0, len(new_first)):
    if new_first[i] == 'x':
        a1 = new_first[0:i]
        y_index = i+1
    if new_first[i] == 'y':
        b1 = new_first[y_index+1:i]
        y_index = i
    if new_first[i] == '=':
        c1 = new_first[i+1:len(new_first)]

for i in range(0, len(new_second)):
    if new_second[i] == 'x':
        a2 = new_second[0:i]
        y_index = i+1
    if new_second[i] == 'y':
        b2 = new_second[y_index+1:i]
    if new_second[i] == '=':
        c2 = new_second[i+1:len(new_first)]


def making_int(list_a):
    # list_a = list(map(int, list_a))
    text = ""
    for i in list_a:
        text += i
    number = int(text)
    return number


a1 = making_int(a1)
# print(a)
b1 = making_int(b1)
c1 = making_int(c1)

a2 = making_int(a2)
# print(a)
b2 = making_int(b2)
c2 = making_int(c2)


A = []
A.append([a1, b1])
A.append([a2, b2])
print(A)
B = []
B.append(c1)
B.append(c2)
print(B)

A = np.array(A)
B = np.array(B)

C = np.linalg.solve(A, B)
print("X : {} Y: {}".format(C[0], C[1]))
