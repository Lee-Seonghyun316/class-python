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
