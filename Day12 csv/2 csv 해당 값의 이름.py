# 과목별 최고점
# 2. 각 학년의 과목별 최고점을 구하시오 ( 그 학생의 이름출력)

# csv 사용하기
import csv

# 파일 읽어오기 , 파일명과 path 변경
f = open('./Day12 csv/시험 성적.csv', 'r')
rdr = csv.reader(f)

# 맨 처음 학년 초기화
grade = '1'
maxvalue_kor = 0
maxname_kor = ""
maxvalue_math = 0
maxname_math = ""
maxvalue_eng = 0
maxname_eng = ""
maxvalue = ""
maxlist = []

# 첫번째 행의 이름은 continue로 건너뛰기 : 열의 이름이라서
# 학년이 달라질 때마다 학년별 국어, 수학, 영어의 최고점을 구한다. (비교연산으로 )
# 성과 이름을 더해 최고점을 가진 사람이 누군지 저장한다.
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
        # 학년 배뀔 때 최고점 연산 ㄱ
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
        if(maxvalue_kor < float(line[5])):
            maxvalue_kor = float(line[5])
            maxname_kor = line[3]+line[4]
        if(maxvalue_math < float(line[6])):
            maxvalue_math = float(line[6])
            maxname_math = line[3]+line[4]
        if(maxvalue_eng < float(line[7])):
            maxvalue_eng = float(line[7])
            maxname_eng = line[3]+line[4]

# ㄱ반복
maxvalue = "{}학년에서 국어 점수가 가장 높은 사람 : {}".format(grade, maxname_kor)
maxlist.append([maxvalue])
maxvalue = "{}학년에서 수학 점수가 가장 높은 사람 : {}".format(grade, maxname_math)
maxlist.append([maxvalue])
maxvalue = "{}학년에서 영어 점수가 가장 높은 사람 : {}".format(grade, maxname_eng)
maxlist.append([maxvalue])

print(maxlist)

f.close()


# 새로운 파일에 작성
f = open('./Day12 csv/과목별 최고점.csv', 'w', newline='')
wr = csv.writer(f)

for line in maxlist:
    wr.writerow(line)


f.close()
