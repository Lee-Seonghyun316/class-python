import pandas as pd
from pandas import DataFrame

test = pd.read_csv('./2019112102_이성현/시험 성적.csv', encoding='UTF-8')

test = test[['학번', '학년', '반', '성', '이름', '국어성적', '수학성적', '영어성적']]
# print(test)

dataframe = pd.DataFrame(test)
dataframe.to_csv("./Day13 pandas/학번먼저.csv",  index=False)
