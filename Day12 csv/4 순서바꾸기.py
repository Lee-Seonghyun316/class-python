# 순서바꾸기
# 4. 저장된 데이터의 순서를 엑셀의 순서를 학년, 반, 학번, 성, 이름, 국어성적, 수학성적, 영어성적에서 학번, 학년, 반, 성, 이름, 국어성적, 수학성적, 영어성적 으로 변경하시오.

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
