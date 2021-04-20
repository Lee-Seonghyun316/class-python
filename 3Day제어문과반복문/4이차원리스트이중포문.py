# 학생의 평균구하기
# 이차원리스트 사용
kor_score = [49, 80, 20, 100, 80]
mathe_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]

midterm_score = [kor_score, mathe_score, eng_score]
# 이차원 리스트 생성
print(midterm_score)
student_mean = []

for i in range(0, 5):
    sum = 0
    for j in range(0, 3):
        sum += midterm_score[j][i]
    average = sum/3
    student_mean.append(average)
    # 학생 각각의 평균구해서 리스트에 추가

print(student_mean)
