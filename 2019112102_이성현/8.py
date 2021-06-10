import csv
from pandas import DataFrame

# test = pd.read_csv('./2019112102_이성현/2019112102 이성현.csv', encoding='UTF-8')

# text_list = ["이성현", 2019112102, "정보통신공학과"]
# # print(test)


# dataframe = pd.DataFrame(text_list)
# dataframe.to_csv("./2019112102_이성현/2019112102 이성현.csv",  index=False)


f = open('./2019112102_이성현/2019112102 이성현.csv', 'w', encoding='utf-8')
wr = csv.writer(f)
wr.writerow(["이성현", 2019112102, "정보통신공학과"])


f.close()
