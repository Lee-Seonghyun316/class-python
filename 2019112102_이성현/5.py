import pandas as pd
from pandas import DataFrame

test = pd.read_csv('./2019112102_이성현/시험 성적.csv', index_col=1, encoding='UTF-8')


sum_value = (test["국어성적"])+(test["수학성적"])+(test["영어성적"])
name = (test["성"]+test["이름"])
name_list = []
sum_value_list = []
for i in sum_value:
    # print(i)
    sum_value_list.append(i)

for i in name:
    # print(i)
    name_list.append(i)

# print(len(sum_value_list))
# print(sum_value_list)

# print(max(sum_value_list))
max_sum = max(sum_value_list)
max_mean = max(sum_value_list)/3

# print(sum_value_list.index(max_sum))
# print(name_list[16])


print("{} : {}".format(name_list[16], max_mean))
