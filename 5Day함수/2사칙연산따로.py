# 사칙 연산 따로 하는 프로그램 구현

data_1, data_2 = input().split()
# 공백 기준 데이터 입력 받기
num_1 = int(data_1)
num_2 = int(data_2)
# 자료형 정수로 변환

# 사칙연산함수


def mul(num_1, num_2):
    return num_1 * num_2


print(mul(num_1, num_2))

# 0으로 나눌 때 에러출력


def div(num_1, num_2):
    if num_2 == 0:
        return 'error'
    else:
        return num_1 / num_2


print(div(num_1, num_2))


def plu(num_1, num_2):
    return num_1 + num_2


print(plu(num_1, num_2))


def min(num_1, num_2):
    return num_1 - num_2


print(min(num_1, num_2))
