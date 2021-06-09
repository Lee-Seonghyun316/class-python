# pandas
# 각 학년의 반별 평균 구하기
# 학년 반이 같은 것들끼리 성적끼리의 mean 구하기
# 구한 숫자 그대로 입력
import pandas as pd
from pandas import DataFrame

test = pd.read_csv('./Day13 pandas/시험 성적.csv', index_col=2, encoding='UTF-8')

class_number = list(test["반"])
grade = list(test["학년"])

# class number 로 반복문 돌아갈 때
# now_class이랑 last_class이랑 다르면
# first_index부터 이전 인덱스값까지의 평균 구하기
# 몇학년 몇반인지는 바뀌긴 전 값으로 넣어주면 된다.
# 현재 인덱스값 first_index부터 넣기
# now_class 이전 last_class에 넣기
# 같으면 넘어가기

last_class = 1
first_index = 0
grade_index = 1
text = ""
text_list = []

for i in range(0, len(test)):
    now_class = class_number[i]
    if last_class != now_class:
        first_mean = test.iloc[[first_index, i-1], [4, 5, 6]].mean()
        text = ["{} 학년 {}반의 전체 평균 점수 : {}".format(grade_index, last_class,
                                                  (first_mean.iloc[0]+first_mean[1]+first_mean[2])/3)]
        text_list.append(text)
        first_index = i
        last_class = now_class
        grade_index = grade[i]

first_mean = test.iloc[[first_index, i-1], [4, 5, 6]].mean()
text = ["{} 학년 {}반의 전체 평균 점수 : {}".format(grade_index, last_class,
                                          (first_mean.iloc[0]+first_mean[1]+first_mean[2])/3)]
text_list.append(text)


dataframe = pd.DataFrame(text_list)
dataframe.to_csv("./Day13 pandas/반별 평균.csv", header=False, index=False)
