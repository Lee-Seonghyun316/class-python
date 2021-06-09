# Day9 폴더 안에 4.txt 있어야 실행 된다!

# 4. 학생에 대한 정보를 클래스를 생성하시오
# 해당 클래스에는 이름, 국어성적, 수학성적, 영어성적을 가질 수 있어야 함
# 음수 성적을 받지 않도록 캡슐화 하시오
# 자기 자신의 평균 성적을 구하는 even 메소드를 만드시오

# 학생의 정보(이름, 국어성적, 수학성적, 영어성적)을 파일로부터 입력받고
# enen 메소드를 사용하여 학생 개인의 평균 성적을 화면에 출력하시오

# * 제출시 참고한 학생 파일도 제출하시오.


class Student:
    def __init__(self, name, kor, math, eng):
        self.__name = name

        self.__kor = int(kor)
        self.__math = int(math)
        self.__eng = int(eng)

    def __str__(self):
        return 'Student(이름 : '+self.__name+', 국어점수 : '+str(self.__kor)+', 수학점수 : '+str(self.__math)+', 영어점수 : '+str(self.__eng)+')'

    def even(self):
        return (self.__kor+self.__math+self.__eng)/3

    def set_math(self, math):
        if math >= 0:
            self.__kor = math

    def get_math(self):
        return self.__math

    def set_eng(self, eng):
        if eng >= 0:
            self.__kor = eng

    def get_eng(self):
        return self.__eng

    def set_kor(self, kor):
        if kor >= 0:
            self.__kor = kor

    def get_kor(self):
        return self.__kor


f = open("./Day10 람다함수와 리스트 축약/4.txt", 'r')
data = f.read()
f.close()

data_list = list(data.split())

Erica = Student(data_list[0], data_list[1], data_list[2], data_list[3])

# Erica = Student('Erica', '90', '100', '90')
print(Erica)
print('평균 : {}'.format(Erica.even()))
# 양수는 할당 가능
Erica.set_kor(100)
print(Erica)

# 음수는 할당 불가능
Erica.set_kor(-90)
print(Erica)
