# 각 학년의 과목별 최고점 구하기
# 학년 과목이 같은 것들끼리 성적끼리의 max 구하기
import pandas as pd
from pandas import DataFrame

test = pd.read_csv('./Day13/시험 성적.csv', index_col=2, encoding='UTF-8')

# class_number = list(test["반"])
grade = list(test["학년"])
# print(grade)

# grade 로 반복문
# 이전 학년과 다르면 처음인덱스first_index부터
#  이전인덱스까지의 Max 구하기
# 현재 인덱스를 처음인덱스에 넣기
# 현재 학년 이전 학년에 넣기
# 이전학년 last_grade 초기값은 1
# 처음 인덱스 초기값은 0
# 같으면 넘어가기

last_grade = 1
first_index = 0

# 이중 리스트로 csv 생성할 것임
text = ""
text_list = []

for i in range(0, len(test)):
    now_grade = grade[i]
    if last_grade != now_grade:
        first_max = test.iloc[[first_index, i-1], :].max()

        first_index = i
        last_grade = now_grade
        text = ["{} 학년에서 국어 점수가 가장 높은 사람 : {}{}".format(
            first_max.iloc[0], first_max.iloc[2], first_max.iloc[3])]
        text_list.append(text)

first_max = test.iloc[[first_index, i-1], :].max()
text = ["{} 학년에서 국어 점수가 가장 높은 사람 : {}{}".format(
    first_max.iloc[0], first_max.iloc[2], first_max.iloc[3])]
text_list.append(text)

dataframe = pd.DataFrame(text_list)
dataframe.to_csv("./Day13/학년별 최고점.csv", header=False, index=False)
