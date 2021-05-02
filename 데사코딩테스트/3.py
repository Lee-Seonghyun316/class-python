# 3번
num = int(input("별 피라미드 행의 숫자 입력"))

for i in range(1, num+1):
    for j in range(i):
        print("*", end="")
    print()
