# 가변 매개 변수 이용, 모두 곱한다.
def mul(*numbers):
    result = 1
    for n in numbers:
        result *= n
    return result
# 가변 매개변수(리스트로 들어옴)로 입력 받아 그 값들을 모두 곱하는 함수
# 단, 매개 변수들은 모두 숫자라고 가정


print(mul(7, 2, 3))
