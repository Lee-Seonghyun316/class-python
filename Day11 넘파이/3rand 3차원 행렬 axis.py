# 3차원 행렬

# 1 학년에 10 반이 있고, 각 반에 10 명의 학생이 있다고 가정하고, 4 과목이 있다고 가정하시오
# 랜덤함수를 사용하여 각 반의 학생들의 성적을 2 차원 배열로 구성하시오
# -> 결과적으로 10 반이 있으니 3 차원 배열로 구성
# 3 차원 배열을 활용하여 과목별 전체 평균과 반별 평균을 구하시오.
# 기왕이면 axis 사용 요망

import numpy as np

score = np.random.rand(10, 10, 4)
# 10개반, 10명, 4개과목
# print(score)
subject_average = score.sum(axis=1)
subject_average = subject_average.sum(axis=0)
# print(subject_average)
class_average = score.sum(axis=1)
class_average = class_average.sum(axis=1)
# print(class_average)

print("과목별 평균 : {} \n 반별 평균 : {} \n".format(subject_average, class_average))
