import turtle as t
print('공백기준 3개의 값을 입력하시오.')
num_1, num_2, num_3 = input().split()
num_1 = int(num_1)
num_2 = int(num_2)
num_3 = int(num_3)

width = 20
move = 20*2


def drawing_graph(height, move):
    for i in range(4):
        if i % 2 == 1:
            t.forward(height)
        else:
            t.forward(width)
        t.left(90)
    t.penup()
    t.forward(width)
    t.pendown()
    t.forward(move)


drawing_graph(num_1, move)
drawing_graph(num_2, move)
drawing_graph(num_3, 0)

t.done()
