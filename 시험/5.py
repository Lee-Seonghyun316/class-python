import datetime as dt

name, born_year, born_month, born_date = input(
    "공백기준으로 이름과 생일을 입력해주세요\n (예 : 김철수 1979 01 01) \n").split()
age = dt.datetime.today().year - int(born_year) + 1

print("대상자는 현재 {}살입니다.".format(age))


exam_day = dt.datetime.now()
born_day = dt.datetime(int(born_year), int(born_month), int(born_date))

TimeInterval = exam_day-born_day
print("태어난 날부터 오늘까지 {} 일이 지났습니다. ".format(TimeInterval.days))
