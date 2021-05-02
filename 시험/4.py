# 팩토리얼 프로그램

data1, data2 = input("팩토리얼 계산 : 공백 기준 숫자 두개 입력").split()
data1 = int(data1)
data2 = int(data2)

if 0 > data1:
    print("팩토리얼은 음수계산 불가")

if 0 > data2:
    print("팩토리얼은 음수계산 불가")
# 범위 벗어나면 에러출력
# 팩토리얼은 0 이하 계산 불가

# 사용자 함수 사용


def factorial(n):
    if n <= 1:
        factorial_result = 1
        return factorial_result
    else:
        factorial_result = n * factorial(n-1)
        return factorial_result


result1 = factorial(data1)
result2 = factorial(data2)

bigger = result1
smaller = result2

if result1 > result2:
    bigger = result1
    smaller = result2
else:
    bigger = result2
    smaller = result1
print(bigger)

minus = bigger - smaller

print("큰 팩토리얼 결과값 : ", bigger, "작은 팩토리얼 결과값", smaller)
print("두 팩토리얼 결과값의 차이 : ", minus)
