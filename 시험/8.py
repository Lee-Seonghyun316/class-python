from tkinter import *
from tkinter import ttk
import random as rd

initial_list = []


repeat = True

window = Tk()
# 창 하나 만들고
window.title('8번')
# 제목 달아주고
window.geometry('400x4000')
# 윈도우 크기 설정해주고
Label(window, text='합계').grid(column=0, row=0)
Label(window, text='랜덤 값').grid(column=0, row=1)
input_label1 = Label(window, width=10, text=0, bg='white')
input_label1_text = ""
input_label1.grid(row=1, column=1)

result = Label(window, width=10, text=0, bg='white')
# 결과 출력하는 라벨 설정
result_text = "0"
# 결과의 Initial 값 설정
result.grid(column=1, row=0)
result1 = 0
while repeat <= 15:
    plus = rd.randrange(1, 9)
    # 한자리수로 증가

    print(plus)
    input_label1.configure(text=plus)
    result1 = result1 + plus
    if result1 > 100:
        break
    # 100 이상 이면 끝내기
    else:
        print(result1)
        result.configure(text=result1)
    repeat = repeat+1
    # 15번까지만 반복


# btn = Button(window, text="랜덤버튼")
# btn.grid(column=2, row=0, command=)


# def cal():
#     global result_text
#     result_text = str(float(input_label1_text)+float(result_text))
#     result.configure(text=result_text)


window.mainloop()
