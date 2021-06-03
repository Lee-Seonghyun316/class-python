# 반별평균
import csv

f = open('./Day12 csv/시험 성적.csv', 'r')
rdr = csv.reader(f)

grade = '1'
class_name = '1'
average = []
temp = 0
averagename = []
count = 0

for line in rdr:
    if (line[1] == '반'):
        continue
    if(grade == line[0]):
        if(class_name == line[1]):
            temp += float(line[5])
            temp += float(line[6])
            temp += float(line[7])
            count += 3
        else:
            averagename.append(grade)
            averagename.append(class_name)
            averagename.append(temp/count)
            average.append(averagename)
            averagename = []
            class_name = line[1]
            temp = 0
            count = 0
            temp += float(line[5])
            temp += float(line[6])
            temp += float(line[7])
            count += 3

    else:
        averagename.append(grade)
        averagename.append(class_name)
        averagename.append(temp/count)
        average.append(averagename)
        averagename = []
        class_name = '1'
        grade = line[0]
        temp = 0
        temp += float(line[5])
        temp += float(line[6])
        temp += float(line[7])
        count += 3
averagename.append(grade)
averagename.append(class_name)
averagename.append(temp/count)
average.append(averagename)
f.close()
final = []
for line in average:
    final.append(["{}학년 {}반의 전체 평균 점수 : {}".format(line[0], line[1], line[2])])
f = open('./Day12 csv/반별 평균.csv', 'w', newline='')
wr = csv.writer(f)

for line in final:
    wr.writerow(line)

f.close()
