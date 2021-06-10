# 10개 숫자 랜덤으로 입력밭고
# 람다로 10더해서 출력

import numpy as np
from numpy.core.fromnumeric import reshape

A = np.random.randint(0, 100, 10)

ten_plus = list(map(lambda x: x + 10, A))
print(A)
print(ten_plus)
