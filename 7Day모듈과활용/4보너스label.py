# 계산기 만드는 코드(input값이 두개인 특이한 형태)
# 이런 시간이 오래 걸리는 코드는 안 나올 가능성이 크다
# label사용
# 여러 자리수 계산 가능
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
Label(window, text="첫번째 숫자를 입력하고 \n 사칙연산 기호 중 하나를 누룹니다. \n 이후, 두번째 숫자를 입력하고 \n 등호를 누르면 결과를 확인할 수 있습니다. ").grid(
    row=7, column=1)
# 사용법 해설

res_label = Label(window, text='출력값')
# 출력값 라벨
res_label.grid(column=0, row=2)

input_label1 = Label(window, width=10, text=0, bg='white')
input_label1_text = ""
input_label1.grid(row=0, column=1)

input_label2 = Label(window, width=10, text=0, bg='white')
input_label2_text = " "
input_label2.grid(column=1, row=1)

result = Label(window, width=10, text=0, bg='white')
# 결과 출력하는 라벨 설정
result_text = "0"
# 결과의 Initial 값 설정
result.grid(column=1, row=2)

# 사칙연산 기호 삽입함수


def add(value):
    global input_label1_text
    input_label1_text = input_label1_text+value
    input_label1.configure(text=input_label1_text)


def minus(value):
    global input_label1_text
    input_label1_text = input_label1_text+value
    input_label1.configure(text=input_label1_text)


def multi(value):
    global input_label1_text
    input_label1_text = input_label1_text+value
    input_label1.configure(text=input_label1_text)


def div(value):
    global input_label1_text
    input_label1_text = input_label1_text+value
    input_label1.configure(text=input_label1_text)

# 결과 출력 , 연산 함수


def cal():
    global result_text
    global input_label1_text
    global input_label2_text
    list_input_label1_text = list(input_label1_text)
    print(list_input_label1_text)
    if "+" in list_input_label1_text:
        list_input_label1_text.remove("+")
        input_label1_text = "".join(list_input_label1_text)
        print(input_label1_text)
        result_text = str(float(input_label1_text)+float(input_label2_text))
        result.configure(text=result_text)
    elif "-" in list_input_label1_text:
        list_input_label1_text.remove("-")
        input_label1_text = "".join(list_input_label1_text)
        print(input_label1_text)
        result_text = str(float(input_label1_text)-float(input_label2_text))
        result.configure(text=result_text)
    elif "/" in list_input_label1_text:
        list_input_label1_text.remove("/")
        input_label1_text = "".join(list_input_label1_text)
        print(input_label1_text)
        result_text = str(float(input_label1_text)/float(input_label2_text))
        result.configure(text=result_text)
    elif "*" in list_input_label1_text:
        list_input_label1_text.remove("*")
        input_label1_text = "".join(list_input_label1_text)
        print(input_label1_text)
        result_text = str(float(input_label1_text)*float(input_label2_text))
        result.configure(text=result_text)


def button_pressed(value):
    global input_label1_text
    global input_label2_text
    list_input_label1_text = list(input_label1_text)
    print(list_input_label1_text)
    if "+" in list_input_label1_text:
        input_label2_text = input_label2_text+value
        input_label2.configure(text=input_label2_text)
    elif "-" in list_input_label1_text:
        input_label2_text = input_label2_text+value
        input_label2.configure(text=input_label2_text)
    elif "/" in list_input_label1_text:
        input_label2_text = input_label2_text+value
        input_label2.configure(text=input_label2_text)
    elif "*" in list_input_label1_text:
        input_label2_text = input_label2_text+value
        input_label2.configure(text=input_label2_text)

    else:
        input_label1_text = input_label1_text+value
        input_label1.configure(text=input_label1_text)

    print(value, "pressed")


Label_value = StringVar(window, value='')


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
