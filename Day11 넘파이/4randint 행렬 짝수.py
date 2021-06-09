# 3*3 행렬을 randint() 함수를 사용하여 정수로 채우시오
# 원본과 해당 행렬의 짝수만 추출하여 화면에 출력하시오
# boolean indexing 메소드를 참고하시오

import numpy as np
from numpy.core.fromnumeric import reshape

A = np.random.randint(0, 10, 9).reshape(3, 3)
B = []
for i in range(0, 3):
    for j in range(0, 3):
        if A[i][j] % 2 == 0:
            B.append(A[i][j])
print(A)
print(B)
# 0도 제외해야 할 듯
