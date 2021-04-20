# 시그마 연산 함수 구현하기

def cal(num):
    if num < 0:
        return 'error'
        # 음수 전달 시 에러
    else:
        return num*(2**(num-1))
# an 만들기


data = input()
num = int(data)
# 데이터 입력

sum = 0
for i in range(1, num+1):
    sum += cal(i)
# 시그마an 함수 연산

print(sum)
