# 데이터 순서 바꾸기
# 순서바꾸기
# 4. 저장된 데이터의 순서를 엑셀의 순서를 학년, 반, 학번, 성, 이름, 국어성적, 수학성적, 영어성적에서 학번, 학년, 반, 성, 이름, 국어성적, 수학성적, 영어성적 으로 변경하시오.

import pandas as pd
from pandas import DataFrame

test = pd.read_csv('./Day13 pandas/시험 성적.csv', encoding='UTF-8')

test = test[['학번', '학년', '반', '성', '이름', '국어성적', '수학성적', '영어성적']]
# print(test)

dataframe = pd.DataFrame(test)
dataframe.to_csv("./Day13 pandas/학번먼저.csv",  index=False)
