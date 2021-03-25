born_year1 = input("당신이 태어난 연도를 입력하세요\n")
age = 2021 - int(born_year1) + 1

if 26 >= age >= 20:
    print("대학생")
elif 20 > age >= 17:
    print("고등학생")
elif 17 > age >= 14:
    print("중학생")
elif 14 > age >= 8:
    print("초등학생")
else:
    print("학생이 아닙니다. ")
