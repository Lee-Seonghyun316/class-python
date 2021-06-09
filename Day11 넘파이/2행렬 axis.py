# 학생 4 명의 4 과목 성적을 16 (4x4)개의 정수로 입력 받고 저장하시오. (개수가 안 맞을 경우 에러 출력)
# 2 차원 행렬에 형태를 바꾸어 저장하시오 (reshape )
# 각 과목별 성적의 평균과 학생의 평균을 axis 를 활용하여 구하시오

import numpy as np
exam = list(map(int, input("공백기준 16개의 성적을 입력하시오(학생 1명의 4과목 성적 * 4명)\n").split()))
if len(exam) != 16:
    print("error")
else:
    exam = np.array(exam)
    exam = exam.reshape(4, 4)
    print(exam)
    students_sum = exam.sum(axis=1)
    subject_sum = exam.sum(axis=0)
    print("학생별 평균 : {}\n과목별 평균 : {}".format(students_sum/4, subject_sum/4))
