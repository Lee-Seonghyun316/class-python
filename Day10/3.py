# 3차원 행렬
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
