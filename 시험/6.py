# turtle로 막대그래프 그리는 코드
import turtle as t
# turtle 함수 라이브러리 이용

print('공백기준 4개의 값을 입력하시오.')
num_1, num_2, num_3, num_4 = input().split()
# 공백 기준 3개의 값 입력받기

num_1 = int(num_1)
num_2 = int(num_2)
num_3 = int(num_3)
num_4 = int(num_4)
# 자료형 정수로 변환하기

sum = num_1 + num_2 + num_3 + num_4

ratio_1 = num_1/sum*360
ratio_2 = num_2/sum*360
ratio_3 = num_3/sum*360
ratio_4 = num_4/sum*360
# width = 20
# # 넓이 고정 지정
# move = 20*2
# # 넓이의 두배만큼 이동

r = 100


t.circle(r)
t.left(90)
t.forward(r)
t.left(180)
t.left(ratio_1)
t.forward(r)

t.penup()
t.left(180)
t.forward(r)
t.left(180)
t.pendown()
t.left(ratio_2)
t.forward(r)

t.penup()
t.left(180)
t.forward(r)
t.left(180)
t.pendown()
t.left(ratio_3)
t.forward(r)

t.penup()
t.left(180)
t.forward(r)
t.left(180)
t.pendown()
t.left(ratio_4)
t.forward(r)

t.done()

# def drawing_graph(length, move):
#     for i in range(3):
#         t.forward(length)
#         t.left(120)
#     t.penup()
#     t.forward(length)
#     t.pendown()
#     t.forward(move)
# 높이 받아서 막대그래프 그리는 함수
# ( move는 옆으로 얼마나 이동할 것인지를 나타낸다. )


# input 값만큼 높이 가지는 함수를 그려준다.
# drawing_graph(num_1, move)
# drawing_graph(num_2, move)
# drawing_graph(num_3, 0)
# # 마지막은 더 옆으로 갈 필요가 없어서 0

# t.done()
