# 각 학년의 과목별 최고점 구하기
# 학년 과목이 같은 것들끼리 성적끼리의 max 구하기
# + 그 이름 출력하기

# 주의 : max를 쓰면 column 별 큰 값 출력 -> max의 이름이 아님
# sort 를 이용-첫번재 값(max) 와 그 이름 출력

import pandas as pd
from pandas import DataFrame

test = pd.read_csv('./Day13 pandas/시험 성적.csv', index_col=2, encoding='UTF-8')

# class_number = list(test["반"])
grade = list(test["학년"])
# print(grade)

# grade 로 반복문
# 이전 학년과 last_grade다르면
# 처음인덱스 first_index 부터
#  이전인덱스까지의 과목별 max 구하기

# 현재 인덱스를 처음인덱스에 first_index 넣기
# 현재 학년 이전 학년 last_grade에 넣기
# 이전학년 last_grade 초기값은 1

# 처음 인덱스first_index 초기값은 0
# 같으면 넘어가기

last_grade = 1
first_index = 0

# 이중 리스트로 csv 생성할 것임
text_list = []


def search_max(first_index, i, now_grade):
    kor_sort = test.iloc[first_index:i, :].sort_values('국어성적')
    kor_max = kor_sort.iloc[[len(kor_sort)-1], :].max()

    math_sort = test.iloc[first_index:i, :].sort_values('수학성적')
    math_max = math_sort.iloc[[len(math_sort)-1], :].max()

    eng_sort = test.iloc[first_index:i, :].sort_values('영어성적')
    eng_max = eng_sort.iloc[[len(eng_sort)-1], :].max()

    first_index = i
    last_grade = now_grade

    kor_text = ["{} 학년에서 국어 점수가 {} 으로 가장 높은 사람 : {}{}".format(
        kor_max.iloc[0], kor_max.iloc[4], kor_max.iloc[2], kor_max.iloc[3])]
    print(kor_text)
    text_list.append(kor_text)

    math_text = ["{} 학년에서 수학 점수가 {} 으로 가장 높은 사람 : {}{}".format(
        math_max.iloc[0], math_max.iloc[5], math_max.iloc[2], math_max.iloc[3])]
    print(math_text)
    text_list.append(math_text)

    eng_text = ["{} 학년에서 영어 점수가 {} 으로 가장 높은 사람 : {}{}".format(
        eng_max.iloc[0], eng_max.iloc[6], eng_max.iloc[2], eng_max.iloc[3])]
    print(eng_text)
    text_list.append(eng_text)

    return last_grade, first_index


for i in range(0, len(test)):
    now_grade = grade[i]
    if last_grade != now_grade:
        last_grade, first_index = search_max(first_index, i, now_grade)

search_max(first_index, i, now_grade)

dataframe = pd.DataFrame(text_list)
dataframe.to_csv("./Day13 pandas/학년별 최고점.csv", header=False, index=False)
