import csv

f = open('./Day12 csv/시험 성적.csv', 'r')
rdr = csv.reader(f)

grade = '1'


maxvalue_kor = 0
maxname_kor = ""
maxvalue_math = 0
maxname_math = ""
maxvalue_eng = 0
maxname_eng = ""
maxvalue = ""
maxlist = []
for line in rdr:
    print(line[0])
    if (line[1] == '반'):
        continue
    # print(line[1])
    if(grade == line[0]):
        if(maxvalue_kor < float(line[5])):
            maxvalue_kor = float(line[5])
            maxname_kor = line[3]+line[4]
        if(maxvalue_math < float(line[6])):
            maxvalue_math = float(line[6])
            maxname_math = line[3]+line[4]
        if(maxvalue_eng < float(line[7])):
            maxvalue_eng = float(line[7])
            maxname_eng = line[3]+line[4]
    else:
        maxvalue = "{}학년에서 국어 점수가 가장 높은 사람 : {}".format(grade, maxname_kor)
        maxlist.append([maxvalue])
        maxvalue = "{}학년에서 수학 점수가 가장 높은 사람 : {}".format(grade, maxname_math)
        maxlist.append([maxvalue])
        maxvalue = "{}학년에서 영어 점수가 가장 높은 사람 : {}".format(grade, maxname_eng)
        maxlist.append([maxvalue])
        maxvalue_kor = 0
        maxvalue_math = 0
        maxvalue_eng = 0
        grade = line[0]

maxvalue = "{}학년에서 국어 점수가 가장 높은 사람 : {}".format(grade, maxname_kor)
maxlist.append([maxvalue])
maxvalue = "{}학년에서 수학 점수가 가장 높은 사람 : {}".format(grade, maxname_math)
maxlist.append([maxvalue])
maxvalue = "{}학년에서 영어 점수가 가장 높은 사람 : {}".format(grade, maxname_eng)
maxlist.append([maxvalue])

print(maxlist)

f.close()

f = open('./Day12 csv/과목별 최고점.csv', 'w', newline='')
wr = csv.writer(f)

for line in maxlist:
    wr.writerow(line)
# wr.writerow("{}학년 {}반의 전체 평균 점수 : {}".format(line[0], line[1], line[2]))
# wr.writerow([2, '김갑환', '서울'])

f.close()
