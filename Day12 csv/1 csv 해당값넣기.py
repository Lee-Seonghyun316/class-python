# 반별평균
# 1. 각 학년의 반별 평균을 구하여 별도의 엑셀 파일에 저장하시오

# csv 사용하기
import csv

# 파일 읽어오기 , 파일명과 path 변경
f = open('./Day12 csv/시험 성적.csv', 'r')
rdr = csv.reader(f)

# 맨 처음 학년과 반 번호 초기화
grade = '1'
class_name = '1'
average = []
temp = 0
averagename = []
count = 0

# 첫번째 행의 이름은 continue로 건너뛰기 : 열의 이름이라서
# 반이 달라질 때마다 평균을 구한다.
# 그 평균은 list에 저장하여 csv로 만든다.
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
            # ㄱ
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
        # ㄱ 반복
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

# ㄱ 반복
averagename.append(grade)
averagename.append(class_name)
averagename.append(temp/count)
average.append(averagename)
f.close()

# 문제에서 말하는 형태로 변환
# 한줄 당 하나의 리스트가 들어가도록 작성
final = []
for line in average:
    final.append(["{}학년 {}반의 전체 평균 점수 : {}".format(line[0], line[1], line[2])])


# 새로운 파일에 작성
f = open('./Day12 csv/반별 평균.csv', 'w', newline='')
wr = csv.writer(f)

for line in final:
    wr.writerow(line)

f.close()
