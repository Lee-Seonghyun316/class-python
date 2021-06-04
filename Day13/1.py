# 각 학년의 반별 평균 구하기
# 학년 반이 같은 것들끼리 성적끼리의 mean 구하기
# from datetime import datetime
import pandas as pd
# from pandas.core.frame import DataFrame
from pandas import DataFrame

test = pd.read_csv('./Day13/시험 성적.csv', index_col=2, encoding='UTF-8')
same = ""


class_number = list(test["반"])
grade = list(test["학년"])
# class number 로 돌아갈 때
# 현재 반값이랑 이전 반값이랑 다르면
# 처음부터 이전 값까지의 평균 구하기
# + 현재 인덱스값 처음값에 넣기
# 현 재 반 값 이전 반값에 넣기
# 같으면 넘어가기
last = 1
same_index = 0
grade_index = 1
text = ""
text_list = []

for i in range(0, len(test)):
    index = class_number[i]
    if last != index:
        first_mean = test.iloc[[same_index, i-1], [4, 5, 6]].mean()
        print("{} 학년 {}반의 전체 평균 점수 : {}".format(grade_index, last,
                                                (first_mean.iloc[0]+first_mean[1]+first_mean[2])/3))
        text = ["{} 학년 {}반의 전체 평균 점수 : {}".format(grade_index, last,
                                                  (first_mean.iloc[0]+first_mean[1]+first_mean[2])/3)]
        text_list.append(text)
        same_index = i
        last = index
        grade_index = grade[i]

first_mean = test.iloc[[same_index, i-1], [4, 5, 6]].mean()
print("{} 학년 {}반의 전체 평균 점수 : {}".format(grade_index, last,
                                        (first_mean.iloc[0]+first_mean[1]+first_mean[2])/3))
text = ["{} 학년 {}반의 전체 평균 점수 : {}".format(grade_index, last,
                                          (first_mean.iloc[0]+first_mean[1]+first_mean[2])/3)]
text_list.append(text)


dataframe = pd.DataFrame(text_list)
dataframe.to_csv("./Day13/반별 평균.csv", header=False, index=False)
