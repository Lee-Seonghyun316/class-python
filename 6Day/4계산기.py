# 계산기 만드는 코드(input값이 두개인 특이한 형태)
# 이런 시간이 오래 걸리는 코드는 안 나올 가능성이 크다
from tkinter import *
from tkinter import ttk
# 라이브러리 선언

window = Tk()
# 창 하나 만들고
window.title('계산기')
# 제목 달아주고
window.geometry('400x4000')
# 윈도우 크기 설정해주고
Label(window, text='입력값').grid(column=0, row=0)
# 입력값 lavel 생성, 위치 설정
Label(window, text='입력값').grid(column=0, row=1)
# 입력값 lavel 생성
Label(window, text="입력값에 포커스를 준 후,\n 번호를 클릭하면 번호가 입력됩니다.\n 이후 연산자를 누르면 \n입력값에 표시되고 \n등호를 눌러 결과를 확인합니다. \n").grid(
    row=7, column=1)
# 사용법 해설
res_label = Label(window, text='출력값')
# 출력값 라벨
res_label.grid(column=0, row=2)

# input1 = Entry(window, width=10)
input2 = Entry(window, width=10)
# entry 생성
result = Label(window, width=10, text=0, bg='white')
# 결과 출력하는 라벨 설정
result_text = "0"
# 결과의 Initial 값 설정

# input1.grid(column=1, row=0)
input2.grid(column=1, row=1)
result.grid(column=1, row=2)

# 계산 함수(기호 출력과 계산 동시 수행)


def add(value):
    global result_text
    result_text = str(float(input1.get())+float(input2.get()))
    input1.insert("end", value)


def minus(value):
    global result_text
    result_text = str(float(input1.get())-float(input2.get()))
    input1.insert("end", value)


def multi(value):
    global result_text
    result_text = str(float(input1.get())*float(input2.get()))
    input1.insert("end", value)


def div(value):
    global result_text
    result_text = str(float(input1.get())/float(input2.get()))
    input1.insert("end", value)

# 결과 출력 함수


def cal():
    global result_text
    result.configure(text=result_text)


def button_pressed(value):
    a = window.focus_get()
    # 텍스트 창으로 숫자 전송.'end'는 오른쪽끝에 추가하라는 의미.
    a.insert("end", value)
    print(value, "pressed")
# 버튼 누르면 화면에 입력됨


# 텍스트창의 값 저장할 변수.
entry_value = StringVar(window, value='')

# textvariable 속성으로 변수 설정.
input1 = ttk.Entry(window, textvariable=entry_value, width=10)
input1.grid(row=0, column=1)
# number_entry.grid(row=1, column=1)


btn_1 = Button(window, text='1', command=lambda: button_pressed('1'))
btn_1.grid(column=0, row=3)
btn_2 = Button(window, text='2', command=lambda: button_pressed('2'))
btn_2.grid(column=1, row=3)
btn_3 = Button(window, text='3', command=lambda: button_pressed('3'))
btn_3.grid(column=2, row=3)
btn_4 = Button(window, text='4', command=lambda: button_pressed('4'))
btn_4.grid(column=0, row=4)
btn_5 = Button(window, text='5', command=lambda: button_pressed('5'))
btn_5.grid(column=1, row=4)
btn_6 = Button(window, text='6', command=lambda: button_pressed('6'))
btn_6.grid(column=2, row=4)
btn_7 = Button(window, text='7', command=lambda: button_pressed('7'))
btn_7.grid(column=0, row=5)
btn_8 = Button(window, text='8', command=lambda: button_pressed('8'))
btn_8.grid(column=1, row=5)
btn_9 = Button(window, text='9', command=lambda: button_pressed('9'))
btn_9.grid(column=2, row=5)
btn_0 = Button(window, text='0', command=lambda: button_pressed('0'))
btn_0.grid(column=0, row=6)
btn_result = Button(window, text='=', command=cal)
btn_result.grid(column=2, row=6)
btn_plus = Button(window, text='+', command=lambda: add('+'))
btn_plus.grid(column=3, row=3)
btn_minus = Button(window, text='-', command=lambda: minus('-'))
btn_minus.grid(column=3, row=4)
btn_mult = Button(window, text='*', command=lambda: multi('*'))
btn_mult.grid(column=3, row=5)
btn_div = Button(window, text='/', command=lambda: div('/'))
btn_div.grid(column=3, row=6)

window.mainloop()
