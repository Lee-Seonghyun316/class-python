# 각 학년의 과목별 최고점 구하기
# 학년 과목이 같은 것들끼리 성적끼리의 max 구하기
import pandas as pd
from pandas import DataFrame

test = pd.read_csv('./Day13/시험 성적.csv', index_col=2, encoding='UTF-8')

first_name = list(test["성"])
# print(first_name)
grade = list(test["학년"])
# print(grade)

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

for i in range(0, len(test)):
    now_name = first_name[i]
    now_grade = grade[i]

    if last_grade != now_grade:
        kim_max = test.iloc[list_kim, :].max()
        lee_max = test.iloc[list_lee, :].max()
        park_max = test.iloc[list_park, :].max()
        last_grade = now_grade
        text1 = ["{} 학년에서 {} 씨에서 점수가 가장 높은 사람 : {}{}".format(
            kim_max.iloc[0], kim_max.iloc[2], kim_max.iloc[2], kim_max.iloc[3])]
        text2 = ["{} 학년에서 {} 씨에서 점수가 가장 높은 사람 : {}{}".format(
            lee_max.iloc[0], lee_max.iloc[2], lee_max.iloc[2], lee_max.iloc[3])]
        text3 = ["{} 학년에서 {} 씨에서 점수가 가장 높은 사람 : {}{}".format(
            park_max.iloc[0], park_max.iloc[2], park_max.iloc[2], park_max.iloc[3])]

        text_list.append(text1)
        text_list.append(text2)
        text_list.append(text3)
        # print(text)

    if now_name == "김":
        list_kim.append(i)
    if now_name == "이":
        list_lee.append(i)
    if now_name == "박":
        list_park.append(i)

kim_max = test.iloc[list_kim, :].max()
lee_max = test.iloc[list_lee, :].max()
park_max = test.iloc[list_park, :].max()
last_grade = now_grade
text1 = ["{} 학년에서 {} 씨에서 점수가 가장 높은 사람 : {}{}".format(
    kim_max.iloc[0], kim_max.iloc[2], kim_max.iloc[2], kim_max.iloc[3])]
text2 = ["{} 학년에서 {} 씨에서 점수가 가장 높은 사람 : {}{}".format(
    lee_max.iloc[0], lee_max.iloc[2], lee_max.iloc[2], lee_max.iloc[3])]
text3 = ["{} 학년에서 {} 씨에서 점수가 가장 높은 사람 : {}{}".format(
    park_max.iloc[0], park_max.iloc[2], park_max.iloc[2], park_max.iloc[3])]

text_list.append(text1)
text_list.append(text2)
text_list.append(text3)

dataframe = pd.DataFrame(text_list)
dataframe.to_csv("./Day13/학년성씨별 최고점.csv", header=False, index=False)
