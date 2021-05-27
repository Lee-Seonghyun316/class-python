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
