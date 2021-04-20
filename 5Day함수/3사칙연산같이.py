# 한번에 사칙연산 수행하는 함수 구현

def acc(num_1, num_2):
    mul = num_1 * num_2
    if num_2 == 0:
        div = 'error'
    else:
        div = num_1 / num_2
# 0이면 오류 출력하게
    plu = num_1 + num_2
    min = num_1 - num_2
    return mul, div, plu, min


data_1, data_2 = input().split()
num_1 = int(data_1)
num_2 = int(data_2)
# 데이터 입력

print(acc(num_1, num_2))
