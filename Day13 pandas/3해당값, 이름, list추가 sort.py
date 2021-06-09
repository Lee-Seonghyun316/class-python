# 각 학년의 성씨별 최고점 구하기
# 숫자로 구해서 틀리는 경우 있었음
# 또한 여러 col을 고려해야 하니까
# max 2번 연산이 필요함
import pandas as pd
from pandas import DataFrame

test = pd.read_csv('./Day13 pandas/시험 성적.csv', index_col=2, encoding='UTF-8')

first_name = list(test["성"])
grade = list(test["학년"])

# first_name 으로 반복문
# 이전 first_name 다르면 처음인덱스first_index부터
#  이전인덱스까지의 Max 구하기

# 현재 인덱스를 처음인덱스에 넣기
# 현재 first_name 이전 first_name 넣기

# first_name 초기값은 "김"
# 처음 인덱스 초기값은 0
# 같으면 넘어가기

# 성씨는 붙어있지 않으니까
# 성씨별 리스트를 학년 마다 만들어서-> index 저장
# 그 중 max를 구하자
# g학년 바뀌면 성씨별 리스트 초기화

last_grade = 1
last_name = "김"
first_index = 0

# 이중 리스트로 csv 생성할 것임
text = ""
text_list = []

list_kim = []
list_lee = []
list_park = []

# 성씨별 학년별 max 값 출력해주는 함수


def grade_firstName_max(list_first_name, last_grade, first_name):
    kor_first_name_sort = test.iloc[list_first_name, :].sort_values('국어성적')
    kor_max = kor_first_name_sort.iloc[[len(kor_first_name_sort)-1], :].max()
    math_first_name_sort = test.iloc[list_first_name, :].sort_values('수학성적')
    math_max = math_first_name_sort.iloc[[
        len(math_first_name_sort)-1], :].max()
    eng_first_name_sort = test.iloc[list_first_name, :].sort_values('영어성적')
    eng_max = eng_first_name_sort.iloc[[len(eng_first_name_sort)-1], :].max()

    max_value = max(kor_max.iloc[4], math_max.iloc[5], eng_max.iloc[6])

    if max_value == kor_max.iloc[4]:
        name = kor_max.iloc[2]+kor_max.iloc[3]
    if max_value == math_max.iloc[5]:
        name = math_max.iloc[2]+math_max.iloc[3]
    if max_value == eng_max.iloc[6]:
        name = eng_max.iloc[2]+eng_max.iloc[3]
    text = ["{} 학년에서 {}씨에서 점수가 {}으로 가장 높은 사람 : {}".format(
        last_grade, first_name, max_value, name)]
    print(text)
    return text


for i in range(0, len(test)):
    now_name = first_name[i]
    now_grade = grade[i]

    if last_grade != now_grade:
        # 성씨별 list ㅡmax값 구하기
        text1 = grade_firstName_max(list_kim, last_grade, "김")
        text_list.append(text1)
        text1 = grade_firstName_max(list_lee, last_grade, "이")
        text_list.append(text1)
        text1 = grade_firstName_max(list_park, last_grade, "박")
        text_list.append(text1)

        last_grade = now_grade

        list_kim = []
        list_lee = []
        list_park = []
        # print(text)

    if now_name == "김":
        list_kim.append(i)
    if now_name == "이":
        list_lee.append(i)
    if now_name == "박":
        list_park.append(i)

text1 = grade_firstName_max(list_kim, last_grade, "김")
text_list.append(text1)
text1 = grade_firstName_max(list_lee, last_grade, "이")
text_list.append(text1)
text1 = grade_firstName_max(list_park, last_grade, "박")
text_list.append(text1)

dataframe = pd.DataFrame(text_list)
dataframe.to_csv("./Day13 pandas/학년성씨별 최고점.csv", header=False, index=False)
