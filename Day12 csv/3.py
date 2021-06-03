import csv

f = open('./Day12 csv/시험 성적.csv', 'r')
rdr = csv.reader(f)

class_name = '1'
average = []
temp = 0
averagename = []
count = 0


grade = '1'
maxvalue = 0
maxtext = ""
maxlist = []
maxname = ""

first_name = '김'

for line in rdr:
    if (line[1] == '반'):
        continue
    # print(line[1])
    if(grade == line[0]):
        if(first_name == line[3]):
            if(maxvalue < float(line[5])):
                maxvalue = float(line[5])
                maxname = line[3]+line[4]
            if(maxvalue < float(line[6])):
                maxvalue = float(line[6])
                maxname = line[3]+line[4]
            if(maxvalue < float(line[7])):
                maxvalue = float(line[7])
                maxname = line[3]+line[4]
        else:
            maxtext = "{}학년 {}씨 중에서 가장 높은 성적을 받은 이의 이름 : {}".format(
                grade, first_name, maxname)
            maxlist.append([maxtext])
            first_name = line[3]
            maxvalue = 0
            if(maxvalue < float(line[5])):
                maxvalue = float(line[5])
                maxname = line[3]+line[4]
            if(maxvalue < float(line[6])):
                maxvalue = float(line[6])
                maxname = line[3]+line[4]
            if(maxvalue < float(line[7])):
                maxvalue = float(line[7])
                maxname = line[3]+line[4]
    else:
        maxtext = "{}학년 {}씨 중에서 가장 높은 성적을 받은 이의 이름 : {}".format(
            grade, first_name, maxname)
        maxlist.append([maxtext])
        first_name = line[3]
        maxvalue = 0
        grade = line[0]
        if(maxvalue < float(line[5])):
            maxvalue = float(line[5])
            maxname = line[3]+line[4]
        if(maxvalue < float(line[6])):
            maxvalue = float(line[6])
            maxname = line[3]+line[4]
        if(maxvalue < float(line[7])):
            maxvalue = float(line[7])
            maxname = line[3]+line[4]

maxtext = "{}학년 {}씨 중에서 가장 높은 성적을 받은 이의 이름 : {}".format(
    grade, first_name, maxname)
maxlist.append([maxtext])

print(maxlist)
f.close()

f = open('./Day12 csv/학년성씨별.csv', 'w', newline='')
wr = csv.writer(f)

for line in maxlist:
    wr.writerow(line)
# wr.writerow("{}학년 {}반의 전체 평균 점수 : {}".format(line[0], line[1], line[2]))
# wr.writerow([2, '김갑환', '서울'])

f.close()
