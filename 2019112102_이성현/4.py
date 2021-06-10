import turtle as t

n = 6
t.penup
for i in range(3):
    t.forward(100)
    t.right(360 / n)
t.pendown
# 출발위치 설정

n = 6    # 육각형
t.shape('turtle')
t.color('green')          # 펜의 색을 빨간색으로 설정
t.begin_fill()          # 색칠할 영역 시작
for i in range(n):      # n번 반복
    t.forward(100)
    t.right(360 / n)    # 360을 n으로 나누어서 외각을 구함
t.end_fill()            # 색칠할 영역 끝


n = 5   # 육각형
t.shape('turtle')
t.color('gray')          # 펜의 색을 빨간색으로 설정
t.begin_fill()          # 색칠할 영역 시작
for i in range(n):      # n번 반복
    t.forward(100)
    t.right(360 / n)    # 360을 n으로 나누어서 외각을 구함
t.end_fill()            # 색칠할 영역 끝


n = 4   # 육각형
t.shape('turtle')
t.color('blue')          # 펜의 색을 빨간색으로 설정
t.begin_fill()          # 색칠할 영역 시작
for i in range(n):      # n번 반복
    t.forward(100)
    t.right(360 / n)    # 360을 n으로 나누어서 외각을 구함
t.end_fill()            # 색칠할 영역 끝

n = 3   # 육각형
t.shape('turtle')
t.color('skyblue')          # 펜의 색을 빨간색으로 설정
t.begin_fill()          # 색칠할 영역 시작
for i in range(n):      # n번 반복
    t.forward(100)
    t.right(360 / n)    # 360을 n으로 나누어서 외각을 구함
t.end_fill()            # 색칠할 영역 끝


t.forward(100)

t.done
