# 학년별 성씨 별 최고점 이름 출력
# 3. 학년 별로 성씨 별로 가장 성적이 높은 사람의 이름을 출력

# csv 사용하기
import csv

# 파일 읽어오기 , 파일명과 path 변경
f = open('./Day12 csv/시험 성적.csv', 'r')
test = csv.reader(f)
for i in test:
    print(i[0])
f.close()

# f = open('./Day12 csv/학년성씨별.csv', 'w', newline='')
# wr = csv.writer(f)

# for line in text_list:
#     wr.writerow(line)
# f.close()
