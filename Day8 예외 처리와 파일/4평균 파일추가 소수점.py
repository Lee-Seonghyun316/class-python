import math
# Day8 폴더 안에 있어야 실행 된다!

# 학생의 성적이 실수 형태로 score.txt 파일에 저장되어 있다고 가정하시오
# 이 성적을 읽고 파일의 끝에 소수점 첫번째 까지의 평균값을 기록하시오

f = open("./Day8 예외 처리와 파일/4.txt", 'r')
data = f.read()


f.close()
# writedata.py
f = open("./Day8 예외 처리와 파일/4.txt", 'a')
a = data.split("\n")
for i in range(0, len(a)):
    a[i] = float(a[i])

average = sum(a)/len(a)

b = math.floor(average*10)/10
f.write('\n'+str(b))
f.close()
