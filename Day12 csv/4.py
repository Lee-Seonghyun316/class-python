# 순서바꾸기
import csv

f = open('./Day12 csv/시험 성적.csv', 'r')
rdr = csv.reader(f)

text = []
for line in rdr:
    text.append([line[2], line[0], line[1], line[3],
                 line[4], line[5], line[6], line[7]])

# print(text)
f.close()

f = open('./Day12 csv/학번먼저.csv', 'w', newline='')
wr = csv.writer(f)

for line in text:
    wr.writerow(line)


f.close()
